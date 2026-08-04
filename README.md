# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-13113-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-08-04 11:35:33 МСК`

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
| Всего серверов | `13113` |
| Россия | `3661` |
| Global | `9452` |
| Global 5K | `5000` |
| Global Non-Stable MANUAL | `5000` |
| Global Non-Stable AUTO | `4079` |
| Unknown | `338` |
| Reality | `8608` |
| TLS | `11278` |
| TCP | `8638` |
| WebSocket | `2787` |
| gRPC | `827` |
| XHTTP | `861` |

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
| rjsxrd bypass-all | `2026-08-04 11:13 МСК` | `374` | `338` | `338` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-08-04 11:07 МСК` | `1680` | `1680` | `1680` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| zieng2 vless_lite.txt | `2026-08-04 10:59 МСК` | `325` | `270` | `270` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-08-04 10:59 МСК` | `325` | `270` | `270` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-08-04 10:55 МСК` | `2020` | `1187` | `1187` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-08-04 10:35 МСК` | `58` | `41` | `41` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-08-04 10:35 МСК` | `33` | `25` | `25` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-08-04 10:35 МСК` | `4` | `4` | `4` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-08-04 10:35 МСК` | `58` | `41` | `41` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| AvenCores githubmirror/26.txt | `2026-08-04 09:49 МСК` | `4473` | `2616` | `2549` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-08-04 09:33 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| AvenCores 26_urls.json | `2026-08-04 09:31 МСК` | `3242` | `1341` | `1341` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-08-04 09:31 МСК` | `1639` | `341` | `341` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-08-04 08:54 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_all.txt | `2026-08-04 01:05 МСК` | `512` | `109` | `109` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-08-03 23:45 МСК` | `161` | `158` | `129` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `2026-08-03 21:58 МСК` | `19` | `18` | `3` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| etoneya whitelist | `2026-08-03 17:52 МСК` | `628` | `572` | `572` | [raw](https://etoneya.su/whitelist) |
| EtoNeYaProject GitHub whitelist | `2026-08-03 17:48 МСК` | `628` | `572` | `572` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `5` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `2026-06-20 04:56 МСК` | `27` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `2026-06-20 04:56 МСК` | `5` | `5` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `0` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `0` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| 0xRadikal light/configs.txt | `2026-08-04 11:13 МСК` | `1144` | `1054` | `130` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-08-04 11:11 МСК` | `365` | `355` | `26` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| SoliSpirit Protocols/vless.txt | `2026-08-04 11:07 МСК` | `3417` | `3306` | `221` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-04 10:31 МСК` | `53` | `52` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| MahanKenway configs/vless.txt | `2026-08-04 09:33 МСК` | `141` | `137` | `15` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-08-04 09:31 МСК` | `2577` | `2480` | `202` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-08-04 09:25 МСК` | `219` | `211` | `19` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-08-04 09:24 МСК` | `2630` | `2542` | `203` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-08-04 07:09 МСК` | `2378` | `2297` | `168` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-08-04 06:24 МСК` | `2760` | `2664` | `219` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `199` | `194` | `16` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `0` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `13646` | `13113` | `-533` |
| Россия | `↓` | `3677` | `3661` | `-16` |
| Global | `↓` | `9969` | `9452` | `-517` |
| Global 5K | `→` | `5000` | `5000` | `0` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-08-04 11:35:33 МСК` | `13113` | `3661` | `9452` | `5000` | `-303` | `-94` | `-209` | `0` |
| `2026-08-03 22:30:45 МСК` | `13416` | `3755` | `9661` | `5000` | `+212` | `-73` | `+285` | `0` |
| `2026-08-03 12:41:15 МСК` | `13204` | `3828` | `9376` | `5000` | `-30` | `+138` | `-168` | `0` |
| `2026-08-02 22:57:36 МСК` | `13234` | `3690` | `9544` | `5000` | `-21` | `-10` | `-11` | `0` |
| `2026-08-02 22:46:42 МСК` | `13255` | `3700` | `9555` | `5000` | `-17` | `+26` | `-43` | `0` |
| `2026-08-02 22:10:12 МСК` | `13272` | `3674` | `9598` | `5000` | `+132` | `-41` | `+173` | `0` |
| `2026-08-02 21:00:24 МСК` | `13140` | `3715` | `9425` | `5000` | `-47` | `-1` | `-46` | `0` |
| `2026-08-02 20:54:07 МСК` | `13187` | `3716` | `9471` | `5000` | `-338` | `-17` | `-321` | `0` |
| `2026-08-02 18:12:49 МСК` | `13525` | `3733` | `9792` | `5000` | `-121` | `+56` | `-177` | `0` |
| `2026-08-02 18:04:56 МСК` | `13646` | `3677` | `9969` | `5000` | `-169` | `-90` | `-79` | `0` |

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
