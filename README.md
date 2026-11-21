# pale-signal

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-8298-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

Автоматически обновляемые VLESS-подписки для Mihomo, OpenClash и Happ/Happ Plus.

**Последнее обновление:** `2026-11-20 17:59:02 МСК`

## Подписки

| Файл | Назначение |
|------|------------|
| [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) | Все серверы |
| [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) | Россия |
| [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) | Все non-RU серверы |
| [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) | Global, до 5000 серверов |
| [subscription-global-megafon-candidates.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-megafon-candidates.yaml) | Ограниченный список кандидатов, прошедших HTTPS через Mihomo вне сети МегаФона; требует роутерной проверки |
| [subscription-lan-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml) | Основная LAN-подписка для проводного интернета, до 5000 серверов; при меньшем пуле совпадает с LAN Global |
| [subscription-lan-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml) | Полный LAN-пул для проводного интернета без лимита |
| [subscription-lan-global-fast-check.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global-fast-check.yaml) | LAN Global Fast Check — те же серверы LAN Global, более активная автоматическая проверка |
| [subscription-lan-experimental.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-experimental.yaml) | Изолированная тестовая LAN-подписка |
| [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) | Тестовая Global |
| [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) | Reality-узлы для режима блокировок |
| [subscription-mobile.txt](https://markkikhtenko.github.io/pale-signal/subscription-mobile.txt) | Компактная мобильная Reality-подписка для Happ/Happ Plus |
| [subscription-zapret.yaml](https://markkikhtenko.github.io/pale-signal/subscription-zapret.yaml) | Изолированный VLESS/VMess/Shadowsocks-пул Zapret из страниц 1–25 |

`subscription-global.yaml`, `subscription-global-5k.yaml` и `subscription-bs-safe.yaml` используют `PulseProxy/30.txt` как приоритетный источник узлов для обхода SNI/CIDR белых списков. Из него импортируются только валидные VLESS-конфигурации; дубли удаляются общей сборкой.

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `8298` |
| Россия | `1846` |
| Global | `7390` |
| Global 5K | `2450` |
| LAN 5K | `5000` |
| LAN Global | `5379` |
| LAN Global Fast Check | `5379` |
| LAN Experimental | `2143` |
| LAN Experimental AUTO | `2143` |
| Исключено пересечений Experimental с LAN Global | `321` |
| BS Safe MANUAL | `1566` |
| BS Safe AUTO | `50` |
| Happ Mobile | `449` |
| Zapret | `2798` |

<!-- GLOBAL-SOURCE-STATS:START -->
## Global: источники обхода белых списков

Три новых whitelist/SNI-источника добавляются только в production Global-контур. Дедупликация выполняется по фактическим параметрам VLESS, TLS/REALITY и транспорта; имя узла в ключ не входит. PulseProxy сохраняет первый приоритет, относительный порядок всех прежних источников не изменён.

HTTPS в этой таблице выполняется через Mihomo в среде GitHub Actions/локального прогона и не является проверкой в сети МегаФона. До запуска роутерного теста колонка МегаФон всегда содержит `NOT TESTED`.

| Источник | HTTP | Обновлён | Получено | Валидных | Уникальных в источнике | Новых Global | Дубли/невалидные | DNS | HTTPS | МегаФон |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| [hussaroff lte-universal-checked whitelist.txt](https://raw.githubusercontent.com/hussaroff/lte-universal-checked/main/whitelist.txt) | `200` | `2026-11-21 05:54 МСК` | `126` | `126` | `79` | `1` | `47` | `5/5` | `3/5` | `NOT TESTED` |
| [coloramamoe whitelist-vless.txt](https://raw.githubusercontent.com/coloramamoe/vless-parser/main/githubmirror/whitelist-vless.txt) | `200` | `2026-11-21 06:57 МСК` | `697` | `697` | `652` | `0` | `45` | `5/5` | `0/5` | `NOT TESTED` |
| [coloramamoe ru-sni-best-vless.txt](https://raw.githubusercontent.com/coloramamoe/vless-parser/main/githubmirror/ru-sni-best-vless.txt) | `200` | `2026-11-21 06:57 МСК` | `120` | `120` | `120` | `0` | `0` | `5/5` | `0/5` | `NOT TESTED` |

### Недоступные старые источники

Текущая диагностика получила HTTP 404. Источники не удалены автоматически; для каждого предлагается проверить перенос или переименование и только затем исключать.

| Источник | HTTP | Серия 404 | Рекомендация |
|---|---:|---:|---|
| [EtoNeYaProject GitHub whitelist](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |
| [FLEXIY0 matryoshka-vpn russia_whitelist.txt](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |
| [Epodonios Splitted-By-Protocol/vless.txt](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |
| [Epodonios Sub26.txt](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |
| [MahsaNetConfigTopic xray_final.txt](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |
| [AvenCores 26_urls.json](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |
| [AvenCores githubmirror/26.txt](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |
| [PrinceVSFX Adapt-Configs White_list.txt](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) | `404` | `1` | HTTP 404: проверить перенос/переименование и предложить исключение; автоматически не удалён |

### Кандидаты для проверки на МегаФоне

В этот список попадают только узлы, уже выполнившие реальный HTTPS-запрос через Mihomo. Это ещё не подтверждение работы в мобильной сети.

| Имя | Источник | мс | HTTPS | МегаФон |
|---|---|---:|---|---|
| 荷兰_112106571 t.me/rjsxrd | hussaroff lte-universal-checked whitelist.txt | `1555` | PASS | NOT TESTED |
| [OpenRay] 🇸🇪SE-1 | hussaroff lte-universal-checked whitelist.txt | `646` | PASS | NOT TESTED |
| [OpenRay] 🇦🇹AT-5 | hussaroff lte-universal-checked whitelist.txt | `812` | PASS | NOT TESTED |

Ограниченный тест на роутере (по умолчанию не более 12 узлов, 2 параллельных процесса, таймаут 12 секунд):

```sh
python3 scripts/check_megafon.py --mihomo /usr/bin/mihomo --confirm-megafon --limit 12 --workers 2 --timeout 12
```

Скрипт классифицирует DNS, TCP, TLS, HTTPS и таймауты и создаёт отдельную проверенную подписку только из фактических `PASS` в подтверждённой сети МегаФона.
<!-- GLOBAL-SOURCE-STATS:END -->

<!-- LAN-EXPERIMENTAL:START -->
## LAN Experimental

Изолированная тестовая подписка: `2143` серверов, все входят в `AUTO`. Протоколы: `ss: 410, trojan: 434, vless: 1299`. Дубли и совпадения с `LAN Global` удаляются до публикации. Опубликованный до этого пул сохранён без изменений и используется как базовый; при временной недоступности нового источника используется его последний опубликованный пул. Старые три источника остаются обязательными.

Шесть GitHub YAML-источников `wuge0/free-nodes`, `sakazxc1400/free-vpn-sub`, `learnLi/free-nodes`, `bily1258-design/beimi`, `Delta-Kronecker/V2ray-Config` и `hezhanleiok/freesub` подключены целиком и только к LAN Experimental. Отчёт `WireVeil-Mihomo-Report-20261111-141445.zip` используется как историческая проверка актуальности самих источников и для статистики точных совпадений, а не как поузловой allowlist: при каждом обновлении импортируются все текущие валидные VLESS, Shadowsocks и Trojan. VMess, Hysteria2, невалидные записи, дубли и пересечения с LAN Global по-прежнему исключаются. В отчёте 60 уникальных Good/Partial, из них 4 VMess/Hysteria2 не поддерживаются политикой протоколов; в текущих YAML найдено `1` из `56` поддерживаемых проверенных записей (`1` Good, `0` Partial), а также `2` совпадений запрещённых протоколов.

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
| [wuge0/free-nodes](https://raw.githubusercontent.com/wuge0/free-nodes/main/output/github.yaml) | `fallback` | `2026-11-12 17:43:44 МСК` | `0` | `2` | `1` | `1` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `39` | `ss: 25, trojan: 14` | `source:unavailable: 1` |
| [sakazxc1400/free-vpn-sub](https://raw.githubusercontent.com/sakazxc1400-creator/free-vpn-sub/data/output/clash.yaml) | `ok` | `2026-11-20 18:02:16 МСК` | `200` | `0` | `0` | `0` | `0` | `141` | `59` | `0` | `6` | `56` | `27` | `0` | `148` | `52` | `ss: 45, trojan: 4, vless: 3` | `duplicate:experimental: 56, filtered:ru: 6, overlap:lan_global: 27, unsupported:hysteria2: 34, unsupported:vmess: 25` |
| [learnLi/free-nodes](https://raw.githubusercontent.com/learnLi/free-nodes/output/list.meta.cn.yml) | `ok` | `2026-11-20 18:02:16 МСК` | `247` | `0` | `0` | `0` | `0` | `150` | `91` | `6` | `1` | `32` | `26` | `0` | `156` | `91` | `ss: 14, trojan: 51, vless: 26` | `duplicate:experimental: 32, filtered:ru: 1, invalid:encryption: 2, invalid:unsupported_parameter:xudp: 4, overlap:lan_global: 26, unsupported:anytls: 1, unsupported:vmess: 90` |
| [bily1258-design/beimi](https://raw.githubusercontent.com/bily1258-design/beimi/main/output/clash.yaml) | `ok` | `2026-11-20 18:02:16 МСК` | `659` | `2` | `2` | `0` | `1` | `570` | `64` | `25` | `16` | `20` | `98` | `0` | `223` | `436` | `ss: 22, trojan: 57, vless: 357` | `duplicate:experimental: 20, filtered:non_public: 14, filtered:ru: 1, filtered:unknown_country: 1, invalid:network: 23, invalid:uuid: 2, overlap:lan_global: 98, unsupported:hysteria2: 28, unsupported:vmess: 36` |
| [Delta-Kronecker/V2ray-Config](https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/batches/clash/batch_001.yaml) | `ok` | `2026-11-20 18:02:16 МСК` | `500` | `0` | `0` | `0` | `0` | `473` | `26` | `1` | `10` | `89` | `70` | `0` | `196` | `304` | `ss: 88, trojan: 203, vless: 13` | `duplicate:experimental: 89, filtered:ru: 10, invalid:unsupported_parameter:httpupgrade-opts: 1, overlap:lan_global: 70, unsupported:vmess: 26` |
| [hezhanleiok/freesub](https://raw.githubusercontent.com/hezhanleiok/freesub/main/output/clash.yaml) | `ok` | `2026-11-20 18:02:16 МСК` | `594` | `1` | `1` | `0` | `1` | `508` | `86` | `0` | `42` | `103` | `100` | `0` | `331` | `263` | `ss: 103, trojan: 38, vless: 122` | `duplicate:experimental: 103, filtered:non_public: 36, filtered:ru: 6, overlap:lan_global: 100, unsupported:hysteria2: 52, unsupported:vmess: 34` |
<!-- LAN-EXPERIMENTAL:END -->

<!-- LAN-SOURCE-STATS:START -->
## Новые LAN-источники

Эталонные `2002` записей из `origin/main` и ранее добавленные `157` записей (всего `2159`) сохранены без изменения имён, параметров и порядка. Добавлено `3220` новых конфигураций; исключено `12300` новых дублей. Итого `5379` записей и `4490` уникальных `server + port + UUID` (в старом пуле: `1270`). Статус «проверено» присваивается только после успешного HTTPS через VLESS.

Полные URL, время обновления, ошибки загрузки, причины отбраковки, транспорты и результаты стадий HTTPS сохранены в [`lan-source-stats.json`](lan-source-stats.json).

Политика дальнейшего обновления: фиксированный префикс из 2159 записей не накапливается заново; при каждом запуске пересобирается только текущий суффикс из доступных источников. Удаление или замена узлов фиксированного префикса требует отдельной проверяемой миграции.

| Источник | Получено | VLESS | Валидных | Уникальных | Дубли | Добавлено | HTTPS | Статус |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [MahanKenway configs/vless.txt](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) | `112` | `112` | `103` | `72` | `31` | `72` | `0/3` | не проверено |
| [Epodonios Splitted-By-Protocol/vless.txt](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `0` | `0` | `0` | `0` | `0` | `0` | `0/0` | не проверено |
| [barry-far V2ray-config vless.txt](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) | `5950` | `5950` | `5522` | `2241` | `3281` | `1886` | `0/3` | не проверено |
| [SoliSpirit Protocols/vless.txt](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) | `5140` | `5140` | `4589` | `342` | `4247` | `268` | `0/3` | не проверено |
| [liMilCo v2r pro/vless.txt](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) | `3818` | `3818` | `3473` | `637` | `2836` | `476` | `1/3` | проверено |
| [V2RayRoot Config/vless.txt](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) | `263` | `263` | `258` | `15` | `243` | `15` | `0/3` | не проверено |
| [0xRadikal FAST](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/fast/configs.txt) | `967` | `343` | `337` | `145` | `192` | `128` | `3/3` | проверено |
| [v2go Live-tested VLESS](https://raw.githubusercontent.com/Danialsamadi/v2go/main/Splitted-By-Protocol/vless.txt) | `136` | `136` | `130` | `46` | `84` | `39` | `2/3` | проверено |
| [PulseConfigs FAST](https://raw.githubusercontent.com/drmikecrypto/PulseConfigs/main/fast/configs.txt) | `130` | `10` | `10` | `0` | `10` | `0` | `0/0` | не проверено |
| [free-xray-gcp VLESS](https://raw.githubusercontent.com/noahclanman/free-xray-gcp/main/output/protocols/vless.txt) | `514` | `514` | `507` | `130` | `377` | `109` | `0/3` | не проверено |
| [multi-proxy-config-fetcher tested](https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/main/configs/proxy_configs_tested.txt) | `226` | `62` | `62` | `2` | `60` | `0` | `0/0` | не проверено |
| [patterniha Free-Configs](https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt) | `33` | `33` | `30` | `17` | `13` | `9` | `1/3` | проверено |
| [CaptchaQ working_all](https://raw.githubusercontent.com/CaptchaQ/vless-servers/main/working_all.txt) | `84` | `84` | `84` | `21` | `63` | `17` | `0/3` | не проверено |
| [NodesRadar v2ray](https://radarhub.top/v2ray.txt) | `500` | `0` | `0` | `0` | `0` | `0` | `0/0` | не проверено |
| [mrdevmohamed VLESS](https://raw.githubusercontent.com/mrdevmohamed/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `1016` | `1016` | `992` | `142` | `850` | `123` | `2/3` | проверено |
| [Baarcuda top100 VLESS](https://raw.githubusercontent.com/Baarcuda/vpn-configs/master/top100-vless.txt) | `100` | `100` | `99` | `86` | `13` | `78` | `0/3` | не проверено |
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

### Zapret

`subscription-zapret.yaml` пересобирается только из 25 страниц `hiztin/VLESS-PO-GRIBI`. Только для этого источника разрешены VLESS, VMess и Shadowsocks; некорректные записи отбрасываются, точные дубли конфигураций удаляются. Все страницы обязательны, а резкое сокращение пула блокирует публикацию. Это исключение не меняет VLESS-only правила остальных production-подписок. Проверка синтаксиса не гарантирует сетевую доступность узлов. Подробности каждой сборки сохраняются в [`zapret-stats.json`](https://markkikhtenko.github.io/pale-signal/zapret-stats.json).

## Маршрутизация

Доступны два OpenClash Override Module с общими обновляемыми списками маршрутизации:

| Подписка | Override Module |
|----------|-----------------|
| Бесплатные подписки Pale Signal | [`blacklist-routing.conf`](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing.conf) |
| Платная подписка VPnBot | [`blacklist-routing-vpnbot.conf`](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing-vpnbot.conf) |

В OpenClash откройте **Overwrite Settings → Overwrite Modules**, добавьте URL одного модуля, включите его для нужного профиля и примените профиль в режиме `Rule`. Для VPnBot основная целевая группа — `🌐 VPnBot`; обычный трафик оба модуля оставляют на `DIRECT`, DNS не меняют.
## Обновление

Сборка запускается ежедневно в 09:00 и 21:00 МСК. Некорректные конфигурации не публикуются. Наличие сервера в списке не гарантирует его доступность у конкретного провайдера.
