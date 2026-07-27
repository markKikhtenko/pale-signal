# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12638-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-27 22:25:45 МСК`

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
| Всего серверов | `12638` |
| Россия | `4405` |
| Global | `8233` |
| Global 5K | `5000` |
| Unknown | `352` |
| Reality | `8758` |
| TLS | `11138` |
| TCP | `8736` |
| WebSocket | `2336` |
| gRPC | `864` |
| XHTTP | `702` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт первые 5000 узлов из той же сортировки: сначала более свежая дата обновления источника, затем приоритет whitelist/bypass источника. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

<details>
<summary>Источники</summary>

Источники разделены по назначению. `subscription-global.yaml` берёт все non-RU узлы из всех источников. БС / whitelist / bypass shortlist (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `RKP_WHITELIST`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `PRINCE_WHITE_LIST`) получает приоритет в сортировке, затем идут остальные global-пулы.
`subscription-global-5k.yaml` берёт первые 5000 узлов из этого же отсортированного global-списка: сначала свежие БС/whitelist/bypass источники, потом остальные свежие global-источники.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global-файле | Ссылка |
|----------|---------------------|---------------------------|----------------|--------|
| rjsxrd bypass-all | `2026-07-27 22:02 МСК` | `686` | `593` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| zieng2 vless_lite.txt | `2026-07-27 21:59 МСК` | `288` | `252` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-07-27 21:59 МСК` | `288` | `252` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-07-27 21:27 МСК` | `165` | `117` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-07-27 21:27 МСК` | `9` | `9` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-07-27 21:27 МСК` | `84` | `60` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-07-27 21:27 МСК` | `137` | `95` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| AvenCores githubmirror/26.txt | `2026-07-27 21:09 МСК` | `4419` | `2572` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-07-27 20:56 МСК` | `3493` | `1858` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-07-27 20:47 МСК` | `91` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| AvenCores 26_urls.json | `2026-07-27 20:46 МСК` | `3253` | `1325` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-07-27 20:46 МСК` | `1696` | `364` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-07-27 20:46 МСК` | `115` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `2026-07-27 20:05 МСК` | `39` | `22` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| wlunlocker whitelist_all.txt | `2026-07-27 18:39 МСК` | `501` | `100` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| RKP bypass whitelist.txt | `2026-07-27 17:02 МСК` | `130` | `87` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| etoneya whitelist | `2026-07-27 15:56 МСК` | `601` | `499` | [raw](https://etoneya.su/whitelist) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-07-25 18:48 МСК` | `177` | `124` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global-файле | Ссылка |
|----------|---------------------|---------------------------|----------------|--------|
| ALIILAPRO v2rayNG-Config sub.txt | `2026-07-27 22:13 МСК` | `302` | `289` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| SoliSpirit Protocols/vless.txt | `2026-07-27 22:06 МСК` | `3260` | `3169` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-07-27 22:05 МСК` | `2555` | `2491` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-07-27 22:02 МСК` | `2560` | `2496` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| 0xRadikal light/configs.txt | `2026-07-27 21:23 МСК` | `440` | `355` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| Rayan-Config proxy.txt | `2026-07-27 21:18 МСК` | `57` | `56` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| MahanKenway configs/vless.txt | `2026-07-27 20:47 МСК` | `158` | `153` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-07-27 20:41 МСК` | `218` | `206` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-07-27 19:13 МСК` | `2195` | `2138` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-07-27 06:50 МСК` | `2506` | `2431` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `12983` | `12638` | `-345` |
| Россия | `↓` | `4760` | `4405` | `-355` |
| Global | `↑` | `3000` | `8233` | `+5233` |
| Global 5K | `↑` | `3000` | `5000` | `+2000` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|-----------|---------|----------|----------|-------------|
| `2026-07-27 22:25:45 МСК` | `12638` | `4405` | `8233` | `5000` | `+112` | `-24` | `+136` | `0` |
| `2026-07-27 15:22:28 МСК` | `12526` | `4429` | `8097` | `5000` | `+154` | `+73` | `+81` | `0` |
| `2026-07-27 15:13:33 МСК` | `12372` | `4356` | `8016` | `5000` | `-114` | `-71` | `+3619` | `+603` |
| `2026-07-27 14:54:38 МСК` | `12486` | `4427` | `4397` | `4397` | `+54` | `+24` | `+28` | `+28` |
| `2026-07-27 14:46:40 МСК` | `12432` | `4403` | `4369` | `4369` | `-191` | `-92` | `-108` | `+4369` |
| `2026-07-27 14:27:26 МСК` | `12623` | `4495` | `4477` | `4477` | `+134` | `+66` | `+67` | `+67` |
| `2026-07-27 14:18:46 МСК` | `12489` | `4429` | `4410` | `4410` | `-3` | `-133` | `+1410` | `+1410` |
| `2026-07-27 12:48:08 МСК` | `12492` | `4562` | `3000` | `3000` | `+70` | `+412` | `0` | `0` |
| `2026-07-26 22:12:26 МСК` | `12422` | `4150` | `3000` | `3000` | `-561` | `-610` | `0` | `0` |
| `2026-07-26 11:27:46 МСК` | `12983` | `4760` | `3000` | `3000` | `+480` | `+536` | `0` | `0` |

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
