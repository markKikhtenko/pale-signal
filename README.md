# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-9675-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-09-30 14:55:57 МСК`

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
| Всего серверов | `9675` |
| Россия | `2782` |
| Global | `6893` |
| Global 5K | `2113` |
| LAN 5K | `5000` |
| LAN 5K из VestraNet | `1304` |
| Global Non-Stable MANUAL | `2113` |
| Global Non-Stable AUTO | `1430` |
| BS Safe MANUAL | `2205` |
| BS Safe AUTO | `50` |
| BS Safe из all_subs | `296` |
| BS Safe TCP / gRPC / XHTTP | `1812` / `228` / `165` |
| Unknown | `338` |
| Reality | `5886` |
| TLS | `8143` |
| TCP | `5755` |
| WebSocket | `2294` |
| gRPC | `895` |
| XHTTP | `731` |

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
| solovyov-jenya2004 all_subs final_sorted | `2026-09-30 14:48 МСК` | `1075` | `741` | `741` | [raw](https://raw.githubusercontent.com/solovyov-jenya2004/all_subs/main/final_sorted) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-09-30 14:42 МСК` | `178` | `139` | `139` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| RKPchannel whitelist.txt | `2026-09-30 14:42 МСК` | `51` | `22` | `22` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/refs/heads/main/whitelist.txt) |
| etoneya whitelist | `2026-09-30 14:39 МСК` | `150` | `38` | `38` | [raw](https://etoneya.su/whitelist) |
| rjsxrd bypass-all | `2026-09-30 14:39 МСК` | `272` | `247` | `247` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-09-30 14:25 МСК` | `22` | `18` | `18` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-09-30 14:25 МСК` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-09-30 14:25 МСК` | `5` | `5` | `5` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-09-30 14:25 МСК` | `22` | `18` | `18` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| zieng2 vless_lite.txt | `2026-09-30 13:59 МСК` | `77` | `58` | `58` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-09-30 13:59 МСК` | `77` | `58` | `58` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| AetrisVPN whitelist pool | `2026-09-30 10:38 МСК` | `448` | `363` | `363` | [raw](https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-09-30 09:31 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-09-30 09:28 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-09-30 09:21 МСК` | `1097` | `581` | `581` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| wlrus wl.txt | `2026-09-30 07:52 МСК` | `1594` | `273` | `273` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_all.txt | `2026-09-30 00:48 МСК` | `462` | `85` | `85` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
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
| 0xRadikal light/configs.txt | `2026-09-30 14:45 МСК` | `523` | `498` | `26` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-09-30 14:40 МСК` | `420` | `394` | `17` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-09-30 14:32 МСК` | `3487` | `3333` | `108` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| SoliSpirit Protocols/vless.txt | `2026-09-30 14:06 МСК` | `4251` | `4064` | `127` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-09-30 11:58 МСК` | `3508` | `3357` | `112` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-09-30 10:56 МСК` | `246` | `232` | `8` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-09-30 09:33 МСК` | `3314` | `3174` | `108` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-09-30 08:16 МСК` | `3828` | `3664` | `141` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| MahanKenway configs/vless.txt | `2026-09-30 07:34 МСК` | `151` | `145` | `5` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-17 13:30 МСК` | `31` | `30` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | `5` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `48` | `0` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

### Специализированные источники

| Источник | Область | Обновление источника | В LAN 5K | Ссылка |
|----------|---------|---------------------|----------|--------|
| VestraNet Nodes protocols/vless.txt | только LAN | `2026-09-30 14:41 МСК` | `1304` | [raw](https://raw.githubusercontent.com/MustafaBaqer/VestraNet-Nodes/main/protocols/vless.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `11448` | `9675` | `-1773` |
| Россия | `↑` | `2619` | `2782` | `+163` |
| Global | `↓` | `8829` | `6893` | `-1936` |
| Global 5K | `↓` | `3773` | `2113` | `-1660` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-09-30 14:55:57 МСК` | `9675` | `2782` | `6893` | `2113` | `-398` | `+133` | `-531` | `-38` |
| `2026-09-30 00:55:07 МСК` | `10073` | `2649` | `7424` | `2151` | `+158` | `-97` | `+255` | `-81` |
| `2026-09-29 15:09:16 МСК` | `9915` | `2746` | `7169` | `2232` | `-461` | `-97` | `-364` | `-118` |
| `2026-09-29 02:03:28 МСК` | `10376` | `2843` | `7533` | `2350` | `+605` | `+190` | `+415` | `+79` |
| `2026-09-28 15:53:53 МСК` | `9771` | `2653` | `7118` | `2271` | `-132` | `-53` | `-79` | `+13` |
| `2026-09-27 23:53:17 МСК` | `9903` | `2706` | `7197` | `2258` | `+438` | `+117` | `+321` | `+60` |
| `2026-09-27 14:24:04 МСК` | `9465` | `2589` | `6876` | `2198` | `-53` | `-29` | `-24` | `+54` |
| `2026-09-26 23:42:35 МСК` | `9518` | `2618` | `6900` | `2144` | `-1533` | `+113` | `-1646` | `-1794` |
| `2026-09-26 13:51:44 МСК` | `11051` | `2505` | `8546` | `3938` | `-397` | `-114` | `-283` | `+165` |
| `2026-09-26 00:09:50 МСК` | `11448` | `2619` | `8829` | `3773` | `+210` | `+44` | `+166` | `-158` |

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
