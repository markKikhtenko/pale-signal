# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12513-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-08-11 22:01:41 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 самых свежих иностранных БС/whitelist/bypass серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |
| **pale-signal подписка - Global Non-Stable** | Тестовая Global 5K: полный MANUAL, AUTO без дублей endpoint | https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml | [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12513` |
| Россия | `3590` |
| Global | `8923` |
| Global 5K | `4585` |
| Global Non-Stable MANUAL | `4585` |
| Global Non-Stable AUTO | `3939` |
| Unknown | `403` |
| Reality | `8491` |
| TLS | `10755` |
| TCP | `8551` |
| WebSocket | `2487` |
| gRPC | `701` |
| XHTTP | `774` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

`subscription-global-non-stable.yaml` использует тот же полный список, что и Global 5K. В `MANUAL` остаются все узлы, а только в `AUTO` одинаковые endpoint объединяются до первой ноды.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из всех источников и остаётся полным большим global-списком.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| igareck WHITE-CIDR-RU-all.txt | `2026-08-11 21:53 МСК` | `23` | `11` | `11` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-08-11 21:53 МСК` | `5` | `5` | `5` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-08-11 21:53 МСК` | `11` | `0` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-08-11 21:53 МСК` | `37` | `16` | `16` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-08-11 21:32 МСК` | `1662` | `1662` | `1662` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| EtoNeYaProject GitHub whitelist | `2026-08-11 21:27 МСК` | `334` | `312` | `312` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| AvenCores 26_urls.json | `2026-08-11 21:26 МСК` | `2859` | `966` | `966` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| etoneya whitelist | `2026-08-11 21:26 МСК` | `334` | `312` | `312` | [raw](https://etoneya.su/whitelist) |
| AvenCores githubmirror/26.txt | `2026-08-11 21:16 МСК` | `4569` | `2643` | `2579` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| rjsxrd bypass-all | `2026-08-11 21:12 МСК` | `204` | `185` | `185` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-08-11 21:09 МСК` | `1363` | `751` | `751` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| zieng2 vless_lite.txt | `2026-08-11 20:59 МСК` | `298` | `227` | `227` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-08-11 20:59 МСК` | `298` | `227` | `227` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| wlunlocker whitelist_all.txt | `2026-08-11 20:59 МСК` | `484` | `92` | `92` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-08-11 20:02 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-08-11 20:01 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-08-11 19:34 МСК` | `102` | `71` | `71` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| wlrus wl.txt | `2026-08-11 18:07 МСК` | `1584` | `272` | `272` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
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
| 0xRadikal light/configs.txt | `2026-08-11 21:51 МСК` | `904` | `780` | `109` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| Rayan-Config proxy.txt | `2026-08-11 21:49 МСК` | `50` | `49` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-08-11 21:37 МСК` | `333` | `313` | `50` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| barry-far V2ray-config vless.txt | `2026-08-11 21:13 МСК` | `2857` | `2743` | `203` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| SoliSpirit Protocols/vless.txt | `2026-08-11 21:06 МСК` | `3557` | `3416` | `257` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-08-11 20:59 МСК` | `2835` | `2718` | `198` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-08-11 20:56 МСК` | `2639` | `2535` | `190` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| MahanKenway configs/vless.txt | `2026-08-11 20:02 МСК` | `131` | `128` | `17` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-08-11 19:56 МСК` | `198` | `187` | `25` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| liMilCo v2r pro/vless.txt | `2026-08-11 05:14 МСК` | `2996` | `2851` | `192` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | `18` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `1` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `12550` | `12513` | `-37` |
| Россия | `↑` | `3569` | `3590` | `+21` |
| Global | `↓` | `8981` | `8923` | `-58` |
| Global 5K | `↓` | `4638` | `4585` | `-53` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-08-11 22:01:41 МСК` | `12513` | `3590` | `8923` | `4585` | `+264` | `-59` | `+323` | `-23` |
| `2026-08-11 10:03:25 МСК` | `12249` | `3649` | `8600` | `4608` | `-949` | `+5` | `-954` | `-392` |
| `2026-08-10 21:56:34 МСК` | `13198` | `3644` | `9554` | `5000` | `+367` | `+32` | `+335` | `+39` |
| `2026-08-10 10:28:09 МСК` | `12831` | `3612` | `9219` | `4961` | `-114` | `-99` | `-15` | `+273` |
| `2026-08-09 21:38:52 МСК` | `12945` | `3711` | `9234` | `4688` | `+216` | `+59` | `+157` | `-139` |
| `2026-08-09 09:53:08 МСК` | `12729` | `3652` | `9077` | `4827` | `-300` | `+25` | `-325` | `+73` |
| `2026-08-08 21:35:17 МСК` | `13029` | `3627` | `9402` | `4754` | `-93` | `-52` | `-41` | `-246` |
| `2026-08-08 09:49:23 МСК` | `13122` | `3679` | `9443` | `5000` | `-225` | `+75` | `-300` | `+30` |
| `2026-08-07 21:54:27 МСК` | `13347` | `3604` | `9743` | `4970` | `+797` | `+35` | `+762` | `+332` |
| `2026-08-07 10:13:17 МСК` | `12550` | `3569` | `8981` | `4638` | `-341` | `-17` | `-324` | `-198` |

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
