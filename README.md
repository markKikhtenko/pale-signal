# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12736-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-08-12 11:15:26 МСК`

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
| Всего серверов | `12736` |
| Россия | `3683` |
| Global | `9053` |
| Global 5K | `5000` |
| Global Non-Stable MANUAL | `5000` |
| Global Non-Stable AUTO | `4104` |
| BS Safe MANUAL | `2500` |
| BS Safe AUTO | `50` |
| BS Safe TCP / gRPC / XHTTP | `2249` / `187` / `64` |
| Unknown | `419` |
| Reality | `8714` |
| TLS | `11038` |
| TCP | `8602` |
| WebSocket | `2477` |
| gRPC | `849` |
| XHTTP | `808` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

`subscription-global-non-stable.yaml` использует тот же полный список, что и Global 5K. В `MANUAL` остаются все узлы, а только в `AUTO` одинаковые endpoint объединяются до первой ноды.

`subscription-bs-safe.yaml` — большой резервный профиль для условий активной БС-фильтрации. В `MANUAL` попадают до 2500 свежих non-RU Reality-узлов только из помеченных bypass/whitelist-источников. Приоритет получают gRPC/XHTTP с fingerprint `firefox`, `edge`, `qq` или `android`; далее идут Reality/TCP и остальные варианты, причём стандартный порт `443` поднимается выше внутри каждого уровня. Ноды с `skip-cert-verify` исключаются. Повторы одного resolved IP + SNI удаляются независимо от порта, UUID и ключа; gRPC получает `max-connections: 1`, XHTTP — `reuse-settings.max-connections: 1`. Это фильтрация по метаданным, а не гарантия живости узла.

Чтобы OpenClash не создавал лавину TLS-проверок, группа `AUTO` содержит только первые 50 наиболее приоритетных gRPC/XHTTP-нод. Все остальные доступны исключительно через `MANUAL`.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из всех источников и остаётся полным большим global-списком.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`RKP_BYPASS`, `AETRIS_BYPASS`, `AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| RKPchannel whitelist.txt | `2026-08-12 11:08 МСК` | `26` | `18` | `18` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/refs/heads/main/whitelist.txt) |
| AetrisVPN whitelist pool | `2026-08-12 11:07 МСК` | `628` | `536` | `536` | [raw](https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt) |
| zieng2 vless_lite.txt | `2026-08-12 10:59 МСК` | `263` | `191` | `191` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-08-12 10:59 МСК` | `263` | `191` | `191` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-08-12 10:46 МСК` | `1676` | `1671` | `1671` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| AvenCores 26_urls.json | `2026-08-12 10:39 МСК` | `2904` | `1011` | `1010` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-08-12 10:39 МСК` | `1587` | `299` | `299` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-08-12 10:26 МСК` | `1586` | `972` | `972` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| rjsxrd bypass-all | `2026-08-12 10:22 МСК` | `285` | `257` | `257` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-08-12 10:08 МСК` | `67` | `47` | `47` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-08-12 10:08 МСК` | `11` | `11` | `11` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-08-12 10:08 МСК` | `16` | `12` | `12` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-08-12 10:08 МСК` | `67` | `47` | `47` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| AvenCores githubmirror/26.txt | `2026-08-12 10:02 МСК` | `4605` | `2656` | `2589` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-08-12 09:19 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-08-12 07:50 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_all.txt | `2026-08-12 04:38 МСК` | `526` | `90` | `90` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| etoneya whitelist | `2026-08-11 22:36 МСК` | `376` | `339` | `338` | [raw](https://etoneya.su/whitelist) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-08-11 22:33 МСК` | `146` | `105` | `105` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| EtoNeYaProject GitHub whitelist | `2026-08-11 22:32 МСК` | `376` | `339` | `338` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `110` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `35` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `49` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| 0xRadikal light/configs.txt | `2026-08-12 11:06 МСК` | `1055` | `921` | `186` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| SoliSpirit Protocols/vless.txt | `2026-08-12 11:06 МСК` | `3574` | `3442` | `293` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-08-12 10:49 МСК` | `335` | `316` | `60` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| MahanKenway configs/vless.txt | `2026-08-12 10:30 МСК` | `135` | `132` | `16` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-08-12 10:27 МСК` | `2861` | `2759` | `235` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-08-12 10:20 МСК` | `208` | `196` | `46` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-12 10:09 МСК` | `53` | `52` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-08-12 09:16 МСК` | `2811` | `2707` | `236` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-08-12 09:10 МСК` | `2629` | `2536` | `205` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-08-12 05:31 МСК` | `2809` | `2695` | `260` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `200` | `195` | `20` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `1` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `13029` | `12736` | `-293` |
| Россия | `↑` | `3627` | `3683` | `+56` |
| Global | `↓` | `9402` | `9053` | `-349` |
| Global 5K | `↑` | `4754` | `5000` | `+246` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-08-12 11:15:26 МСК` | `12736` | `3683` | `9053` | `5000` | `+324` | `+25` | `+299` | `+255` |
| `2026-08-12 10:23:00 МСК` | `12412` | `3658` | `8754` | `4745` | `+4` | `-14` | `+18` | `-17` |
| `2026-08-12 09:37:13 МСК` | `12408` | `3672` | `8736` | `4762` | `-105` | `+82` | `-187` | `+177` |
| `2026-08-11 22:01:41 МСК` | `12513` | `3590` | `8923` | `4585` | `+264` | `-59` | `+323` | `-23` |
| `2026-08-11 10:03:25 МСК` | `12249` | `3649` | `8600` | `4608` | `-949` | `+5` | `-954` | `-392` |
| `2026-08-10 21:56:34 МСК` | `13198` | `3644` | `9554` | `5000` | `+367` | `+32` | `+335` | `+39` |
| `2026-08-10 10:28:09 МСК` | `12831` | `3612` | `9219` | `4961` | `-114` | `-99` | `-15` | `+273` |
| `2026-08-09 21:38:52 МСК` | `12945` | `3711` | `9234` | `4688` | `+216` | `+59` | `+157` | `-139` |
| `2026-08-09 09:53:08 МСК` | `12729` | `3652` | `9077` | `4827` | `-300` | `+25` | `-325` | `+73` |
| `2026-08-08 21:35:17 МСК` | `13029` | `3627` | `9402` | `4754` | `-93` | `-52` | `-41` | `-246` |

</details>

## Группы

Во всех подписках оставлены только группы `AUTO`, `MANUAL` и `PROXY`.

| Группа | Тип | Назначение |
|--------|-----|------------|
| `AUTO` | `url-test` | Автовыбор серверов через URL Test |
| `MANUAL` | `select` | Ручной выбор сервера |
| `PROXY` | `select` | Главная группа для правила `MATCH,PROXY` |

Параметры `AUTO`: `interval: 900`, `tolerance: 100`, `lazy: true`.

В BS Safe группа `PROXY` по умолчанию направлена в `MANUAL`, а ленивый `AUTO` из максимум 50 нод запускается только при явном выборе и имеет `interval: 3600`. Для параметров ограничения соединений нужен Mihomo core v1.19.24 или новее.

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
