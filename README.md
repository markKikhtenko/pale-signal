# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12816-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-29 22:13:14 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 самых свежих иностранных БС/whitelist/bypass серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12816` |
| Россия | `3735` |
| Global | `9081` |
| Global 5K | `5000` |
| Unknown | `347` |
| Reality | `8558` |
| TLS | `11121` |
| TCP | `8497` |
| WebSocket | `2663` |
| gRPC | `916` |
| XHTTP | `740` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из всех источников и остаётся полным большим global-списком.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `RKP_WHITELIST`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| zieng2 vless_lite.txt | `2026-07-29 21:59 МСК` | `249` | `224` | `224` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-07-29 21:59 МСК` | `249` | `224` | `224` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| AvenCores githubmirror/26.txt | `2026-07-29 21:54 МСК` | `4374` | `2570` | `2510` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| EtoNeYaProject GitHub whitelist | `2026-07-29 21:47 МСК` | `631` | `538` | `538` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| AvenCores 26_urls.json | `2026-07-29 21:47 МСК` | `3220` | `1313` | `1313` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| etoneya whitelist | `2026-07-29 21:47 МСК` | `631` | `538` | `538` | [raw](https://etoneya.su/whitelist) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-07-29 21:43 МСК` | `1467` | `1460` | `1459` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| RKP bypass whitelist.txt | `2026-07-29 21:38 МСК` | `147` | `91` | `91` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-07-29 21:27 МСК` | `2425` | `1576` | `1576` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-07-29 21:23 МСК` | `95` | `74` | `74` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-07-29 21:23 МСК` | `45` | `42` | `42` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-07-29 21:23 МСК` | `9` | `6` | `6` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-07-29 21:23 МСК` | `95` | `74` | `74` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| rjsxrd bypass-all | `2026-07-29 21:20 МСК` | `584` | `528` | `528` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| wlunlocker whitelist_all.txt | `2026-07-29 21:03 МСК` | `510` | `119` | `119` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| wlrus wl.txt | `2026-07-29 20:21 МСК` | `1658` | `337` | `337` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-07-29 20:20 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-07-29 20:19 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `2026-07-29 13:54 МСК` | `17` | `14` | `14` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-07-25 18:48 МСК` | `177` | `137` | `137` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `110` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `20` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `2026-06-20 04:56 МСК` | `27` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `2026-06-20 04:56 МСК` | `5` | `5` | `5` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `20` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `35` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `27` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| SoliSpirit Protocols/vless.txt | `2026-07-29 22:06 МСК` | `3368` | `3270` | `284` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| Rayan-Config proxy.txt | `2026-07-29 21:59 МСК` | `51` | `50` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| 0xRadikal light/configs.txt | `2026-07-29 21:53 МСК` | `818` | `726` | `95` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-07-29 21:39 МСК` | `2536` | `2470` | `236` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-07-29 21:38 МСК` | `490` | `467` | `51` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| barry-far V2ray-config vless.txt | `2026-07-29 20:45 МСК` | `2530` | `2464` | `236` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| MahanKenway configs/vless.txt | `2026-07-29 20:20 МСК` | `155` | `151` | `16` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-07-29 20:13 МСК` | `341` | `322` | `34` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-07-29 20:11 МСК` | `2247` | `2188` | `204` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-07-29 06:23 МСК` | `2589` | `2507` | `225` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | `22` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `2` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `12992` | `12816` | `-176` |
| Россия | `↓` | `4412` | `3735` | `-677` |
| Global | `↑` | `5000` | `9081` | `+4081` |
| Global 5K | `→` | `5000` | `5000` | `0` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-07-29 22:13:14 МСК` | `12816` | `3735` | `9081` | `5000` | `-400` | `-348` | `-52` | `0` |
| `2026-07-29 11:38:33 МСК` | `13216` | `4083` | `9133` | `5000` | `-435` | `-344` | `-91` | `0` |
| `2026-07-28 22:23:10 МСК` | `13651` | `4427` | `9224` | `5000` | `+211` | `+47` | `+164` | `0` |
| `2026-07-28 15:42:53 МСК` | `13440` | `4380` | `9060` | `5000` | `0` | `-5` | `+5` | `0` |
| `2026-07-28 15:35:10 МСК` | `13440` | `4385` | `9055` | `5000` | `-5` | `-5` | `0` | `0` |
| `2026-07-28 15:28:53 МСК` | `13445` | `4390` | `9055` | `5000` | `-106` | `-11` | `-95` | `0` |
| `2026-07-28 12:01:58 МСК` | `13551` | `4401` | `9150` | `5000` | `+8` | `-1` | `+9` | `0` |
| `2026-07-28 11:37:41 МСК` | `13543` | `4402` | `9141` | `5000` | `0` | `-4` | `+4` | `0` |
| `2026-07-28 11:24:31 МСК` | `13543` | `4406` | `9137` | `5000` | `+551` | `-6` | `+4137` | `0` |
| `2026-07-28 11:06:03 МСК` | `12992` | `4412` | `5000` | `5000` | `+354` | `+7` | `-3233` | `0` |

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
