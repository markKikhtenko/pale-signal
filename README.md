# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-13140-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-08-02 21:00:24 МСК`

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
| Всего серверов | `13140` |
| Россия | `3715` |
| Global | `9425` |
| Global 5K | `5000` |
| Unknown | `381` |
| Reality | `8728` |
| TLS | `11371` |
| TCP | `8797` |
| WebSocket | `2713` |
| gRPC | `790` |
| XHTTP | `840` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из всех источников и остаётся полным большим global-списком.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| igareck WHITE-CIDR-RU-all.txt | `2026-08-02 20:51 МСК` | `74` | `42` | `42` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-08-02 20:51 МСК` | `8` | `8` | `8` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-08-02 20:51 МСК` | `22` | `8` | `8` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-08-02 20:51 МСК` | `74` | `42` | `42` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| AvenCores githubmirror/26.txt | `2026-08-02 20:37 МСК` | `4497` | `2594` | `2526` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-08-02 20:29 МСК` | `1728` | `1725` | `1725` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-08-02 20:11 МСК` | `2343` | `1476` | `1476` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| AvenCores 26_urls.json | `2026-08-02 20:05 МСК` | `3024` | `1109` | `1109` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-08-02 20:05 МСК` | `1606` | `293` | `293` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| zieng2 vless_lite.txt | `2026-08-02 19:59 МСК` | `244` | `187` | `187` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-08-02 19:59 МСК` | `244` | `187` | `187` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| rjsxrd bypass-all | `2026-08-02 19:53 МСК` | `294` | `268` | `268` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| wlunlocker whitelist_all.txt | `2026-08-02 19:06 МСК` | `479` | `98` | `98` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-08-02 19:04 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-08-02 19:03 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-08-02 16:40 МСК` | `178` | `145` | `145` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| etoneya whitelist | `2026-08-02 13:39 МСК` | `583` | `516` | `516` | [raw](https://etoneya.su/whitelist) |
| EtoNeYaProject GitHub whitelist | `2026-08-02 13:36 МСК` | `583` | `516` | `516` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| PrinceVSFX Adapt-Configs White_list.txt | `2026-08-01 20:44 МСК` | `2` | `1` | `1` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `110` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `20` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `2026-06-20 04:56 МСК` | `27` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `2026-06-20 04:56 МСК` | `5` | `5` | `5` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `20` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `35` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `33` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| Epodonios Splitted-By-Protocol/vless.txt | `2026-08-02 20:54 МСК` | `2581` | `2502` | `332` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-02 20:54 МСК` | `54` | `53` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| 0xRadikal light/configs.txt | `2026-08-02 20:42 МСК` | `1311` | `1221` | `225` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-08-02 20:26 МСК` | `356` | `346` | `38` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| barry-far V2ray-config vless.txt | `2026-08-02 20:23 МСК` | `2580` | `2501` | `332` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| SoliSpirit Protocols/vless.txt | `2026-08-02 20:06 МСК` | `3372` | `3261` | `380` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| MahanKenway configs/vless.txt | `2026-08-02 20:05 МСК` | `151` | `148` | `22` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-08-02 19:56 МСК` | `236` | `228` | `23` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-08-02 19:04 МСК` | `2292` | `2219` | `305` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-08-02 06:38 МСК` | `2810` | `2714` | `234` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | `21` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `1` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `12547` | `13140` | `+593` |
| Россия | `↑` | `3652` | `3715` | `+63` |
| Global | `↑` | `8895` | `9425` | `+530` |
| Global 5K | `↑` | `4880` | `5000` | `+120` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-08-02 21:00:24 МСК` | `13140` | `3715` | `9425` | `5000` | `-47` | `-1` | `-46` | `0` |
| `2026-08-02 20:54:07 МСК` | `13187` | `3716` | `9471` | `5000` | `-338` | `-17` | `-321` | `0` |
| `2026-08-02 18:12:49 МСК` | `13525` | `3733` | `9792` | `5000` | `-121` | `+56` | `-177` | `0` |
| `2026-08-02 18:04:56 МСК` | `13646` | `3677` | `9969` | `5000` | `-169` | `-90` | `-79` | `0` |
| `2026-08-02 11:20:56 МСК` | `13815` | `3767` | `10048` | `5000` | `+625` | `-6` | `+631` | `0` |
| `2026-08-01 22:07:42 МСК` | `13190` | `3773` | `9417` | `5000` | `-142` | `-95` | `-47` | `0` |
| `2026-08-01 11:18:09 МСК` | `13332` | `3868` | `9464` | `5000` | `+31` | `-129` | `+160` | `+26` |
| `2026-07-31 22:23:51 МСК` | `13301` | `3997` | `9304` | `4974` | `+371` | `+199` | `+172` | `-26` |
| `2026-07-31 11:47:40 МСК` | `12930` | `3798` | `9132` | `5000` | `+383` | `+146` | `+237` | `+120` |
| `2026-07-30 22:23:36 МСК` | `12547` | `3652` | `8895` | `4880` | `-425` | `-292` | `-133` | `-120` |

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
