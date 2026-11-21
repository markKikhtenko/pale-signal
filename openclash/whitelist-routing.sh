#!/bin/sh
. /usr/share/openclash/ruby.sh
. /usr/share/openclash/log.sh
. /lib/functions.sh

# OpenClash Custom Overwrite Script
# Назначение:
#   1. Явно отправлять сервисы из публичных/операторских белых списков через DIRECT.
#   2. Возвращать для них реальные IP вместо Fake-IP.
#   3. Резолвить белые домены и адреса прокси-нод через DNS Huawei/MegaFon.
#   4. Не отправлять напрямую вообще всю зону .ru или весь GEOIP RU.
#   5. Принудительно отправлять Т-Банк/Тинькофф, Т-Инвестиции, Сбер и Спортмастер
#      через основную VPN-политику.
#
# Основа: проверенная рабочая версия от 2026-07-22
# Обновлено: 2026-08-21
# Изменил: ChatGPT
# Изменения: DION удалён из специальных правил; предыдущие правила банков,
# Спортмастера и Т-Инвестиций сохранены без изменений.
# Остальная логика, включая DNS, белый список и Fake-IP, не изменялась.

LOG_TIP "Start Running Custom Overwrite Scripts..."
LOGTIME="$(date '+%Y-%m-%d %H:%M:%S')"
LOG_FILE="/tmp/openclash.log"
CONFIG_FILE="$1"

[ -n "$CONFIG_FILE" ] || {
  LOG_OUT "[Error] Custom overwrite: config path is empty"
  exit 1
}

