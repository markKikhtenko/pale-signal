# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-9708-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-10-11 08:32:55 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 самых свежих иностранных БС/whitelist/bypass серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |
| **pale-signal подписка - LAN 5K** | До 5000 иностранных узлов для проводного интернета; без БС/whitelist/mobile/CIDR-пулов | https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml | [subscription-lan-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml) |
| **pale-signal подписка - LAN Global** | Все доступные иностранные узлы из тех же LAN-пулов, без лимита 5000 | https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml | [subscription-lan-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml) |
| **pale-signal подписка - Global Non-Stable** | Тестовая Global 5K: полный MANUAL, AUTO без дублей endpoint | https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml | [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) |
| **pale-signal подписка - BS Safe** | До 2500 свежих Reality-узлов из БС-источников; AUTO ограничен 50 нодами | https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml | [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `9708` |
| Россия | `2649` |
| Global | `7059` |
| Global 5K | `2227` |
| LAN 5K | `5000` |
| LAN Global | `5815` |
| LAN 5K из VestraNet | `1335` |
| Global Non-Stable MANUAL | `2227` |
| Global Non-Stable AUTO | `1584` |
| BS Safe MANUAL | `2103` |
| BS Safe AUTO | `50` |
| BS Safe из all_subs | `492` |
| BS Safe TCP / gRPC / XHTTP | `1683` / `228` / `192` |
| Unknown | `343` |
| Reality | `5867` |
| TLS | `8414` |
| TCP | `5748` |
| WebSocket | `2272` |
| gRPC | `816` |
| XHTTP | `872` |

Для OpenClash при активных блокировках используйте `BS Safe`: в `MANUAL` доступно до 2500 Reality-узлов из базовых LTE/whitelist/bypass-источников, включая `all_subs`, а `AUTO` проверяет только 50, чтобы не перегружать роутер.

Для обычного домашнего или офисного проводного подключения используйте `LAN 5K` или полную `LAN Global`. Обе подписки используют одинаковые LAN-пулы и исключают узлы, специально собранные под белые списки и CIDR-ограничения мобильных операторов; `LAN Global` отличается только отсутствием лимита 5000.

## Маршрутизация по чёрным спискам

Отдельный [Overwrite Module](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing.conf) оставляет обычный трафик на `DIRECT`, а ресурсы из автоматически обновляемых Re:filter-списков направляет в существующую группу `PROXY`. Пользовательские исключения находятся в `openclash/rules/custom-direct-*.yaml`, а принудительное проксирование — в `openclash/rules/custom-proxy-*.yaml`.

В OpenClash добавьте URL модуля в `Overwrite Modules` и включите его для нужной конфигурации. Если используются другие модули, добавляющие правила, применяйте этот модуль последним: он сохраняет существующие специальные правила, затем добавляет пользовательские DIRECT/PROXY, внешние списки и единственный финальный `MATCH,DIRECT`. Внутри блока модуля пользовательские списки имеют приоритет над внешними. Модуль не задаёт `dns.nameserver`, `dns.fallback` или `dns.proxy-server-nameserver`, поэтому существующие DNS-серверы не заменяются.

Подписка собирает и фильтрует узлы, но не может гарантировать их работу у конкретного провайдера.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из базовых источников и остаётся полным большим global-списком. Специализированные LAN-only источники в него не попадают.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`RKP_BYPASS`, `SOLOVYOV_ALL_SUBS`, `AETRIS_BYPASS`, `AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.
`subscription-lan-5k.yaml` берёт до 5000 узлов с подтверждённой страной не RU только из обычных проводных пулов (`RADIKAL_LIGHT`, `MAHAN_VLESS`, `EPODONIOS_VLESS`, `BARRY_FAR_VLESS`, `SOLISPIRIT_VLESS`, `MATIN_VLESS`, `LIMILCO_VLESS`, `V2RAYROOT_VLESS`, `SURFBOARD_MIXED`, `ALIILAPRO_SUB`, `MAHSANET_XRAY_FINAL`, `RAYAN_PROXY`, `FNET_MAIN`, `VESTRANET_VLESS`); БС, whitelist, mobile и CIDR-источники исключены.
`subscription-lan-global.yaml` использует те же LAN-пулы и фильтры, но включает все доступные узлы без искусственного лимита.
`SOLOVYOV_ALL_SUBS` — базовый LTE/whitelist-источник: его узлы участвуют в общей, RU, Global, Global 5K, Global Non-Stable и BS Safe, но исключены из LAN 5K и LAN Global.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| solovyov-jenya2004 all_subs final_sorted | `2026-10-11 08:26 МСК` | `1430` | `1104` | `1104` | [raw](https://raw.githubusercontent.com/solovyov-jenya2004/all_subs/main/final_sorted) |
| rjsxrd bypass-all | `2026-10-11 08:25 МСК` | `676` | `584` | `584` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-10-11 08:17 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlrus wl.txt | `2026-10-11 08:00 МСК` | `1572` | `275` | `275` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| zieng2 vless_lite.txt | `2026-10-11 07:59 МСК` | `151` | `110` | `110` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-10-11 07:59 МСК` | `151` | `110` | `110` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-10-11 07:55 МСК` | `118` | `79` | `79` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-10-11 07:55 МСК` | `1` | `1` | `1` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-10-11 07:55 МСК` | `12` | `8` | `8` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-10-11 07:55 МСК` | `118` | `79` | `79` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| etoneya whitelist | `2026-10-11 05:43 МСК` | `108` | `59` | `59` | [raw](https://etoneya.su/whitelist) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-10-11 04:43 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-10-11 04:39 МСК` | `679` | `306` | `306` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| AetrisVPN whitelist pool | `2026-10-11 04:23 МСК` | `406` | `319` | `319` | [raw](https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-10-11 03:29 МСК` | `150` | `97` | `97` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| wlunlocker whitelist_all.txt | `2026-10-11 02:10 МСК` | `506` | `93` | `93` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| RKPchannel whitelist.txt | `2026-10-08 00:03 МСК` | `1` | `1` | `1` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/refs/heads/main/whitelist.txt) |
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
| 0xRadikal light/configs.txt | `2026-10-11 08:22 МСК` | `564` | `533` | `61` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| SoliSpirit Protocols/vless.txt | `2026-10-11 08:06 МСК` | `3965` | `3782` | `151` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-10-11 08:05 МСК` | `428` | `412` | `31` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| MahanKenway configs/vless.txt | `2026-10-11 07:39 МСК` | `163` | `158` | `11` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-10-11 05:21 МСК` | `3365` | `3204` | `128` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-10-11 04:59 МСК` | `3387` | `3217` | `133` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-10-11 03:40 МСК` | `237` | `228` | `20` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-10-11 02:10 МСК` | `3157` | `3009` | `124` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-10-10 08:32 МСК` | `3628` | `3443` | `128` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-17 13:30 МСК` | `31` | `30` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `196` | `5` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `48` | `0` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

### Специализированные источники

| Источник | Область | Обновление источника | В LAN 5K | Ссылка |
|----------|---------|---------------------|----------|--------|
| VestraNet Nodes protocols/vless.txt | только LAN | `2026-10-11 08:26 МСК` | `1335` | [raw](https://raw.githubusercontent.com/MustafaBaqer/VestraNet-Nodes/main/protocols/vless.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `9363` | `9708` | `+345` |
| Россия | `↓` | `2689` | `2649` | `-40` |
| Global | `↑` | `6674` | `7059` | `+385` |
| Global 5K | `↑` | `1761` | `2227` | `+466` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-10-11 08:32:55 МСК` | `9708` | `2649` | `7059` | `2227` | `+380` | `+30` | `+350` | `+390` |
| `2026-10-11 00:09:30 МСК` | `9328` | `2619` | `6709` | `1837` | `+302` | `-1` | `+303` | `+62` |
| `2026-10-10 14:54:53 МСК` | `9026` | `2620` | `6406` | `1775` | `-304` | `+43` | `-347` | `+63` |
| `2026-10-10 01:18:04 МСК` | `9330` | `2577` | `6753` | `1712` | `+291` | `+33` | `+258` | `-36` |
| `2026-10-09 15:34:28 МСК` | `9039` | `2544` | `6495` | `1748` | `-26` | `+18` | `-44` | `+124` |
| `2026-10-09 01:53:26 МСК` | `9065` | `2526` | `6539` | `1624` | `+274` | `+35` | `+239` | `-33` |
| `2026-10-08 15:48:11 МСК` | `8791` | `2491` | `6300` | `1657` | `-56` | `-164` | `+108` | `+40` |
| `2026-10-08 01:41:07 МСК` | `8847` | `2655` | `6192` | `1617` | `+105` | `+12` | `+93` | `-29` |
| `2026-10-07 15:39:02 МСК` | `8742` | `2643` | `6099` | `1646` | `-621` | `-46` | `-575` | `-115` |
| `2026-10-07 01:20:52 МСК` | `9363` | `2689` | `6674` | `1761` | `+257` | `-20` | `+277` | `+98` |

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
