# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12847-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-08-12 15:33:43 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 самых свежих иностранных БС/whitelist/bypass серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |
| **pale-signal подписка - Global Non-Stable** | Тестовая Global 5K: полный MANUAL, AUTO без дублей endpoint | https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml | [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) |
| **pale-signal подписка - BS Safe** | До 2500 свежих Reality-узлов из БС-источников; AUTO ограничен 50 нодами | https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml | [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12847` |
| Россия | `3620` |
| Global | `9227` |
| Global 5K | `5000` |
| Global Non-Stable MANUAL | `5000` |
| Global Non-Stable AUTO | `4133` |
| BS Safe MANUAL | `2500` |
| BS Safe AUTO | `50` |
| BS Safe TCP / gRPC / XHTTP | `2050` / `308` / `142` |
| Unknown | `428` |
| Reality | `8741` |
| TLS | `11126` |
| TCP | `8713` |
| WebSocket | `2542` |
| gRPC | `783` |
| XHTTP | `809` |

Для OpenClash при активных блокировках используйте `BS Safe`: в `MANUAL` доступно до 2500 Reality-узлов, а `AUTO` проверяет только 50, чтобы не перегружать роутер.

Подписка собирает и фильтрует узлы, но не может гарантировать их работу у конкретного провайдера.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из всех источников и остаётся полным большим global-списком.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`RKP_BYPASS`, `AETRIS_BYPASS`, `AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| rjsxrd bypass-all | `2026-08-12 15:16 МСК` | `420` | `361` | `361` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| AvenCores githubmirror/26.txt | `2026-08-12 15:10 МСК` | `4587` | `2652` | `2581` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-08-12 15:03 МСК` | `1424` | `835` | `835` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-08-12 15:01 МСК` | `1667` | `1664` | `1664` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| zieng2 vless_lite.txt | `2026-08-12 14:59 МСК` | `276` | `205` | `205` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-08-12 14:59 МСК` | `276` | `205` | `205` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-08-12 14:52 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-08-12 14:51 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| AetrisVPN whitelist pool | `2026-08-12 14:37 МСК` | `599` | `501` | `501` | [raw](https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-08-12 14:25 МСК` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-08-12 14:25 МСК` | `15` | `15` | `15` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-08-12 14:25 МСК` | `28` | `15` | `15` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-08-12 14:25 МСК` | `28` | `15` | `15` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| AvenCores 26_urls.json | `2026-08-12 14:02 МСК` | `2871` | `984` | `983` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-08-12 14:02 МСК` | `1591` | `298` | `298` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_all.txt | `2026-08-12 11:13 МСК` | `470` | `88` | `88` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| RKPchannel whitelist.txt | `2026-08-12 11:08 МСК` | `26` | `17` | `17` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/refs/heads/main/whitelist.txt) |
| etoneya whitelist | `2026-08-11 22:36 МСК` | `376` | `339` | `338` | [raw](https://etoneya.su/whitelist) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-08-11 22:33 МСК` | `151` | `112` | `112` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| EtoNeYaProject GitHub whitelist | `2026-08-11 22:32 МСК` | `376` | `339` | `338` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `109` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `35` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `13` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| ALIILAPRO v2rayNG-Config sub.txt | `2026-08-12 15:26 МСК` | `261` | `248` | `47` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| 0xRadikal light/configs.txt | `2026-08-12 15:22 МСК` | `980` | `850` | `153` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| SoliSpirit Protocols/vless.txt | `2026-08-12 15:06 МСК` | `3544` | `3414` | `298` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-08-12 15:05 МСК` | `2852` | `2747` | `250` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-08-12 14:54 МСК` | `2621` | `2525` | `225` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-08-12 14:49 МСК` | `2845` | `2736` | `240` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-12 14:39 МСК` | `49` | `48` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| MahanKenway configs/vless.txt | `2026-08-12 14:05 МСК` | `142` | `140` | `17` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-08-12 13:59 МСК` | `204` | `193` | `30` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| liMilCo v2r pro/vless.txt | `2026-08-12 05:31 МСК` | `2814` | `2702` | `276` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `196` | `20` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `1` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `12567` | `12847` | `+280` |
| Россия | `↑` | `3601` | `3620` | `+19` |
| Global | `↑` | `8966` | `9227` | `+261` |
| Global 5K | `↑` | `4995` | `5000` | `+5` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-08-12 15:33:43 МСК` | `12847` | `3620` | `9227` | `5000` | `-47` | `-25` | `-22` | `0` |
| `2026-08-12 15:06:14 МСК` | `12894` | `3645` | `9249` | `5000` | `+164` | `-1` | `+165` | `+33` |
| `2026-08-12 14:57:23 МСК` | `12730` | `3646` | `9084` | `4967` | `-4` | `+8` | `-12` | `-24` |
| `2026-08-12 14:19:59 МСК` | `12734` | `3638` | `9096` | `4991` | `+27` | `+3` | `+24` | `+24` |
| `2026-08-12 14:11:56 МСК` | `12707` | `3635` | `9072` | `4967` | `+172` | `+46` | `+126` | `+7` |
| `2026-08-12 13:02:10 МСК` | `12535` | `3589` | `8946` | `4960` | `-30` | `-20` | `-10` | `-12` |
| `2026-08-12 12:43:58 МСК` | `12565` | `3609` | `8956` | `4972` | `-108` | `+8` | `-116` | `-28` |
| `2026-08-12 12:33:56 МСК` | `12673` | `3601` | `9072` | `5000` | `0` | `-7` | `+7` | `0` |
| `2026-08-12 12:26:02 МСК` | `12673` | `3608` | `9065` | `5000` | `+106` | `+7` | `+99` | `+5` |
| `2026-08-12 12:01:39 МСК` | `12567` | `3601` | `8966` | `4995` | `-47` | `-16` | `-31` | `-5` |

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