ruby -ryaml -E UTF-8 -e "# encoding: UTF-8
begin
  file = '$CONFIG_FILE'
  value = YAML.load_file(file)

  raise 'Configuration root is not a YAML map' unless value.is_a?(Hash)

  value['rules'] = [] unless value['rules'].is_a?(Array)

  # Домены Т-Банка/Т-Инвестиций, Сбера и Спортмастера должны всегда идти через VPN,
  # даже если они присутствуют в операторском или публичном белом списке.
  vpn_domains = %w[
    tbank.ru
    tinkoff.ru
    t-bank-app.ru
    cdn-tinkoff.ru
    tinkoff-mobile.ru
    sber.ru
    sberbank.ru
    sbermarket.ru
    sbermegamarket.ru
    sbermobile.ru
    sportmaster.ru
  ].map(&:downcase).uniq.sort

  # Определяем основную VPN-политику из завершающего MATCH/FINAL правила
  # исходной конфигурации подписки.
  terminal_rule = value['rules'].reverse.find { |rule|
    rule.is_a?(String) && rule.match?(/\A(?:MATCH|FINAL),/)
  }

  raise 'MATCH/FINAL rule was not found; VPN policy cannot be detected' unless terminal_rule

  vpn_policy = terminal_rule.split(',', 3)[1].to_s.strip

  raise 'VPN policy in MATCH/FINAL rule is empty' if vpn_policy.empty?

  if %w[DIRECT REJECT REJECT-DROP PASS].include?(vpn_policy.upcase)
    raise 'MATCH/FINAL policy is not a VPN group: ' + vpn_policy
  end

  whitelist_domains = []

  # observed_public_whitelist
  whitelist_domains.concat(%w[
    2gis.com 2gis.ru 47news.ru alfabank.ru auth-nsdi.ru auto.ru avito.ru avito.st cdn-tinkoff.ru
    cdn-vk.ru cikrf.ru digital.gov.ru dobro.ru duma.gov.ru dzen.ru evotor.ru gazeta.ru
    genproc.gov.ru gosuslugi.ru government.ru gu-st.ru hrlink.ru izbirkom.ru kinopoisk.ru kp.ru
    kremlin.ru lemanapro.ru lenta.ru lizaalert.org lmru.tech mail.ru max.ru mradx.net ofd.ru ok.ru
    okcdn.ru oneme.ru onf.ru ozon.ru ozone.ru pochta.ru rambler.ru rbc.ru res-nsdi.ru
    roskachestvo.gov.ru rutube.ru rutubelist.ru rzd.ru sber.ru sberbank.ru sirius.online
    sochisirius.ru t2.ru taximaxim.ru tbank.ru tutu.ru userapi.com vk-portal.net vk.com vk.ru
    vtb.ru wb.ru wildberries.ru xn--80ajghhoc2aj1c8b.xn--p1ai ya.ru yandex.com yandex.net yandex.ru
    yastatic.net
  ])

  # yandex_and_cdn
  whitelist_domains.concat(%w[
    edadeal.ru kinopoisk.com yandexaudio.net yandexcdn.net yandexcloud.net yandexvideo.net
  ])

  # marketplaces_and_retail
  whitelist_domains.concat(%w[
    5ka.ru auchan.ru av.ru azbukavkusa.ru chizhik.club citilink.ru detmir.ru dixy.ru dns-shop.ru
    eldorado.ru lenta.com magnit.ru megamarket.ru metro-cc.ru mvideo.ru okmarket.ru perekrestok.ru
    pyaterochka.ru sbermegamarket.ru sportmaster.ru vkusvill.ru vprok.ru
  ])

  # delivery_and_food
  whitelist_domains.concat(%w[
    burgerkingrus.ru cdek.ru kuper.ru rostics.ru samokat.ru sbermarket.ru vkusnoitochka.ru
  ])

  # banks_and_payments
  whitelist_domains.concat(%w[
    cbr.ru finuslugi.ru gazprombank.ru mironline.ru moex.com mtsbank.ru nspk.ru psbank.ru
    tinkoff.ru
  ])

  # government_and_social
  whitelist_domains.concat(%w[
    bus.gov.ru council.gov.ru dom.gosuslugi.ru mchs.gov.ru minfin.gov.ru mos.ru mosreg.ru mvd.ru
    nalog.gov.ru roskazna.gov.ru rosreestr.gov.ru zakupki.gov.ru
  ])

  # telecom
  whitelist_domains.concat(%w[
    beeline.ru dom.ru megafon.ru motivtelecom.ru mts.ru rostelecom.ru rt.ru sbermobile.ru
    tinkoff-mobile.ru
  ])

  # vk_mail_and_cdn
  whitelist_domains.concat(%w[
    mycdn.me vk-cdn.net vkuseraudio.net vkuserlive.com vkuserlive.net
  ])

  # media
  whitelist_domains.concat(%w[
    1tv.ru 360.ru 5-tv.ru aif.ru ctc.ru domashniy.ru dumatv.ru friday.ru iz.ru kommersant.ru
    matchtv.ru mir24.tv mk.ru muz-tv.ru ntv.ru otr-online.ru pnp.ru radioplayer.ru ren.tv rg.ru
    ria.ru rt.com smotrim.ru soloviev.live spastv.ru sport24.ru tass.ru tnt-online.ru tv3.ru tvc.ru
    tvzvezda.ru vedomosti.ru vesti.ru vitrina.tv vmeste-rf.tv
  ])

  # transport_maps_and_services
  whitelist_domains.concat(%w[
    1c.ru gismeteo.ru glonass.com grandtrain.ru hh.ru khl.ru kontur.ru mamadeti.ru medsi.ru
    rosagroleasing.ru rosatom.ru rosneft.ru rosseti.ru rostec.ru ruwiki.ru sbis.ru tensor.ru
    trueconf.ru
  ])

  whitelist_domains = whitelist_domains.map(&:downcase).uniq.sort

  # Даже если домены банка случайно добавлены в один из списков выше,
  # удаляем их из DIRECT-белого списка.
  whitelist_domains -= vpn_domains

  # Т-Банк/Т-Инвестиции, Сбер и Спортмастер должны попасть под VPN-правила раньше
  # любых DIRECT-правил и раньше правил из основной подписки.
  vpn_rules = vpn_domains.map { |domain|
    'DOMAIN-SUFFIX,' + domain + ',' + vpn_policy
  }

  # Системные сети всегда DIRECT.
  infrastructure_rules = [
    'IP-CIDR,192.168.1.0/24,DIRECT,no-resolve',
    'IP-CIDR,192.168.8.0/24,DIRECT,no-resolve',
    'IP-CIDR,10.153.0.0/16,DIRECT,no-resolve'
  ]

  # Точное правило для Яндекс Музыки оставляем первым среди DIRECT-доменов.
  exact_rules = [
    'DOMAIN,music.yandex.ru,DIRECT'
  ]

  domain_rules = whitelist_domains.map { |domain|
    'DOMAIN-SUFFIX,' + domain + ',DIRECT'
  }

  direct_rules = infrastructure_rules + exact_rules + domain_rules

  # Удаляем правила от старых версий скрипта.
  obsolete_rules = [
    'DOMAIN-SUFFIX,ru,DIRECT',
    'DOMAIN-SUFFIX,su,DIRECT',
    'DOMAIN-SUFFIX,xn--p1ai,DIRECT',
    'GEOIP,RU,DIRECT',
    'GEOIP,RU,DIRECT,no-resolve'
  ]

  # Удаляем старые DIRECT-правила Т-Банка/Т-Инвестиций, Сбера и Спортмастера,
  # которые могли остаться после предыдущих версий overwrite-скрипта.
  vpn_domains.each { |domain|
    obsolete_rules << 'DOMAIN-SUFFIX,' + domain + ',DIRECT'
    obsolete_rules << 'DOMAIN,' + domain + ',DIRECT'
  }

  generated_rules = (vpn_rules + direct_rules).each_with_object({}) { |rule, index|
    index[rule] = true
  }

  obsolete_index = obsolete_rules.each_with_object({}) { |rule, index|
    index[rule] = true
  }

  value['rules'] =
    vpn_rules +
    direct_rules +
    value['rules'].reject { |rule|
      generated_rules.key?(rule) || obsolete_index.key?(rule)
    }

  # Полностью отключаем IPv6 внутри Mihomo.
  value['ipv6'] = false

  value['dns'] = {} unless value['dns'].is_a?(Hash)
  dns = value['dns']

  # DNS Huawei HiLink + DNS текущей сессии MegaFon.
  # Публичные DNS в конце используются как резерв при обычном WAN.
  local_dns = [
    '192.168.8.1',
    '10.153.1.131',
    '10.153.3.196',
    '119.29.29.29',
    '8.8.8.8'
  ]

  dns['enable'] = true
  dns['ipv6'] = false
  dns['prefer-h3'] = false
  dns['respect-rules'] = false
  dns['use-hosts'] = true
  dns['use-system-hosts'] = true

  dns['default-nameserver'] = local_dns.dup
  dns['nameserver'] = local_dns.dup
  dns['proxy-server-nameserver'] = local_dns.dup
  dns['direct-nameserver'] = local_dns.dup
  dns['direct-nameserver-follow-policy'] = true

  dns.delete('fallback')
  dns.delete('fallback-filter')

  dns['nameserver-policy'] = {} unless dns['nameserver-policy'].is_a?(Hash)

  # Удаляем старые DNS-политики доменов, принудительно направляемых через VPN.
  vpn_domains.each { |domain|
    dns['nameserver-policy'].delete(domain)
    dns['nameserver-policy'].delete('+.' + domain)
  }

  whitelist_domains.each { |domain|
    dns['nameserver-policy']['+.' + domain] = local_dns.dup
  }

  # DIRECT-сервисы получают настоящий IP.
  # Т-Банк/Т-Инвестиции, Сбер и Спортмастер сюда намеренно не добавляются и остаются
  # в Fake-IP, чтобы доменные правила гарантированно выбрали VPN.
  dns['fake-ip-filter-mode'] = 'rule'

  real_ip_rules = [
    'DOMAIN,localhost,real-ip',
    'DOMAIN-SUFFIX,lan,real-ip',
    'DOMAIN-SUFFIX,local,real-ip',
    'DOMAIN-SUFFIX,home.arpa,real-ip',
    'DOMAIN,music.yandex.ru,real-ip'
  ]

  whitelist_domains.each { |domain|
    real_ip_rules << 'DOMAIN-SUFFIX,' + domain + ',real-ip'
  }

  real_ip_rules << 'MATCH,fake-ip'
  dns['fake-ip-filter'] = real_ip_rules

  File.open(file, 'w') { |output| YAML.dump(value, output) }

  puts '$LOGTIME [Info] White-list overwrite applied: ' +
       whitelist_domains.length.to_s +
       ' DIRECT domains; T-Bank/T-Investments/Sber/Sportmaster via VPN policy 【' +
       vpn_policy +
       '】'

rescue Exception => e
  puts '$LOGTIME [Error] White-list overwrite failed,【' + e.message + '】'
end
" 2>/dev/null >> "$LOG_FILE"

exit 0
