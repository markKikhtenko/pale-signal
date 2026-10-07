# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-8742-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-10-07 15:39:02 МСК`

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
| Всего серверов | `8742` |
| Россия | `2643` |
| Global | `6099` |
| Global 5K | `1646` |
| LAN 5K | `5000` |
| LAN 5K из VestraNet | `1473` |
| Global Non-Stable MANUAL | `1646` |
| Global Non-Stable AUTO | `1150` |
| BS Safe MANUAL | `1943` |
| BS Safe AUTO | `50` |
| BS Safe из all_subs | `367` |
| BS Safe TCP / gRPC / XHTTP | `1582` / `190` / `171` |
| Unknown | `351` |
| Reality | `5437` |
| TLS | `7495` |
| TCP | `5377` |
| WebSocket | `1934` |
| gRPC | `677` |
| XHTTP | `754` |

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
| solovyov-jenya2004 all_subs final_sorted | `2026-10-07 15:32 МСК` | `953` | `689` | `689` | [raw](https://raw.githubusercontent.com/solovyov-jenya2004/all_subs/main/final_sorted) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-10-07 15:26 МСК` | `88` | `76` | `76` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| etoneya whitelist | `2026-10-07 15:13 МСК` | `118` | `37` | `37` | [raw](https://etoneya.su/whitelist) |
| zieng2 vless_lite.txt | `2026-10-07 14:59 МСК` | `65` | `49` | `49` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-10-07 14:59 МСК` | `65` | `49` | `49` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| rjsxrd bypass-all | `2026-10-07 14:48 МСК` | `268` | `228` | `228` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| AetrisVPN whitelist pool | `2026-10-07 14:43 МСК` | `416` | `327` | `327` | [raw](https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-10-07 14:09 МСК` | `57` | `52` | `52` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-10-07 14:09 МСК` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-10-07 14:09 МСК` | `13` | `13` | `13` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-10-07 14:09 МСК` | `57` | `52` | `52` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| RKPchannel whitelist.txt | `2026-10-07 13:00 МСК` | `20` | `12` | `12` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/refs/heads/main/whitelist.txt) |
| wlunlocker whitelist_all.txt | `2026-10-07 12:44 МСК` | `479` | `91` | `91` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-10-07 12:41 МСК` | `717` | `250` | `250` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-10-07 11:27 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-10-07 11:22 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlrus wl.txt | `2026-10-07 08:12 МСК` | `1572` | `272` | `272` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `109` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `35` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `121` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |
| AvenCores githubmirror/26.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| AvenCores 26_urls.json | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| EtoNeYaProject GitHub whitelist | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Обычные LAN/global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| ALIILAPRO v2rayNG-Config sub.txt | `2026-10-07 15:30 МСК` | `402` | `382` | `19` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| 0xRadikal light/configs.txt | `2026-10-07 15:23 МСК` | `470` | `449` | `28` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| SoliSpirit Protocols/vless.txt | `2026-10-07 15:06 МСК` | `4064` | `3859` | `99` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-10-07 14:53 МСК` | `3263` | `3092` | `91` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-10-07 12:43 МСК` | `3057` | `2899` | `86` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-10-07 12:20 МСК` | `3268` | `3105` | `90` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| liMilCo v2r pro/vless.txt | `2026-10-07 08:37 МСК` | `3452` | `3275` | `113` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| MahanKenway configs/vless.txt | `2026-10-07 07:54 МСК` | `142` | `135` | `4` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-10-07 07:12 МСК` | `236` | `220` | `12` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-17 13:30 МСК` | `31` | `30` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | `5` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `48` | `0` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

### Специализированные источники

| Источник | Область | Обновление источника | В LAN 5K | Ссылка |
|----------|---------|---------------------|----------|--------|
| VestraNet Nodes protocols/vless.txt | только LAN | `2026-10-07 15:26 МСК` | `1473` | [raw](https://raw.githubusercontent.com/MustafaBaqer/VestraNet-Nodes/main/protocols/vless.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `9848` | `8742` | `-1106` |
| Россия | `↓` | `2739` | `2643` | `-96` |
| Global | `↓` | `7109` | `6099` | `-1010` |
| Global 5K | `↓` | `2001` | `1646` | `-355` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-10-07 15:39:02 МСК` | `8742` | `2643` | `6099` | `1646` | `-621` | `-46` | `-575` | `-115` |
| `2026-10-07 01:20:52 МСК` | `9363` | `2689` | `6674` | `1761` | `+257` | `-20` | `+277` | `+98` |
| `2026-10-06 15:45:27 МСК` | `9106` | `2709` | `6397` | `1663` | `-265` | `-19` | `-246` | `-70` |
| `2026-10-06 02:43:58 МСК` | `9371` | `2728` | `6643` | `1733` | `+105` | `-81` | `+186` | `+24` |
| `2026-10-05 16:32:09 МСК` | `9266` | `2809` | `6457` | `1709` | `-313` | `+48` | `-361` | `+4` |
| `2026-10-04 23:55:16 МСК` | `9579` | `2761` | `6818` | `1705` | `+297` | `+26` | `+271` | `+84` |
| `2026-10-04 14:48:35 МСК` | `9282` | `2735` | `6547` | `1621` | `-88` | `-18` | `-70` | `-48` |
| `2026-10-03 23:38:17 МСК` | `9370` | `2753` | `6617` | `1669` | `-212` | `-109` | `-103` | `-339` |
| `2026-10-03 14:07:05 МСК` | `9582` | `2862` | `6720` | `2008` | `-266` | `+123` | `-389` | `+7` |
| `2026-10-03 00:51:42 МСК` | `9848` | `2739` | `7109` | `2001` | `+550` | `-22` | `+572` | `+226` |

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
