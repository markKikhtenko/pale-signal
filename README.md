# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12167-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-23 11:28:21 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Curated иностранные серверы для обхода БС, до 2500 узлов | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global checked** | Иностранные серверы из полной общей подписки, проверенные ядром Mihomo | https://markkikhtenko.github.io/pale-signal/subscription-global-checked.yaml | [subscription-global-checked.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-checked.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12167` |
| Россия | `2648` |
| Global | `2500` |
| Unknown | `1682` |
| Reality | `8276` |
| TLS | `10657` |
| TCP | `8340` |
| WebSocket | `2312` |
| gRPC | `862` |
| XHTTP | `653` |

`subscription-global.yaml` каждый запуск собирается заново из свежих trusted whitelist/26 источников, но обрезается до 2500 серверов, чтобы не перегружать роутер.

`subscription-global-checked.yaml` создаётся после полной `subscription.yaml`: GitHub Actions берёт иностранные серверы из полной подписки и оставляет только те, которые прошли проверку через API Mihomo.

<details>
<summary>Источники</summary>

Источники разделены по назначению. `subscription-global.yaml` берёт только свежие узлы из curated shortlist (`AVEN_MIRROR_26`, `AVEN_26`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`) и ограничен до 2500 серверов. Остальные источники остаются только в полной `subscription.yaml`.

### Global shortlist

| Источник | Серверов в общей подписке | В Global-файле | Ссылка |
|----------|---------------------------|----------------|--------|
| AvenCores githubmirror/26.txt | `4215` | `2500` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| AvenCores 26_urls.json | `2815` | `426` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `1620` | `166` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| etoneya whitelist | `293` | `168` | [raw](https://etoneya.su/whitelist) |
| ByeWhiteLists2 | `633` | `81` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| zieng2 vless_universal.txt | `260` | `14` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| zieng2 vless_lite.txt | `260` | `14` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| igareck WHITE-CIDR-RU-all.txt | `67` | `4` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `31` | `7` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `4` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `67` | `4` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |

### БС / whitelist / bypass только для полной подписки

| Источник | Серверов в общей подписке | Ссылка |
|----------|---------------------------|--------|
| V.O.I.D VPN Bypass url_work.txt | `2993` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| rjsxrd bypass-all | `1242` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| wlunlocker whitelist_all.txt | `540` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `154` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `119` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `115` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `91` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| RKP bypass whitelist.txt | `80` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `20` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Общие global-пулы только для полной подписки

| Источник | Серверов в общей подписке | Ссылка |
|----------|---------------------------|--------|
| SoliSpirit Protocols/vless.txt | `3483` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| liMilCo v2r pro/vless.txt | `2625` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| barry-far V2ray-config vless.txt | `2530` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2525` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2187` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| ALIILAPRO v2rayNG-Config sub.txt | `395` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| 0xRadikal light/configs.txt | `385` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| MatinGhanbari filtered vless.txt | `282` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| V2RayRoot Config/vless.txt | `201` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| MahanKenway configs/vless.txt | `141` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MahsaNetConfigTopic xray_final.txt | `132` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |
| Rayan-Config proxy.txt | `51` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| FNET00 Config/Main | `50` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `11865` | `12167` | `+302` |
| Россия | `↓` | `3162` | `2648` | `-514` |
| Global | `↓` | `8703` | `2500` | `-6203` |

| Обновление, МСК | Общая | Россия | Global | Δ общая | Δ Россия | Δ Global |
|-----------------|-------|--------|--------|---------|----------|----------|
| `2026-07-23 11:28:21 МСК` | `12167` | `2648` | `2500` | `+196` | `-336` | `0` |
| `2026-07-23 09:23:12 МСК` | `11971` | `2984` | `2500` | `-153` | `-636` | `0` |
| `2026-07-22 21:25:27 МСК` | `12124` | `3620` | `2500` | `0` | `+481` | `0` |
| `2026-07-22 21:17:39 МСК` | `12124` | `3139` | `2500` | `+100` | `-806` | `0` |
| `2026-07-22 21:09:33 МСК` | `12024` | `3945` | `2500` | `-103` | `+6` | `-5688` |
| `2026-07-22 19:48:39 МСК` | `12127` | `3939` | `8188` | `+54` | `+870` | `-816` |
| `2026-07-22 17:24:24 МСК` | `12073` | `3069` | `9004` | `+110` | `-33` | `+143` |
| `2026-07-22 15:06:08 МСК` | `11963` | `3102` | `8861` | `-60` | `-28` | `-32` |
| `2026-07-22 12:41:53 МСК` | `12023` | `3130` | `8893` | `+158` | `-32` | `+190` |
| `2026-07-22 09:45:36 МСК` | `11865` | `3162` | `8703` | `-49` | `-602` | `+553` |

</details>

## Группы

Во всех трех подписках оставлены только группы `AUTO`, `MANUAL` и `PROXY`.

| Группа | Тип | Назначение |
|--------|-----|------------|
| `AUTO` | `url-test` | Автовыбор серверов через URL Test |
| `MANUAL` | `select` | Ручной выбор сервера |
| `PROXY` | `select` | Главная группа для правила `MATCH,PROXY` |

Параметры `AUTO`: `interval: 900`, `tolerance: 100`, `lazy: true`.

## Разделение по странам

- Сначала используется флаг или страна в имени узла.
- Если страны в имени нет, используется GeoIP фактического поля `server`.
- Если `server` является доменом, он сначала разрешается в IP.
- SNI, `servername`, `Host`, XHTTP host и gRPC service name не используются для определения страны.
- Узлы без определенной страны попадают в `subscription-global.yaml` и получают `[UNKNOWN]` в имени.

## Обновление

GitHub Actions запускает пересборку два раза в сутки: в 09:00 и 21:00 по МСК. В GitHub cron это `0 6,18 * * *`, потому что расписание задается в UTC. GitHub может задерживать scheduled-запуски; ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.

Если часть источников не скачалась, она пропускается. Если серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
