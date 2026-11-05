# pale-signal

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-8136-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

Автоматически обновляемые VLESS-подписки для Mihomo, OpenClash и Happ/Happ Plus.

**Последнее обновление:** `2026-11-05 17:02:18 МСК`

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
| Всего серверов | `8136` |
| Россия | `1836` |
| Global | `6300` |
| Global 5K | `1699` |
| LAN 5K | `5000` |
| LAN Global | `5126` |
| LAN Global Fast Check | `5126` |
| LAN Experimental | `1180` |
| LAN Experimental AUTO | `1180` |
| Исключено пересечений Experimental с LAN Global | `92` |
| BS Safe MANUAL | `1512` |
| BS Safe AUTO | `50` |
| Happ Mobile | `488` |

<!-- LAN-EXPERIMENTAL:START -->
## LAN Experimental

Изолированная тестовая подписка: `1180` серверов, все входят в `AUTO`. Протоколы: `ss: 103, trojan: 45, vless: 1032`. Дубли и совпадения с `LAN Global` удаляются до публикации. Новые YAML-источники ограничены 50 узлами каждый и выбираются детерминированно; при их временной недоступности используется последний опубликованный пул этого источника. Старые три источника остаются обязательными.

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

Результаты WireVeil — исторический ориентир на момент локальной проверки, а не гарантия актуальной работоспособности и не live-проверка при сборке.

