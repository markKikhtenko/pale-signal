# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12267-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-25 11:05:58 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Curated иностранные серверы для обхода БС, до 3000 узлов | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global checked** | Иностранные серверы из всех источников, проверенные Mihomo; БС/whitelist shortlist проверяется первым | https://markkikhtenko.github.io/pale-signal/subscription-global-checked.yaml | [subscription-global-checked.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-checked.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12267` |
| Россия | `4091` |
| Global | `3000` |
| Unknown | `0` |
| Reality | `8385` |
| TLS | `10730` |
| TCP | `8465` |
| WebSocket | `2316` |
| gRPC | `788` |
| XHTTP | `698` |

`subscription-global.yaml` каждый запуск собирается заново из свежих trusted whitelist/26 источников, но обрезается до 3000 серверов, чтобы не перегружать роутер.

`subscription-global-checked.yaml` создаётся после полной `subscription.yaml`: GitHub Actions берёт иностранные серверы из всех источников, сначала проверяет БС/whitelist shortlist из `subscription-global.yaml`, затем остальные, и оставляет только прошедшие проверку через API Mihomo.

<details>
<summary>Источники</summary>

Источники разделены по назначению. `subscription-global.yaml` берёт только узлы из БС / whitelist / bypass shortlist (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `RKP_WHITELIST`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `PRINCE_WHITE_LIST`), сортирует их по дате публикации источника и ограничивает до 3000 серверов. Остальные источники остаются только в полной `subscription.yaml`.

### Global shortlist

| Источник | Обновление источника | Серверов в общей подписке | В Global-файле | Ссылка |
|----------|---------------------|---------------------------|----------------|--------|
| zieng2 vless_lite.txt | `2026-07-25 10:59 МСК` | `309` | `273` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-07-25 10:59 МСК` | `303` | `269` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| rjsxrd bypass-all | `2026-07-25 10:37 МСК` | `851` | `771` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-07-25 10:34 МСК` | `3285` | `1958` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-07-25 10:22 МСК` | `185` | `159` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-07-25 10:18 МСК` | `56` | `49` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-07-25 10:18 МСК` | `5` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-07-25 10:18 МСК` | `32` | `32` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-07-25 10:18 МСК` | `56` | `49` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| AvenCores githubmirror/26.txt | `2026-07-25 09:35 МСК` | `4252` | `1359` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-07-25 09:23 МСК` | `91` | `12` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-07-25 09:21 МСК` | `115` | `0` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| AvenCores 26_urls.json | `2026-07-25 09:21 МСК` | `2892` | `608` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-07-25 09:21 МСК` | `1601` | `62` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_all.txt | `2026-07-25 09:13 МСК` | `504` | `32` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| etoneya whitelist | `2026-07-25 09:06 МСК` | `419` | `300` | [raw](https://etoneya.su/whitelist) |
| RKP bypass whitelist.txt | `2026-07-25 08:16 МСК` | `342` | `64` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `2026-07-25 01:54 МСК` | `42` | `18` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `1` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `14` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |

### Общие global-пулы только для полной подписки

| Источник | Серверов в общей подписке | Ссылка |
|----------|---------------------------|--------|
| SoliSpirit Protocols/vless.txt | `3452` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| barry-far V2ray-config vless.txt | `2598` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| liMilCo v2r pro/vless.txt | `2534` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2502` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2213` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| 0xRadikal light/configs.txt | `408` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `374` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| MatinGhanbari filtered vless.txt | `274` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| V2RayRoot Config/vless.txt | `201` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| MahanKenway configs/vless.txt | `149` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MahsaNetConfigTopic xray_final.txt | `147` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |
| Rayan-Config proxy.txt | `53` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| FNET00 Config/Main | `50` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `12239` | `12267` | `+28` |
| Россия | `↑` | `4036` | `4091` | `+55` |
| Global | `↑` | `2500` | `3000` | `+500` |

| Обновление, МСК | Общая | Россия | Global | Δ общая | Δ Россия | Δ Global |
|-----------------|-------|--------|--------|---------|----------|----------|
| `2026-07-25 11:05:58 МСК` | `12267` | `4091` | `3000` | `+305` | `+98` | `0` |
| `2026-07-24 22:25:33 МСК` | `11962` | `3993` | `3000` | `-168` | `-15` | `0` |
| `2026-07-24 11:25:28 МСК` | `12130` | `4008` | `3000` | `-49` | `-80` | `0` |
| `2026-07-23 22:53:16 МСК` | `12179` | `4088` | `3000` | `-138` | `+2` | `0` |
| `2026-07-23 22:17:13 МСК` | `12317` | `4086` | `3000` | `+190` | `+15` | `0` |
| `2026-07-23 22:08:07 МСК` | `12127` | `4071` | `3000` | `+101` | `+74` | `0` |
| `2026-07-23 22:03:03 МСК` | `12026` | `3997` | `3000` | `0` | `0` | `0` |
| `2026-07-23 21:57:39 МСК` | `12026` | `3997` | `3000` | `0` | `0` | `0` |
| `2026-07-23 21:51:16 МСК` | `12026` | `3997` | `3000` | `-213` | `-39` | `+500` |
| `2026-07-23 17:48:49 МСК` | `12239` | `4036` | `2500` | `-187` | `-16` | `0` |

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
