# pale-signal

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-8093-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

Автоматически обновляемые VLESS-подписки для Mihomo, OpenClash и Happ/Happ Plus.

**Последнее обновление:** `2026-11-12 03:07:30 МСК`

## Подписки

| Файл | Назначение |
|------|------------|
| [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) | Все серверы |
| [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) | Россия |
| [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) | Все non-RU серверы |
| [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) | Global, до 5000 серверов |
| [subscription-lan-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml) | Основная LAN-подписка для проводного интернета, до 5000 серверов; при меньшем пуле совпадает с LAN Global |
| [subscription-lan-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml) | Полный LAN-пул для проводного интернета без лимита |
| [subscription-lan-global-fast-check.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global-fast-check.yaml) | LAN Global Fast Check — те же серверы LAN Global, более активная автоматическая проверка |
| [subscription-lan-experimental.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-experimental.yaml) | Изолированная тестовая LAN-подписка |
| [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) | Тестовая Global |
| [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) | Reality-узлы для режима блокировок |
| [subscription-mobile.txt](https://markkikhtenko.github.io/pale-signal/subscription-mobile.txt) | Компактная мобильная Reality-подписка для Happ/Happ Plus |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `8093` |
| Россия | `1531` |
| Global | `6562` |
| Global 5K | `1760` |
| LAN 5K | `5000` |
| LAN Global | `5270` |
| LAN Global Fast Check | `5270` |
| LAN Experimental | `2203` |
| LAN Experimental AUTO | `2203` |
| Исключено пересечений Experimental с LAN Global | `399` |
| BS Safe MANUAL | `1368` |
| BS Safe AUTO | `50` |
| Happ Mobile | `473` |

<!-- LAN-EXPERIMENTAL:START -->
## LAN Experimental

Изолированная тестовая подписка: `2203` серверов, все входят в `AUTO`. Протоколы: `ss: 385, trojan: 462, vless: 1356`. Дубли и совпадения с `LAN Global` удаляются до публикации. Опубликованный до этого пул сохранён без изменений и используется как базовый; при временной недоступности нового источника используется его последний опубликованный пул. Старые три источника остаются обязательными.

Шесть GitHub YAML-источников `wuge0/free-nodes`, `sakazxc1400/free-vpn-sub`, `learnLi/free-nodes`, `bily1258-design/beimi`, `Delta-Kronecker/V2ray-Config` и `hezhanleiok/freesub` подключены целиком и только к LAN Experimental. Отчёт `WireVeil-Mihomo-Report-20261111-141445.zip` используется как историческая проверка актуальности самих источников и для статистики точных совпадений, а не как поузловой allowlist: при каждом обновлении импортируются все текущие валидные VLESS, Shadowsocks и Trojan. VMess, Hysteria2, невалидные записи, дубли и пересечения с LAN Global по-прежнему исключаются. В отчёте 60 уникальных Good/Partial, из них 4 VMess/Hysteria2 не поддерживаются политикой протоколов; в текущих YAML найдено `20` из `56` поддерживаемых проверенных записей (`13` Good, `7` Partial), а также `2` совпадений запрещённых протоколов.

Результаты выбора источников основаны на одном историческом сетевом аудите от 27.10.2026:

| Источник из аудита 27.10.2026 | HTTPS 2/2 | Good |
|---------------------------------|-----------:|-----:|
| [go4sharing/sub](https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml) | `5/15` | `5` |
| [Ruk1ng001/freeSub](https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml) | `20/63` | `9` |
| [awesome-vpn/awesome-vpn](https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/clash.yaml) | `10/41` | `6` |
| [Misaka-blog/chromego_merge](https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml) | `20/101` | `6` |
| [sunmiao4458/free-proxy-airport](https://raw.githubusercontent.com/sunmiao4458/free-proxy-airport/main/output/clash.yaml) | `8/47` | `2` |
| [ermaozi/get_subscribe](https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml) | `46/346` | `11` |
| [peasoft/NoMoreWalls](https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml) | `28/280` | `6` |

Эти числа описывают только тот сетевой прогон, а не все узлы источников. Валидный YAML и успешный `mihomo -t` подтверждают совместимость конфигурации, но не гарантируют сетевую доступность узла.

Перед добавлением F0rc3Run и ProxyQueen локальный WireVeil Checker проверял HTTPS-доступ к ChatGPT, Instagram, Spotify, Telegram Web и YouTube:

| Источник из локальной проверки WireVeil Checker | Успешно | Проверено |
|-------------------------------------------------|---------:|----------:|
| [F0rc3Run](https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/Best-Results/clash.yaml) | `25` | `178` |
| [ProxyQueen](https://raw.githubusercontent.com/lyqnihao/proxy/main/proxyqueen/output.yaml) | `13` | `81` |

Результаты WireVeil — исторический ориентир на момент локальной проверки, а не гарантия актуальной работоспособности и не live-проверка при сборке. Разрешены только VLESS, Shadowsocks и Trojan; VMess и Hysteria2 исключаются.

| Источник | Статус | Последнее успешное обновление | Загружено | Найдено WireVeil | Good | Partial | Исключено по протоколу | Разобрано | Неподдерживаемых | Невалидных | Отфильтровано | Дубли | LAN Global | Лимит | Отброшено | Добавлено | Протоколы | Причины исключения |
|----------|--------|------------------------------|-----------:|-------------------:|-----:|--------:|-----------------------:|----------:|------------------:|-----------:|---------------:|-------:|-----------:|------:|----------:|---------:|-----------|--------------------|
| [MorpheusAdam Best](https://raw.githubusercontent.com/morpheusadam/v2ray-config/main/subs/bundles/best.txt) | `preserved` | `2026-11-10 04:20:39 МСК` | `612` | `0` | `0` | `0` | `0` | `612` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `612` | `vless: 612` | `-` |
| [Mehrtat VLESS](https://raw.githubusercontent.com/mehrtat/vless-collector/main/vless.txt) | `preserved` | `2026-11-10 04:20:39 МСК` | `25` | `0` | `0` | `0` | `0` | `25` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `25` | `vless: 25` | `-` |
| [Au1rxx Verified](https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/main/output/v2ray-base64.txt) | `preserved` | `2026-11-10 04:20:39 МСК` | `53` | `0` | `0` | `0` | `0` | `53` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `53` | `vless: 53` | `-` |
| [go4sharing/sub](https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml) | `preserved` | `2026-11-11 01:58:55 МСК` | `5` | `0` | `0` | `0` | `0` | `5` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `5` | `ss: 4, trojan: 1` | `-` |
| [Ruk1ng001/freeSub](https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml) | `preserved` | `2026-11-11 01:58:55 МСК` | `32` | `0` | `0` | `0` | `0` | `32` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `32` | `ss: 3, trojan: 24, vless: 5` | `-` |
| [awesome-vpn/awesome-vpn](https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/clash.yaml) | `preserved` | `2026-11-11 01:58:55 МСК` | `11` | `0` | `0` | `0` | `0` | `11` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `11` | `ss: 8, trojan: 3` | `-` |
| [Misaka-blog/chromego_merge](https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml) | `preserved` | `2026-11-10 04:20:39 МСК` | `49` | `0` | `0` | `0` | `0` | `49` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `49` | `ss: 34, trojan: 15` | `-` |
| [sunmiao4458/free-proxy-airport](https://raw.githubusercontent.com/sunmiao4458/free-proxy-airport/main/output/clash.yaml) | `preserved` | `2026-11-11 01:58:55 МСК` | `11` | `0` | `0` | `0` | `0` | `11` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `11` | `ss: 6, vless: 5` | `-` |
| [ermaozi/get_subscribe](https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml) | `preserved` | `2026-11-11 01:58:55 МСК` | `50` | `0` | `0` | `0` | `0` | `50` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `50` | `ss: 7, trojan: 9, vless: 34` | `-` |
| [peasoft/NoMoreWalls](https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml) | `preserved` | `2026-11-11 01:58:55 МСК` | `35` | `0` | `0` | `0` | `0` | `35` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `35` | `ss: 1, trojan: 15, vless: 19` | `-` |
| [F0rc3Run](https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/Best-Results/clash.yaml) | `preserved` | `2026-11-11 01:58:55 МСК` | `50` | `0` | `0` | `0` | `0` | `50` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `50` | `ss: 50` | `-` |
| [ProxyQueen](https://raw.githubusercontent.com/lyqnihao/proxy/main/proxyqueen/output.yaml) | `preserved` | `2026-11-11 01:58:55 МСК` | `25` | `0` | `0` | `0` | `0` | `25` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `25` | `vless: 25` | `-` |
| [wuge0/free-nodes](https://raw.githubusercontent.com/wuge0/free-nodes/main/output/github.yaml) | `ok` | `2026-11-12 09:55:34 МСК` | `60` | `2` | `1` | `1` | `0` | `53` | `6` | `1` | `0` | `12` | `2` | `0` | `21` | `39` | `ss: 25, trojan: 14` | `duplicate:experimental: 12, invalid:network: 1, overlap:lan_global: 2, unsupported:vmess: 6` |
| [sakazxc1400/free-vpn-sub](https://raw.githubusercontent.com/sakazxc1400-creator/free-vpn-sub/data/output/clash.yaml) | `ok` | `2026-11-12 09:55:34 МСК` | `200` | `3` | `2` | `1` | `0` | `159` | `41` | `0` | `6` | `41` | `47` | `0` | `135` | `65` | `ss: 39, trojan: 13, vless: 13` | `duplicate:experimental: 41, filtered:ru: 6, overlap:lan_global: 47, unsupported:hysteria2: 22, unsupported:vmess: 19` |
| [learnLi/free-nodes](https://raw.githubusercontent.com/learnLi/free-nodes/output/list.meta.cn.yml) | `ok` | `2026-11-12 09:55:34 МСК` | `294` | `7` | `4` | `3` | `0` | `205` | `80` | `9` | `4` | `49` | `36` | `0` | `178` | `116` | `ss: 12, trojan: 58, vless: 46` | `duplicate:experimental: 49, filtered:ru: 4, invalid:encryption: 2, invalid:unsupported_parameter:x-toolall-mihomo: 1, invalid:unsupported_parameter:xudp: 6, overlap:lan_global: 36, unsupported:anytls: 3, unsupported:hysteria2: 2, unsupported:vmess: 75` |
| [bily1258-design/beimi](https://raw.githubusercontent.com/bily1258-design/beimi/main/output/clash.yaml) | `ok` | `2026-11-12 09:55:34 МСК` | `816` | `5` | `5` | `0` | `1` | `699` | `74` | `43` | `17` | `59` | `117` | `0` | `310` | `506` | `ss: 33, trojan: 94, vless: 379` | `duplicate:experimental: 59, filtered:non_public: 15, filtered:ru: 2, invalid:network: 41, invalid:uuid: 2, overlap:lan_global: 117, unsupported:hysteria2: 38, unsupported:vmess: 36` |
| [Delta-Kronecker/V2ray-Config](https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/batches/clash/batch_001.yaml) | `ok` | `2026-11-12 09:55:34 МСК` | `500` | `4` | `2` | `2` | `0` | `478` | `22` | `0` | `8` | `126` | `86` | `0` | `242` | `258` | `ss: 60, trojan: 178, vless: 20` | `duplicate:experimental: 126, filtered:non_public: 1, filtered:ru: 7, overlap:lan_global: 86, unsupported:vmess: 22` |
| [hezhanleiok/freesub](https://raw.githubusercontent.com/hezhanleiok/freesub/main/output/clash.yaml) | `ok` | `2026-11-12 09:55:34 МСК` | `594` | `1` | `1` | `0` | `1` | `508` | `86` | `0` | `40` | `96` | `111` | `0` | `333` | `261` | `ss: 103, trojan: 38, vless: 120` | `duplicate:experimental: 96, filtered:non_public: 34, filtered:ru: 6, overlap:lan_global: 111, unsupported:hysteria2: 52, unsupported:vmess: 34` |
<!-- LAN-EXPERIMENTAL:END -->

<!-- LAN-SOURCE-STATS:START -->
## Новые LAN-источники

Эталонные `2002` записей из `origin/main` и ранее добавленные `157` записей (всего `2159`) сохранены без изменения имён, параметров и порядка. Добавлено `3111` новых конфигураций; исключено `13480` новых дублей. Итого `5270` записей и `4381` уникальных `server + port + UUID` (в старом пуле: `1270`). Статус «проверено» присваивается только после успешного HTTPS через VLESS.

Полные URL, время обновления, ошибки загрузки, причины отбраковки, транспорты и результаты стадий HTTPS сохранены в [`lan-source-stats.json`](lan-source-stats.json).

Политика дальнейшего обновления: фиксированный префикс из 2159 записей не накапливается заново; при каждом запуске пересобирается только текущий суффикс из доступных источников. Удаление или замена узлов фиксированного префикса требует отдельной проверяемой миграции.

| Источник | Получено | VLESS | Валидных | Уникальных | Дубли | Добавлено | HTTPS | Статус |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [MahanKenway configs/vless.txt](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) | `163` | `163` | `148` | `87` | `61` | `85` | `0/3` | не проверено |
| [Epodonios Splitted-By-Protocol/vless.txt](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `0` | `0` | `0` | `0` | `0` | `0` | `0/0` | не проверено |
| [barry-far V2ray-config vless.txt](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) | `6575` | `6575` | `6147` | `2088` | `4059` | `1789` | `0/3` | не проверено |
| [SoliSpirit Protocols/vless.txt](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) | `5160` | `5160` | `4593` | `320` | `4273` | `266` | `0/3` | не проверено |
| [liMilCo v2r pro/vless.txt](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) | `3668` | `3668` | `3333` | `547` | `2786` | `441` | `0/3` | не проверено |
| [V2RayRoot Config/vless.txt](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) | `263` | `263` | `258` | `15` | `243` | `15` | `0/3` | не проверено |
| [0xRadikal FAST](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/fast/configs.txt) | `1116` | `538` | `533` | `237` | `296` | `225` | `2/3` | проверено |
| [v2go Live-tested VLESS](https://raw.githubusercontent.com/Danialsamadi/v2go/main/Splitted-By-Protocol/vless.txt) | `176` | `176` | `166` | `48` | `118` | `44` | `0/3` | не проверено |
| [PulseConfigs FAST](https://raw.githubusercontent.com/drmikecrypto/PulseConfigs/main/fast/configs.txt) | `130` | `10` | `10` | `0` | `10` | `0` | `0/0` | не проверено |
| [free-xray-gcp VLESS](https://raw.githubusercontent.com/noahclanman/free-xray-gcp/main/output/protocols/vless.txt) | `555` | `555` | `550` | `100` | `450` | `80` | `2/3` | проверено |
| [multi-proxy-config-fetcher tested](https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/main/configs/proxy_configs_tested.txt) | `181` | `65` | `65` | `4` | `61` | `1` | `1/1` | проверено |
| [patterniha Free-Configs](https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt) | `57` | `57` | `51` | `8` | `43` | `3` | `1/3` | проверено |
| [CaptchaQ working_all](https://raw.githubusercontent.com/CaptchaQ/vless-servers/main/working_all.txt) | `84` | `84` | `84` | `21` | `63` | `17` | `0/3` | не проверено |
| [NodesRadar v2ray](https://radarhub.top/v2ray.txt) | `500` | `0` | `0` | `0` | `0` | `0` | `0/0` | не проверено |
| [mrdevmohamed VLESS](https://raw.githubusercontent.com/mrdevmohamed/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `1098` | `1098` | `1095` | `117` | `978` | `91` | `1/3` | проверено |
| [Baarcuda top100 VLESS](https://raw.githubusercontent.com/Baarcuda/vpn-configs/master/top100-vless.txt) | `100` | `100` | `98` | `59` | `39` | `54` | `0/3` | не проверено |
<!-- LAN-SOURCE-STATS:END -->

## LAN Global и Fast Check

Обе подписки содержат одинаковые серверы в одинаковом порядке и используют один URL проверки: `https://cp.cloudflare.com/generate_204`.
Сейчас специализированный пул меньше лимита 5000, поэтому LAN 5K также содержит все серверы LAN Global.
Используются только отдельные пулы для обычного проводного подключения и режима чёрных списков. Whitelist/CIDR-источники pale-signal в эти LAN-подписки не входят:

- [MahanKenway configs/vless.txt](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt)
- [Epodonios Splitted-By-Protocol/vless.txt](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt)
- [barry-far V2ray-config vless.txt](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt)
- [SoliSpirit Protocols/vless.txt](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt)
- [liMilCo v2r pro/vless.txt](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt)
- [V2RayRoot Config/vless.txt](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt)
- [WireVeil VLESS (wired blacklist mode)](https://raw.githubusercontent.com/markKikhtenko/WireVeil/main/vless.txt)
- [WLUnlocker Blacklist All](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/blacklist_all.txt)
- [Apex Parser BlackList (Wi-Fi)](https://raw.githubusercontent.com/Diversan313/apex-parser/main/subs/main/alive_plain_bl.txt)
- [FLAT447 BlackList Full](https://raw.githubusercontent.com/FLAT447/v2ray-lists/main/BLACK_FULL.txt)
- [igareck Black VLESS Russia](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt)
- [Moonishe checked blacklist](https://raw.githubusercontent.com/Moonishe/vpnparser/main/output/subscription-blacklist.txt)
- [0xRadikal FAST](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/fast/configs.txt)
- [v2go Live-tested VLESS](https://raw.githubusercontent.com/Danialsamadi/v2go/main/Splitted-By-Protocol/vless.txt)
- [PulseConfigs FAST](https://raw.githubusercontent.com/drmikecrypto/PulseConfigs/main/fast/configs.txt)
- [free-xray-gcp VLESS](https://raw.githubusercontent.com/noahclanman/free-xray-gcp/main/output/protocols/vless.txt)
- [multi-proxy-config-fetcher tested](https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/main/configs/proxy_configs_tested.txt)
- [patterniha Free-Configs](https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt)
- [CaptchaQ working_all](https://raw.githubusercontent.com/CaptchaQ/vless-servers/main/working_all.txt)
- [NodesRadar v2ray](https://radarhub.top/v2ray.txt)
- [mrdevmohamed VLESS](https://raw.githubusercontent.com/mrdevmohamed/v2ray-configs/main/Splitted-By-Protocol/vless.txt)
- [Baarcuda top100 VLESS](https://raw.githubusercontent.com/Baarcuda/vpn-configs/master/top100-vless.txt)

| Параметр `AUTO` | LAN Global | LAN Global Fast Check |
|-----------------|------------|-----------------------|
| `interval` | `900` | `600` |
| `tolerance` | `100` | `50` |
| `timeout` | значение Mihomo по умолчанию | `3000` мс |
| `max-failed-times` | значение Mihomo по умолчанию | `3` |
| `lazy` | `true` | `true` |

`url-test` измеряет доступность узла и задержку ответа на тестовый URL. Он не измеряет реальную скорость передачи данных до Instagram, ChatGPT или других приложений.

## Подключение

### Mihomo/OpenClash

1. Скопируйте нужную ссылку из таблицы.
2. Добавьте её в `Config Subscription` OpenClash без конвертации.
3. Используйте `PROXY` → `AUTO` для автовыбора или `MANUAL` для ручного выбора.

Для `BS Safe` требуется Mihomo/Meta Core v1.19.24 или новее.

### Happ/Happ Plus

Добавьте URL `subscription-mobile.txt` как обычную подписку. Файл содержит только VLESS-ссылки без YAML, групп и правил; выбор сервера и проверка задержки выполняются в приложении.

## Маршрутизация

[OpenClash Overwrite Module](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing.conf) направляет заблокированные ресурсы в `PROXY`, остальной трафик оставляет на `DIRECT` и не меняет DNS.

## Обновление

Сборка запускается ежедневно в 09:00 и 21:00 МСК. Некорректные конфигурации не публикуются. Наличие сервера в списке не гарантирует его доступность у конкретного провайдера.
