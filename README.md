# pale-signal

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-8126-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

Автоматически обновляемые VLESS-подписки для Mihomo, OpenClash и Happ/Happ Plus.

**Последнее обновление:** `2026-11-11 01:55:19 МСК`

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
| Всего серверов | `8126` |
| Россия | `1561` |
| Global | `6565` |
| Global 5K | `1807` |
| LAN 5K | `5000` |
| LAN Global | `5143` |
| LAN Global Fast Check | `5143` |
| LAN Experimental | `969` |
| LAN Experimental AUTO | `969` |
| Исключено пересечений Experimental с LAN Global | `21` |
| BS Safe MANUAL | `1379` |
| BS Safe AUTO | `50` |
| Happ Mobile | `496` |

<!-- LAN-EXPERIMENTAL:START -->
## LAN Experimental

Изолированная тестовая подписка: `969` серверов, все входят в `AUTO`. Протоколы: `ss: 116, trojan: 70, vless: 783`. Дубли и совпадения с `LAN Global` удаляются до публикации. Опубликованный до этого пул сохранён без изменений и используется как базовый; при временной недоступности нового источника используется его последний опубликованный пул. Старые три источника остаются обязательными.

Шесть GitHub YAML-источников `wuge0/free-nodes`, `sakazxc1400/free-vpn-sub`, `learnLi/free-nodes`, `bily1258-design/beimi`, `Delta-Kronecker/V2ray-Config` и `hezhanleiok/freesub` подключены только к LAN Experimental. Для них действует закрытый allowlist из отчёта `WireVeil-Mihomo-Report-20261111-141445.zip`: сборка допускает только точные конфигурации со статусом Good или Partial и никогда автоматически не импортирует остальные узлы источников. В отчёте 60 уникальных Good/Partial, из них 4 VMess/Hysteria2 исключены политикой протоколов, поэтому allowlist содержит `56` разрешённых кандидатов. В текущих YAML найдено `40` из них (`29` Good, `11` Partial); кроме того, найдены и отклонены `2` из четырёх запрещённых протоколов.

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
| [wuge0/free-nodes](https://raw.githubusercontent.com/wuge0/free-nodes/main/output/github.yaml) | `ok` | `2026-11-11 15:35:57 МСК` | `60` | `2` | `1` | `1` | `0` | `2` | `0` | `0` | `0` | `1` | `0` | `0` | `59` | `1` | `ss: 1` | `duplicate:experimental: 1, wireveil:not_allowlisted: 58` |
| [sakazxc1400/free-vpn-sub](https://raw.githubusercontent.com/sakazxc1400-creator/free-vpn-sub/data/output/clash.yaml) | `ok` | `2026-11-11 15:35:57 МСК` | `200` | `10` | `7` | `3` | `0` | `10` | `0` | `0` | `0` | `0` | `7` | `0` | `197` | `3` | `ss: 2, trojan: 1` | `overlap:lan_global: 7, wireveil:not_allowlisted: 190` |
| [learnLi/free-nodes](https://raw.githubusercontent.com/learnLi/free-nodes/output/list.meta.cn.yml) | `ok` | `2026-11-11 15:35:57 МСК` | `332` | `20` | `15` | `5` | `0` | `16` | `0` | `4` | `0` | `2` | `8` | `0` | `326` | `6` | `trojan: 1, vless: 5` | `duplicate:experimental: 2, invalid:unsupported_parameter:xudp: 4, overlap:lan_global: 8, wireveil:not_allowlisted: 312` |
| [bily1258-design/beimi](https://raw.githubusercontent.com/bily1258-design/beimi/main/output/clash.yaml) | `ok` | `2026-11-11 15:35:57 МСК` | `806` | `5` | `5` | `0` | `1` | `4` | `1` | `0` | `0` | `1` | `3` | `0` | `806` | `0` | `-` | `duplicate:experimental: 1, overlap:lan_global: 3, unsupported:hysteria2: 1, wireveil:not_allowlisted: 801` |
| [Delta-Kronecker/V2ray-Config](https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/batches/clash/batch_001.yaml) | `ok` | `2026-11-11 15:35:57 МСК` | `500` | `4` | `2` | `2` | `0` | `4` | `0` | `0` | `0` | `0` | `3` | `0` | `499` | `1` | `trojan: 1` | `overlap:lan_global: 3, wireveil:not_allowlisted: 496` |
| [hezhanleiok/freesub](https://raw.githubusercontent.com/hezhanleiok/freesub/main/output/clash.yaml) | `ok` | `2026-11-11 15:35:57 МСК` | `594` | `1` | `1` | `0` | `1` | `0` | `1` | `0` | `0` | `0` | `0` | `0` | `594` | `0` | `-` | `unsupported:hysteria2: 1, wireveil:not_allowlisted: 593` |
<!-- LAN-EXPERIMENTAL:END -->

<!-- LAN-SOURCE-STATS:START -->
## Новые LAN-источники

Эталонные `2002` записей из `origin/main` и ранее добавленные `157` записей (всего `2159`) сохранены без изменения имён, параметров и порядка. Добавлено `2984` новых конфигураций; исключено `13332` новых дублей. Итого `5143` записей и `4254` уникальных `server + port + UUID` (в старом пуле: `1270`). Статус «проверено» присваивается только после успешного HTTPS через VLESS.

Полные URL, время обновления, ошибки загрузки, причины отбраковки, транспорты и результаты стадий HTTPS сохранены в [`lan-source-stats.json`](lan-source-stats.json).

Политика дальнейшего обновления: фиксированный префикс из 2159 записей не накапливается заново; при каждом запуске пересобирается только текущий суффикс из доступных источников. Удаление или замена узлов фиксированного префикса требует отдельной проверяемой миграции.

| Источник | Получено | VLESS | Валидных | Уникальных | Дубли | Добавлено | HTTPS | Статус |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [MahanKenway configs/vless.txt](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) | `149` | `149` | `136` | `84` | `52` | `80` | `0/3` | не проверено |
| [Epodonios Splitted-By-Protocol/vless.txt](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `0` | `0` | `0` | `0` | `0` | `0` | `0/0` | не проверено |
| [barry-far V2ray-config vless.txt](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) | `6526` | `6526` | `6077` | `2138` | `3939` | `1817` | `0/3` | не проверено |
| [SoliSpirit Protocols/vless.txt](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) | `5112` | `5112` | `4521` | `343` | `4178` | `284` | `0/3` | не проверено |
| [liMilCo v2r pro/vless.txt](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) | `3668` | `3668` | `3333` | `292` | `3041` | `221` | `0/3` | не проверено |
| [V2RayRoot Config/vless.txt](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) | `263` | `263` | `258` | `14` | `244` | `14` | `0/3` | не проверено |
| [0xRadikal FAST](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/fast/configs.txt) | `821` | `343` | `340` | `133` | `207` | `130` | `3/3` | проверено |
| [v2go Live-tested VLESS](https://raw.githubusercontent.com/Danialsamadi/v2go/main/Splitted-By-Protocol/vless.txt) | `229` | `229` | `216` | `104` | `112` | `101` | `0/3` | не проверено |
| [PulseConfigs FAST](https://raw.githubusercontent.com/drmikecrypto/PulseConfigs/main/fast/configs.txt) | `130` | `10` | `10` | `0` | `10` | `0` | `0/0` | не проверено |
| [free-xray-gcp VLESS](https://raw.githubusercontent.com/noahclanman/free-xray-gcp/main/output/protocols/vless.txt) | `528` | `528` | `521` | `135` | `386` | `119` | `2/3` | проверено |
| [multi-proxy-config-fetcher tested](https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/main/configs/proxy_configs_tested.txt) | `194` | `73` | `73` | `1` | `72` | `0` | `0/0` | не проверено |
| [patterniha Free-Configs](https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt) | `39` | `39` | `33` | `10` | `23` | `6` | `0/3` | не проверено |
| [CaptchaQ working_all](https://raw.githubusercontent.com/CaptchaQ/vless-servers/main/working_all.txt) | `84` | `84` | `84` | `21` | `63` | `17` | `0/3` | не проверено |
| [NodesRadar v2ray](https://radarhub.top/v2ray.txt) | `500` | `3` | `3` | `0` | `3` | `0` | `0/0` | не проверено |
| [mrdevmohamed VLESS](https://raw.githubusercontent.com/mrdevmohamed/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `1141` | `1141` | `1139` | `176` | `963` | `142` | `0/3` | не проверено |
| [Baarcuda top100 VLESS](https://raw.githubusercontent.com/Baarcuda/vpn-configs/master/top100-vless.txt) | `100` | `100` | `98` | `59` | `39` | `53` | `0/3` | не проверено |
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
