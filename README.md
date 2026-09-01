# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-14052-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-09-01 14:13:45 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 самых свежих иностранных БС/whitelist/bypass серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |
| **pale-signal подписка - LAN 5K** | До 5000 иностранных узлов для проводного интернета; без БС/whitelist/mobile/CIDR-пулов | https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml | [subscription-lan-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml) |
| **pale-signal подписка - Global Non-Stable** | Тестовая Global 5K: полный MANUAL, AUTO без дублей endpoint | https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml | [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) |
| **pale-signal подписка - BS Safe** | До 2500 свежих Reality-узлов из БС-источников; AUTO ограничен 50 нодами | https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml | [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `14052` |
| Россия | `3712` |
| Global | `10340` |
| Global 5K | `5000` |
| LAN 5K | `5000` |
| LAN 5K из VestraNet | `1418` |
| Global Non-Stable MANUAL | `5000` |
| Global Non-Stable AUTO | `4222` |
| BS Safe MANUAL | `2500` |
| BS Safe AUTO | `50` |
| BS Safe из all_subs | `417` |
| BS Safe TCP / gRPC / XHTTP | `1942` / `407` / `151` |
| Unknown | `433` |
| Reality | `9562` |
| TLS | `11909` |
| TCP | `9499` |
| WebSocket | `2752` |
| gRPC | `996` |
| XHTTP | `805` |

Для OpenClash при активных блокировках используйте `BS Safe`: в `MANUAL` доступно до 2500 Reality-узлов из базовых LTE/whitelist/bypass-источников, включая `all_subs`, а `AUTO` проверяет только 50, чтобы не перегружать роутер.

Для обычного домашнего или офисного проводного подключения используйте `LAN 5K`. Она дополнена проводным пулом VestraNet; узлы, специально собранные под белые списки и CIDR-ограничения мобильных операторов, в неё не входят.

Подписка собирает и фильтрует узлы, но не может гарантировать их работу у конкретного провайдера.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из базовых источников и остаётся полным большим global-списком. Специализированные LAN-only источники в него не попадают.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`RKP_BYPASS`, `SOLOVYOV_ALL_SUBS`, `AETRIS_BYPASS`, `AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.
`subscription-lan-5k.yaml` берёт до 5000 узлов с подтверждённой страной не RU только из обычных проводных пулов (`RADIKAL_LIGHT`, `MAHAN_VLESS`, `EPODONIOS_VLESS`, `BARRY_FAR_VLESS`, `SOLISPIRIT_VLESS`, `MATIN_VLESS`, `LIMILCO_VLESS`, `V2RAYROOT_VLESS`, `SURFBOARD_MIXED`, `ALIILAPRO_SUB`, `MAHSANET_XRAY_FINAL`, `RAYAN_PROXY`, `FNET_MAIN`, `VESTRANET_VLESS`); БС, whitelist, mobile и CIDR-источники исключены.
`SOLOVYOV_ALL_SUBS` — базовый LTE/whitelist-источник: его узлы участвуют в общей, RU, Global, Global 5K, Global Non-Stable и BS Safe, но исключены из LAN 5K.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| solovyov-jenya2004 all_subs final_sorted | `2026-09-01 13:59 МСК` | `1315` | `867` | `867` | [raw](https://raw.githubusercontent.com/solovyov-jenya2004/all_subs/main/final_sorted) |
| rjsxrd bypass-all | `2026-09-01 13:59 МСК` | `261` | `241` | `241` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-09-01 13:56 МСК` | `1521` | `1088` | `1088` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-09-01 13:34 МСК` | `2197` | `2193` | `2192` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| AvenCores 26_urls.json | `2026-09-01 13:26 МСК` | `2739` | `667` | `667` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| etoneya whitelist | `2026-09-01 13:26 МСК` | `343` | `83` | `83` | [raw](https://etoneya.su/whitelist) |
| zieng2 vless_lite.txt | `2026-09-01 12:59 МСК` | `160` | `124` | `124` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-09-01 12:59 МСК` | `160` | `124` | `124` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-09-01 12:54 МСК` | `16` | `9` | `9` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-09-01 12:54 МСК` | `12` | `1` | `1` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-09-01 12:54 МСК` | `10` | `9` | `9` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-09-01 12:54 МСК` | `16` | `9` | `9` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-09-01 12:52 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| AetrisVPN whitelist pool | `2026-09-01 11:47 МСК` | `586` | `493` | `493` | [raw](https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-09-01 10:33 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| AvenCores githubmirror/26.txt | `2026-09-01 09:31 МСК` | `4700` | `2720` | `2257` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| RKPchannel whitelist.txt | `2026-09-01 08:18 МСК` | `76` | `38` | `38` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/refs/heads/main/whitelist.txt) |
| wlrus wl.txt | `2026-09-01 07:24 МСК` | `1596` | `311` | `311` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_all.txt | `2026-09-01 04:35 МСК` | `512` | `94` | `94` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-08-31 20:12 МСК` | `110` | `99` | `73` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `3` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `0` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `0` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |
| EtoNeYaProject GitHub whitelist | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Обычные LAN/global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| Epodonios Splitted-By-Protocol/vless.txt | `2026-09-01 13:45 МСК` | `2991` | `2883` | `175` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| 0xRadikal light/configs.txt | `2026-09-01 13:45 МСК` | `1254` | `1233` | `152` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-09-01 13:29 МСК` | `270` | `262` | `47` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| SoliSpirit Protocols/vless.txt | `2026-09-01 13:06 МСК` | `3792` | `3664` | `237` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-09-01 12:11 МСК` | `197` | `190` | `39` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-09-01 10:10 МСК` | `2862` | `2762` | `160` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| barry-far V2ray-config vless.txt | `2026-09-01 09:38 МСК` | `2991` | `2883` | `175` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| liMilCo v2r pro/vless.txt | `2026-09-01 07:48 МСК` | `3017` | `2902` | `206` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| MahanKenway configs/vless.txt | `2026-09-01 07:07 МСК` | `147` | `139` | `17` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-17 13:30 МСК` | `31` | `30` | `1` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `200` | `195` | `24` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `48` | `0` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

### Специализированные источники

| Источник | Область | Обновление источника | В LAN 5K | Ссылка |
|----------|---------|---------------------|----------|--------|
| VestraNet Nodes protocols/vless.txt | только LAN | `2026-09-01 13:55 МСК` | `1418` | [raw](https://raw.githubusercontent.com/MustafaBaqer/VestraNet-Nodes/main/protocols/vless.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `14273` | `14052` | `-221` |
| Россия | `↓` | `3747` | `3712` | `-35` |
| Global | `↓` | `10526` | `10340` | `-186` |
| Global 5K | `→` | `5000` | `5000` | `0` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-09-01 14:13:45 МСК` | `14052` | `3712` | `10340` | `5000` | `+525` | `+195` | `+330` | `0` |
| `2026-09-01 01:26:36 МСК` | `13527` | `3517` | `10010` | `5000` | `+216` | `+83` | `+133` | `0` |
| `2026-08-31 15:37:35 МСК` | `13311` | `3434` | `9877` | `5000` | `+64` | `+5` | `+59` | `0` |
| `2026-08-30 23:33:24 МСК` | `13247` | `3429` | `9818` | `5000` | `-233` | `-69` | `-164` | `0` |
| `2026-08-30 14:13:11 МСК` | `13480` | `3498` | `9982` | `5000` | `-2198` | `-183` | `-2015` | `0` |
| `2026-08-29 23:24:43 МСК` | `15678` | `3681` | `11997` | `5000` | `+1605` | `+111` | `+1494` | `0` |
| `2026-08-29 15:16:52 МСК` | `14072` | `3570` | `10502` | `5000` | `-310` | `-205` | `-105` | `0` |
| `2026-08-28 21:14:13 МСК` | `14382` | `3775` | `10607` | `5000` | `-158` | `+48` | `-206` | `0` |
| `2026-08-28 05:08:31 МСК` | `14540` | `3727` | `10813` | `5000` | `+267` | `-20` | `+287` | `0` |
| `2026-08-27 20:24:08 МСК` | `14273` | `3747` | `10526` | `5000` | `-453` | `+119` | `-572` | `0` |

</details>

## Группы

| Группа | Тип | Назначение |
|--------|-----|------------|
| `AUTO` | `url-test` | Автовыбор серверов через URL Test |
| `MANUAL` | `select` | Ручной выбор сервера |
| `PROXY` | `select` | Главная группа для правила `MATCH,PROXY` |

В `BS Safe` группа `PROXY` по умолчанию открывает `MANUAL`. Для автоматического поиска выберите `AUTO`: в нём до 50 нод из разных подсетей и с разными SNI.

### BS Safe в OpenClash

1. В `Plugin Settings` → `Version Update` обновите **Meta Core** до Mihomo v1.19.24 или новее и выберите ядро `Meta`.
2. В `Config Subscription` добавьте прямую ссылку на `subscription-bs-safe.yaml` из таблицы выше. Конвертацию включать не нужно.
3. Обновите подписку, активируйте профиль и примените конфигурацию.
4. В Dashboard выберите `PROXY` → `AUTO` для автоматического поиска или `PROXY` → `MANUAL` для ручного выбора.

Не запускайте массовую проверку всех нод из `MANUAL`: тестируйте через `AUTO` или по одной ноде.

## Разделение по странам

Страна берётся из имени узла. Если её там нет, используется GeoIP адреса `server`. Неопределённые узлы получают `[UNKNOWN]` и попадают в Global.

## Обновление

Подписки обновляются каждый день в 09:00 и 21:00 МСК. Недоступные источники пропускаются, а некорректная сборка не публикуется.
