# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12547-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-30 22:23:36 МСК`

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
| Всего серверов | `12547` |
| Россия | `3652` |
| Global | `8895` |
| Global 5K | `4880` |
| Unknown | `372` |
| Reality | `8388` |
| TLS | `10830` |
| TCP | `8438` |
| WebSocket | `2565` |
| gRPC | `833` |
| XHTTP | `711` |

`subscription-global.yaml` каждый запуск собирается заново из всех non-RU серверов общей подписки без ограничения по количеству.

`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников. Проверка живости прокси в GitHub Actions отключена, чтобы GitHub не отбрасывал узлы, которые могут работать только из-под БС на роутере.

<details>
<summary>Источники</summary>

`subscription-global.yaml` берёт все non-RU узлы из всех источников и остаётся полным большим global-списком.
`subscription-global-5k.yaml` берёт до 5000 самых свежих узлов с подтверждённой страной не RU только из БС / whitelist / bypass источников (`AVEN_MIRROR_26`, `AVEN_26`, `VOID_URL_WORK`, `RJSXRD_BYPASS_ALL`, `WLUNLOCKER_WHITE_ALL`, `RKP_WHITELIST`, `WLRUS_WL`, `ETONEYA_WHITELIST`, `ETONEYA_GH_WHITELIST`, `BYEWL2`, `FULL`, `LITE`, `FLEXIYO_RUSSIA_WHITELIST`, `PROSEK_WHITELIST`, `SILENTGHOST_WHITELIST`, `VLADVARP_WHITELIST_VLESS`, `EPODONIOS_26`, `WLUNLOCKER_CIDR_2`, `WLUNLOCKER_CIDR_1`, `IGARECK_WHITE_CIDR`, `IGARECK_WHITE_SNI`, `IGARECK_WHITE_CIDR_CHECKED`, `IGARECK_WHITE_MOBILE_1`, `KIRILLO4KA_WHITE_CIDR`, `KIRILLO4KA_WHITE_SNI`, `KIRILLO4KA_WHITE_CIDR_CHECKED`, `KIRILLO4KA_WHITE_MOBILE`, `PRINCE_WHITE_LIST`). Проверок живости в GitHub Actions нет.

### Приоритетные БС / whitelist / bypass источники

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| AvenCores githubmirror/26.txt | `2026-07-30 22:05 МСК` | `4410` | `2577` | `2514` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| zieng2 vless_lite.txt | `2026-07-30 21:59 МСК` | `351` | `324` | `324` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-07-30 21:59 МСК` | `351` | `324` | `324` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-07-30 21:55 МСК` | `107` | `99` | `99` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-07-30 21:55 МСК` | `31` | `30` | `30` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-07-30 21:55 МСК` | `85` | `82` | `82` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-07-30 21:55 МСК` | `107` | `99` | `99` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-07-30 21:36 МСК` | `2402` | `1534` | `1534` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| rjsxrd bypass-all | `2026-07-30 21:31 МСК` | `488` | `442` | `442` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| FLEXIY0 matryoshka-vpn russia_whitelist.txt | `2026-07-30 21:25 МСК` | `1304` | `1298` | `1294` | [raw](https://raw.githubusercontent.com/FLEXIY0/matryoshka-vpn/main/configs/russia_whitelist.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-07-30 21:21 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-07-30 21:19 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-07-30 21:03 МСК` | `155` | `120` | `120` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| AvenCores 26_urls.json | `2026-07-30 20:41 МСК` | `3260` | `1371` | `1371` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `2026-07-30 20:41 МСК` | `1656` | `326` | `326` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| wlunlocker whitelist_all.txt | `2026-07-30 20:22 МСК` | `508` | `112` | `112` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| EtoNeYaProject GitHub whitelist | `2026-07-30 20:20 МСК` | `586` | `521` | `521` | [raw](https://raw.githubusercontent.com/EtoNeYaProject/etoneyaproject.github.io/refs/heads/main/whitelist) |
| etoneya whitelist | `2026-07-30 20:19 МСК` | `586` | `521` | `521` | [raw](https://etoneya.su/whitelist) |
| RKP bypass whitelist.txt | `2026-07-30 19:13 МСК` | `83` | `59` | `59` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `2026-07-30 16:01 МСК` | `22` | `14` | `14` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| Epodonios Sub26.txt | `2026-06-30 14:20 МСК` | `119` | `116` | `110` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-all.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `20` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-SNI-RU-all.txt | `2026-06-20 04:56 МСК` | `27` | `0` | `0` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-SNI-RU-all.txt) |
| Kirillo4ka eavevpn WHITE-CIDR-RU-checked.txt | `2026-06-20 04:56 МСК` | `5` | `5` | `5` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/WHITE-CIDR-RU-checked.txt) |
| Kirillo4ka eavevpn Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-06-20 04:56 МСК` | `20` | `20` | `20` | [raw](https://raw.githubusercontent.com/Kirillo4ka/eavevpn-configs/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| 55prosek vpn_config_for_russia whitelist.txt | `2026-04-06 02:25 МСК` | `46` | `35` | `35` | [raw](https://raw.githubusercontent.com/55prosek-lgtm/vpn_config_for_russia/refs/heads/main/whitelist.txt) |
| ByeWhiteLists2 | `2026-03-28 02:29 МСК` | `633` | `143` | `143` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| SilentGhostCodes WhiteListVpn Whitelist.txt | `2026-03-17 15:43 МСК` | `150` | `121` | `121` | [raw](https://raw.githubusercontent.com/SilentGhostCodes/WhiteListVpn/main/Whitelist.txt) |

### Остальные global-пулы

| Источник | Обновление источника | Серверов в общей подписке | В Global | В Global 5K | Ссылка |
|----------|---------------------|---------------------------|-----------|---------------|--------|
| 0xRadikal light/configs.txt | `2026-07-30 22:11 МСК` | `858` | `759` | `116` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| Rayan-Config proxy.txt | `2026-07-30 22:11 МСК` | `54` | `53` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-07-30 22:10 МСК` | `478` | `455` | `42` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| SoliSpirit Protocols/vless.txt | `2026-07-30 22:06 МСК` | `3332` | `3227` | `275` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-07-30 21:43 МСК` | `2460` | `2388` | `226` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-07-30 21:06 МСК` | `2476` | `2400` | `232` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| MahanKenway configs/vless.txt | `2026-07-30 20:40 МСК` | `146` | `141` | `22` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-07-30 20:24 МСК` | `323` | `310` | `27` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-07-30 20:22 МСК` | `2182` | `2117` | `191` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-07-30 05:56 МСК` | `2606` | `2533` | `231` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | `22` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `49` | `2` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `13543` | `12547` | `-996` |
| Россия | `↓` | `4402` | `3652` | `-750` |
| Global | `↓` | `9141` | `8895` | `-246` |
| Global 5K | `↓` | `5000` | `4880` | `-120` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-07-30 22:23:36 МСК` | `12547` | `3652` | `8895` | `4880` | `-425` | `-292` | `-133` | `-120` |
| `2026-07-30 11:22:51 МСК` | `12972` | `3944` | `9028` | `5000` | `+156` | `+209` | `-53` | `0` |
| `2026-07-29 22:13:14 МСК` | `12816` | `3735` | `9081` | `5000` | `-400` | `-348` | `-52` | `0` |
| `2026-07-29 11:38:33 МСК` | `13216` | `4083` | `9133` | `5000` | `-435` | `-344` | `-91` | `0` |
| `2026-07-28 22:23:10 МСК` | `13651` | `4427` | `9224` | `5000` | `+211` | `+47` | `+164` | `0` |
| `2026-07-28 15:42:53 МСК` | `13440` | `4380` | `9060` | `5000` | `0` | `-5` | `+5` | `0` |
| `2026-07-28 15:35:10 МСК` | `13440` | `4385` | `9055` | `5000` | `-5` | `-5` | `0` | `0` |
| `2026-07-28 15:28:53 МСК` | `13445` | `4390` | `9055` | `5000` | `-106` | `-11` | `-95` | `0` |
| `2026-07-28 12:01:58 МСК` | `13551` | `4401` | `9150` | `5000` | `+8` | `-1` | `+9` | `0` |
| `2026-07-28 11:37:41 МСК` | `13543` | `4402` | `9141` | `5000` | `0` | `-4` | `+4` | `0` |

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
