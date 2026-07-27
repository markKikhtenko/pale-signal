# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12372-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-27 15:13:33 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 приоритетных иностранных серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12372` |
| Россия | `4356` |
| Global | `8016` |
| Global 5K | `5000` |
| Unknown | `338` |
| Reality | `8504` |
| TLS | `10896` |
| TCP | `8465` |
| WebSocket | `2313` |
| gRPC | `901` |
| XHTTP | `693` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт первые 5000 узлов из той же сортировки: сначала более свежая дата обновления источника, затем приоритет whitelist/bypass источника. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

<details>
<summary>Источники</summary>

Источники разделены по назначению. `subscription-global.yaml` берёт все non-RU узлы из всех источников. БС / whitelist / bypass shortlist (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `RKP_WHITELIST`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `PRINCE_WHITE_LIST`) получает приоритет в сортировке, затем идут остальные global-пулы.
`subscription-global-5k.yaml` берёт первые 5000 узлов из этого же отсортированного global-списка: сначала свежие БС/whitelist/bypass источники, потом остальные свежие global-источники.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global-файле | Ссылка |
|----------|---------------------|---------------------------|----------------|--------|
| igareck WHITE-CIDR-RU-all.txt | `2026-07-27 15:01 МСК` | `60` | `47` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-07-27 15:01 МСК` | `30` | `30` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-07-27 15:01 МСК` | `14` | `11` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-07-27 15:01 МСК` | `60` | `47` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| rjsxrd bypass-all | `2026-07-27 15:01 МСК` | `747` | `670` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| zieng2 vless_lite.txt | `2026-07-27 14:59 МСК` | `250` | `225` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-07-27 14:59 МСК` | `250` | `225` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| AvenCores githubmirror/26.txt | `2026-07-27 14:47 МСК` | `4385` | `2539` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| AvenCores 26_urls.json | `2026-07-27 14:29 МСК` | `2693` | `768` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-07-27 14:29 МСК` | `1760` | `354` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| RKP bypass whitelist.txt | `2026-07-27 14:11 МСК` | `120` | `69` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-07-27 12:34 МСК` | `3439` | `1907` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-07-27 11:37 МСК` | `91` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-07-27 11:35 МСК` | `115` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_all.txt | `2026-07-27 11:27 МСК` | `511` | `129` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| etoneya whitelist | `2026-07-27 02:53 МСК` | `0` | `0` | [raw](https://etoneya.su/whitelist) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `-` | `177` | `136` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `-` | `20` | `13` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global-файле | Ссылка |
|----------|---------------------|---------------------------|----------------|--------|
| 0xRadikal light/configs.txt | `2026-07-27 15:08 МСК` | `462` | `369` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| SoliSpirit Protocols/vless.txt | `2026-07-27 15:06 МСК` | `3379` | `3276` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-07-27 15:05 МСК` | `288` | `272` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| MahanKenway configs/vless.txt | `2026-07-27 14:28 МСК` | `148` | `143` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-07-27 14:18 МСК` | `215` | `202` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-07-27 13:45 МСК` | `2113` | `2051` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| Rayan-Config proxy.txt | `2026-07-27 13:33 МСК` | `52` | `51` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| barry-far V2ray-config vless.txt | `2026-07-27 11:52 МСК` | `2408` | `2341` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-07-27 11:49 МСК` | `2405` | `2338` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| liMilCo v2r pro/vless.txt | `2026-07-27 06:50 МСК` | `2506` | `2428` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `47` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `12510` | `12372` | `-138` |
| Россия | `↓` | `4398` | `4356` | `-42` |
| Global | `↑` | `3000` | `8016` | `+5016` |
| Global 5K | `↑` | `3000` | `5000` | `+2000` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|-----------|---------|----------|----------|-------------|
| `2026-07-27 15:13:33 МСК` | `12372` | `4356` | `8016` | `5000` | `-114` | `-71` | `+3619` | `+603` |
| `2026-07-27 14:54:38 МСК` | `12486` | `4427` | `4397` | `4397` | `+54` | `+24` | `+28` | `+28` |
| `2026-07-27 14:46:40 МСК` | `12432` | `4403` | `4369` | `4369` | `-191` | `-92` | `-108` | `+4369` |
| `2026-07-27 14:27:26 МСК` | `12623` | `4495` | `4477` | `4477` | `+134` | `+66` | `+67` | `+67` |
| `2026-07-27 14:18:46 МСК` | `12489` | `4429` | `4410` | `4410` | `-3` | `-133` | `+1410` | `+1410` |
| `2026-07-27 12:48:08 МСК` | `12492` | `4562` | `3000` | `3000` | `+70` | `+412` | `0` | `0` |
| `2026-07-26 22:12:26 МСК` | `12422` | `4150` | `3000` | `3000` | `-561` | `-610` | `0` | `0` |
| `2026-07-26 11:27:46 МСК` | `12983` | `4760` | `3000` | `3000` | `+480` | `+536` | `0` | `0` |
| `2026-07-25 22:08:50 МСК` | `12503` | `4224` | `3000` | `3000` | `-7` | `-174` | `0` | `0` |
| `2026-07-25 15:10:17 МСК` | `12510` | `4398` | `3000` | `3000` | `+181` | `+43` | `0` | `0` |

</details>

## Группы

Во всех подписках оставлены только группы `AUTO`, `MANUAL` и `PROXY`.

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
- Узлы без определенной страны попадают в global-подписки и получают `[UNKNOWN]` в имени.

## Обновление

GitHub Actions запускает пересборку два раза в сутки: в 09:00 и 21:00 по МСК. В GitHub cron это `0 6,18 * * *`, потому что расписание задается в UTC. GitHub может задерживать scheduled-запуски; ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.

Если часть источников не скачалась, она пропускается. Если серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
