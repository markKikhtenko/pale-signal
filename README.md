# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12412-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-08-12 10:23:00 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 самых свежих иностранных БС/whitelist/bypass серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |
| **pale-signal подписка - Global Non-Stable** | Тестовая Global 5K: полный MANUAL, AUTO без дублей endpoint | https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml | [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) |
| **pale-signal подписка - BS Safe** | До 100 консервативных Reality gRPC/XHTTP узлов без повторов IP+SNI | https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml | [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12412` |
| Россия | `3658` |
| Global | `8754` |
| Global 5K | `4745` |
| Global Non-Stable MANUAL | `4745` |
| Global Non-Stable AUTO | `3988` |
| BS Safe | `100` |
| BS Safe gRPC / XHTTP | `75` / `25` |
| Unknown | `410` |
| Reality | `8442` |
| TLS | `10717` |
| TCP | `8367` |
| WebSocket | `2467` |
| gRPC | `823` |
| XHTTP | `755` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

`subscription-global-non-stable.yaml` использует тот же полный список, что и Global 5K. В `MANUAL` остаются все узлы, а только в `AUTO` одинаковые endpoint объединяются до первой ноды.

`subscription-bs-safe.yaml` — маленький консервативный профиль для условий активной БС-фильтрации. В него попадают только подтверждённые non-RU Reality-узлы из bypass/whitelist-источников с транспортом gRPC или XHTTP и явно заданным fingerprint `firefox`, `edge`, `qq` или `android`. Повторы одного resolved IP + SNI удаляются независимо от порта, UUID и ключа; gRPC получает `max-connections: 1`, XHTTP — `reuse-settings.max-connections: 1`. Это фильтрация по метаданным, а не гарантия живости узла.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из всех источников и остаётся полным большим global-списком.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| igareck WHITE-CIDR-RU-all.txt | `2026-08-12 10:08 МСК` | `67` | `49` | `49` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-08-12 10:08 МСК` | `12` | `12` | `12` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-08-12 10:08 МСК` | `16` | `12` | `12` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-08-12 10:08 МСК` | `67` | `49` | `49` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| AvenCores githubmirror/26.txt | `2026-08-12 10:02 МСК` | `4605` | `2651` | `2584` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| zieng2 vless_lite.txt | `2026-08-12 09:59 МСК` | `284` | `206` | `206` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-08-12 09:59 МСК` | `284` | `206` | `206` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| rjsxrd bypass-all | `2026-08-12 09:22 МСК` | `285` | `249` | `249` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-08-12 09:19 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-08-12 09:05 МСК` | `1658` | `1656` | `1656` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-08-12 08:46 МСК` | `1581` | `942` | `942` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| AvenCores 26_urls.json | `2026-08-12 08:40 МСК` | `2936` | `1033` | `1032` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-08-12 08:40 МСК` | `1599` | `306` | `306` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-08-12 07:50 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_all.txt | `2026-08-12 04:38 МСК` | `527` | `91` | `91` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| etoneya whitelist | `2026-08-11 22:36 МСК` | `376` | `338` | `337` | [raw](https://etoneya.su/whitelist) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-08-11 22:33 МСК` | `139` | `100` | `100` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| EtoNeYaProject GitHub whitelist | `2026-08-11 22:32 МСК` | `376` | `338` | `337` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `110` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `35` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `121` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| Rayan-Config proxy.txt | `2026-08-12 10:09 МСК` | `53` | `52` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| 0xRadikal light/configs.txt | `2026-08-12 10:07 МСК` | `1072` | `931` | `165` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| SoliSpirit Protocols/vless.txt | `2026-08-12 10:06 МСК` | `3564` | `3434` | `277` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-08-12 09:48 МСК` | `335` | `316` | `52` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-08-12 09:16 МСК` | `2807` | `2703` | `226` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-08-12 09:10 МСК` | `2626` | `2533` | `196` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| barry-far V2ray-config vless.txt | `2026-08-12 09:00 МСК` | `2813` | `2709` | `226` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| MahanKenway configs/vless.txt | `2026-08-12 08:42 МСК` | `131` | `128` | `19` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-08-12 07:05 МСК` | `201` | `187` | `31` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| liMilCo v2r pro/vless.txt | `2026-08-12 05:31 МСК` | `2800` | `2688` | `237` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `198` | `194` | `18` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `1` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `13122` | `12412` | `-710` |
| Россия | `↓` | `3679` | `3658` | `-21` |
| Global | `↓` | `9443` | `8754` | `-689` |
| Global 5K | `↓` | `5000` | `4745` | `-255` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-08-12 10:23:00 МСК` | `12412` | `3658` | `8754` | `4745` | `+4` | `-14` | `+18` | `-17` |
| `2026-08-12 09:37:13 МСК` | `12408` | `3672` | `8736` | `4762` | `-105` | `+82` | `-187` | `+177` |
| `2026-08-11 22:01:41 МСК` | `12513` | `3590` | `8923` | `4585` | `+264` | `-59` | `+323` | `-23` |
| `2026-08-11 10:03:25 МСК` | `12249` | `3649` | `8600` | `4608` | `-949` | `+5` | `-954` | `-392` |
| `2026-08-10 21:56:34 МСК` | `13198` | `3644` | `9554` | `5000` | `+367` | `+32` | `+335` | `+39` |
| `2026-08-10 10:28:09 МСК` | `12831` | `3612` | `9219` | `4961` | `-114` | `-99` | `-15` | `+273` |
| `2026-08-09 21:38:52 МСК` | `12945` | `3711` | `9234` | `4688` | `+216` | `+59` | `+157` | `-139` |
| `2026-08-09 09:53:08 МСК` | `12729` | `3652` | `9077` | `4827` | `-300` | `+25` | `-325` | `+73` |
| `2026-08-08 21:35:17 МСК` | `13029` | `3627` | `9402` | `4754` | `-93` | `-52` | `-41` | `-246` |
| `2026-08-08 09:49:23 МСК` | `13122` | `3679` | `9443` | `5000` | `-225` | `+75` | `-300` | `+30` |

</details>

## Группы

Во всех подписках оставлены только группы `AUTO`, `MANUAL` и `PROXY`.

| Группа | Тип | Назначение |
|--------|-----|------------|
| `AUTO` | `url-test` | Автовыбор серверов через URL Test |
| `MANUAL` | `select` | Ручной выбор сервера |
| `PROXY` | `select` | Главная группа для правила `MATCH,PROXY` |

Параметры `AUTO`: `interval: 900`, `tolerance: 100`, `lazy: true`.

В BS Safe группа `PROXY` по умолчанию направлена в `MANUAL`, а ленивый `AUTO` запускается только при явном выборе и имеет `interval: 3600`. Для параметров ограничения соединений нужен Mihomo core v1.19.24 или новее.

### BS Safe в OpenClash

1. В `Plugin Settings` → `Version Update` обновите **Meta Core** минимум до Mihomo v1.19.24 и выберите тип ядра `Meta`.
2. В `Config Subscription` добавьте прямой URL `subscription-bs-safe.yaml` как Clash/Mihomo-конфиг. Онлайн-конвертацию для этой ссылки включать не нужно.
3. Обновите подписку, активируйте полученный профиль и примените конфигурацию.
4. В Dashboard откройте группу `PROXY`: сначала оставьте `MANUAL` и проверьте ноды по одной. `AUTO` включайте только после появления рабочих нод — он намеренно не является выбором по умолчанию.

OpenClash использует файл как самостоятельный YAML-профиль и может добавить в него свои настройки DNS, TUN и перехвата трафика при применении шаблона/override. Отбор BS Safe меняет только список прокси и три policy group, не системные параметры OpenClash.

## Разделение по странам

- Сначала используется флаг или страна в имени узла.
- Если страны в имени нет, используется GeoIP фактического поля `server`.
- Если `server` является доменом, он сначала разрешается в IP.
- SNI, `servername`, `Host`, XHTTP host и gRPC service name не используются для определения страны.
- Узлы без определенной страны попадают в global-подписки и получают `[UNKNOWN]` в имени.

## Обновление

GitHub Actions запускает пересборку два раза в сутки: в 09:00 и 21:00 по МСК. В GitHub cron это `0 6,18 * * *`, потому что расписание задается в UTC. GitHub может задерживать scheduled-запуски; ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.

Если часть источников не скачалась, она пропускается. Если серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