| Источник | Статус | Последнее успешное обновление | Загружено | Разобрано | Неподдерживаемых | Невалидных | Отфильтровано | Дубли | LAN Global | Лимит | Отброшено | Добавлено | Протоколы | Причины исключения |
|----------|--------|------------------------------|-----------:|----------:|------------------:|-----------:|---------------:|-------:|-----------:|------:|----------:|---------:|-----------|--------------------|
| [MorpheusAdam Best](https://raw.githubusercontent.com/morpheusadam/v2ray-config/main/subs/bundles/best.txt) | `fallback` | `2026-10-20 21:16 МСК` | `436` | `414` | `0` | `22` | `0` | `0` | `0` | `0` | `22` | `942` | `vless: 942` | `invalid:vless: 22, source:legacy_pool_fallback: 1` |
| [Mehrtat VLESS](https://raw.githubusercontent.com/mehrtat/vless-collector/main/vless.txt) | `fallback` | `2026-10-21 09:47 МСК` | `51` | `51` | `0` | `0` | `0` | `0` | `0` | `0` | `0` | `9` | `vless: 9` | `source:legacy_pool_fallback: 1, source:truncated: 1` |
| [Au1rxx Verified](https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/main/output/v2ray-base64.txt) | `fallback` | `2026-10-21 13:01 МСК` | `1002` | `970` | `0` | `32` | `0` | `0` | `0` | `0` | `32` | `0` | `-` | `invalid:vless: 32, source:legacy_pool_fallback: 1` |
| [go4sharing/sub](https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml) | `ok` | `2026-11-05 17:06:06 МСК` | `13` | `9` | `4` | `0` | `0` | `0` | `0` | `0` | `4` | `9` | `ss: 7, trojan: 2` | `unsupported:vmess: 4` |
| [Ruk1ng001/freeSub](https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml) | `ok` | `2026-11-05 17:06:06 МСК` | `500` | `34` | `448` | `18` | `0` | `3` | `2` | `0` | `471` | `29` | `ss: 1, trojan: 23, vless: 5` | `duplicate:experimental: 3, invalid:unsupported_parameter:alterId: 3, invalid:unsupported_parameter:xudp: 15, overlap:lan_global: 2, unsupported:anytls: 3, unsupported:http: 408, unsupported:hysteria2: 2, unsupported:mieru: 1, unsupported:socks5: 28, unsupported:ssr: 1, unsupported:vmess: 5` |
| [awesome-vpn/awesome-vpn](https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/clash.yaml) | `ok` | `2026-11-05 17:06:06 МСК` | `26` | `26` | `0` | `0` | `0` | `2` | `12` | `0` | `14` | `12` | `ss: 10, trojan: 2` | `duplicate:experimental: 2, overlap:lan_global: 12` |
| [Misaka-blog/chromego_merge](https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml) | `ok` | `2026-11-05 17:06:06 МСК` | `188` | `162` | `26` | `0` | `4` | `95` | `0` | `13` | `138` | `50` | `ss: 35, trojan: 15` | `duplicate:experimental: 95, filtered:ru: 4, limited:per_source: 13, unsupported:vmess: 26` |
| [sunmiao4458/free-proxy-airport](https://raw.githubusercontent.com/sunmiao4458/free-proxy-airport/main/output/clash.yaml) | `ok` | `2026-11-05 17:06:06 МСК` | `24` | `15` | `3` | `6` | `0` | `5` | `6` | `0` | `20` | `4` | `vless: 4` | `duplicate:experimental: 5, invalid:unsupported_parameter:skip-cert-verify: 6, overlap:lan_global: 6, unsupported:hysteria: 1, unsupported:hysteria2: 1, unsupported:vmess: 1` |
| [ermaozi/get_subscribe](https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml) | `ok` | `2026-11-05 17:06:06 МСК` | `370` | `203` | `158` | `9` | `7` | `91` | `60` | `0` | `325` | `45` | `trojan: 1, vless: 44` | `duplicate:experimental: 91, filtered:non_public: 1, filtered:ru: 6, invalid:encryption: 1, invalid:unsupported_parameter:skip-cert-verify: 8, overlap:lan_global: 60, unsupported:anytls: 2, unsupported:http: 68, unsupported:hysteria: 12, unsupported:hysteria2: 58, unsupported:socks5: 2, unsupported:ssr: 1, unsupported:vmess: 15` |
| [peasoft/NoMoreWalls](https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml) | `ok` | `2026-11-05 17:06:06 МСК` | `340` | `194` | `145` | `1` | `7` | `187` | `0` | `0` | `340` | `0` | `-` | `duplicate:experimental: 187, filtered:non_public: 1, filtered:ru: 6, invalid:encryption: 1, unsupported:anytls: 1, unsupported:http: 68, unsupported:hysteria: 7, unsupported:hysteria2: 54, unsupported:socks5: 2, unsupported:vmess: 13` |
| [F0rc3Run](https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/Best-Results/clash.yaml) | `ok` | `2026-11-05 17:06:06 МСК` | `235` | `212` | `23` | `0` | `1` | `42` | `4` | `115` | `185` | `50` | `ss: 50` | `duplicate:experimental: 42, filtered:ru: 1, limited:per_source: 115, overlap:lan_global: 4, unsupported:vmess: 23` |
| [ProxyQueen](https://raw.githubusercontent.com/lyqnihao/proxy/main/proxyqueen/output.yaml) | `ok` | `2026-11-05 17:06:06 МСК` | `115` | `75` | `19` | `21` | `14` | `23` | `8` | `0` | `85` | `30` | `trojan: 2, vless: 28` | `duplicate:experimental: 23, filtered:ru: 14, invalid:unsupported_parameter:skip-cert-verify: 21, overlap:lan_global: 8, unsupported:anytls: 13, unsupported:hysteria2: 1, unsupported:vmess: 5` |
<!-- LAN-EXPERIMENTAL:END -->

<!-- LAN-SOURCE-STATS:START -->
## Новые LAN-источники

Эталонные `2002` записей из `origin/main` и ранее добавленные `157` записей (всего `2159`) сохранены без изменения имён, параметров и порядка. Добавлено `2967` новых конфигураций; исключено `12637` новых дублей. Итого `5126` записей и `4237` уникальных `server + port + UUID` (в старом пуле: `1270`). Статус «проверено» присваивается только после успешного HTTPS через VLESS.

Полные URL, время обновления, ошибки загрузки, причины отбраковки, транспорты и результаты стадий HTTPS сохранены в [`lan-source-stats.json`](lan-source-stats.json).

Политика дальнейшего обновления: фиксированный префикс из 2159 записей не накапливается заново; при каждом запуске пересобирается только текущий суффикс из доступных источников. Удаление или замена узлов фиксированного префикса требует отдельной проверяемой миграции.

| Источник | Получено | VLESS | Валидных | Уникальных | Дубли | Добавлено | HTTPS | Статус |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [MahanKenway configs/vless.txt](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) | `142` | `142` | `125` | `76` | `49` | `75` | `0/3` | не проверено |
| [Epodonios Splitted-By-Protocol/vless.txt](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `0` | `0` | `0` | `0` | `0` | `0` | `0/0` | не проверено |
| [barry-far V2ray-config vless.txt](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) | `6249` | `6249` | `5775` | `2152` | `3623` | `1823` | `0/3` | не проверено |
| [SoliSpirit Protocols/vless.txt](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) | `4969` | `4969` | `4407` | `439` | `3968` | `371` | `0/3` | не проверено |
| [liMilCo v2r pro/vless.txt](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) | `3587` | `3587` | `3270` | `277` | `2993` | `207` | `2/3` | проверено |
| [V2RayRoot Config/vless.txt](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) | `263` | `263` | `258` | `15` | `243` | `15` | `0/3` | не проверено |
| [0xRadikal FAST](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/fast/configs.txt) | `763` | `308` | `308` | `111` | `197` | `111` | `3/3` | проверено |
| [v2go Live-tested VLESS](https://raw.githubusercontent.com/Danialsamadi/v2go/main/Splitted-By-Protocol/vless.txt) | `192` | `192` | `183` | `70` | `113` | `68` | `3/3` | проверено |
| [PulseConfigs FAST](https://raw.githubusercontent.com/drmikecrypto/PulseConfigs/main/fast/configs.txt) | `130` | `10` | `10` | `0` | `10` | `0` | `0/0` | не проверено |
| [free-xray-gcp VLESS](https://raw.githubusercontent.com/noahclanman/free-xray-gcp/main/output/protocols/vless.txt) | `414` | `414` | `407` | `85` | `322` | `72` | `2/3` | проверено |
| [multi-proxy-config-fetcher tested](https://raw.githubusercontent.com/4n0nymou3/multi-proxy-config-fetcher/main/configs/proxy_configs_tested.txt) | `178` | `41` | `41` | `2` | `39` | `2` | `2/2` | проверено |
| [patterniha Free-Configs](https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt) | `15` | `12` | `12` | `8` | `4` | `5` | `1/3` | проверено |
| [CaptchaQ working_all](https://raw.githubusercontent.com/CaptchaQ/vless-servers/main/working_all.txt) | `84` | `84` | `84` | `21` | `63` | `17` | `0/3` | не проверено |
| [NodesRadar v2ray](https://radarhub.top/v2ray.txt) | `500` | `3` | `3` | `0` | `3` | `0` | `0/0` | не проверено |
| [mrdevmohamed VLESS](https://raw.githubusercontent.com/mrdevmohamed/v2ray-configs/main/Splitted-By-Protocol/vless.txt) | `1177` | `1177` | `1175` | `198` | `977` | `183` | `1/3` | проверено |
| [Baarcuda top100 VLESS](https://raw.githubusercontent.com/Baarcuda/vpn-configs/master/top100-vless.txt) | `54` | `54` | `54` | `21` | `33` | `18` | `0/3` | не проверено |
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
