# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-9973-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-10-12 17:22:30 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Все иностранные non-RU серверы из общей подписки | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |
| **pale-signal подписка - Global 5K** | До 5000 самых свежих иностранных БС/whitelist/bypass серверов | https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml | [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) |
| **pale-signal подписка - LAN 5K** | До 5000 иностранных узлов для проводного интернета; без БС/whitelist/mobile/CIDR-пулов | https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml | [subscription-lan-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml) |
| **pale-signal подписка - LAN Global** | Все доступные иностранные узлы из тех же LAN-пулов, без лимита 5000 | https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml | [subscription-lan-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml) |
| **pale-signal подписка - LAN Experimental** | Только новые non-RU узлы из независимых экспериментальных источников; без пересечений с LAN Global | https://markkikhtenko.github.io/pale-signal/subscription-lan-experimental.yaml | [subscription-lan-experimental.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-experimental.yaml) |
| **pale-signal подписка - Global Non-Stable** | Тестовая Global 5K: полный MANUAL, AUTO без дублей endpoint | https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml | [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) |
| **pale-signal подписка - BS Safe** | До 2500 свежих Reality-узлов из БС-источников; AUTO ограничен 50 нодами | https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml | [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `9973` |
| Россия | `2980` |
| Global | `6993` |
| Global 5K | `2540` |
| LAN 5K | `5000` |
| LAN Global | `5635` |
| LAN Experimental | `1463` |
| LAN Experimental AUTO | `1463` |
| Исключено пересечений Experimental с LAN Global | `361` |
| LAN 5K из VestraNet | `1383` |
| Global Non-Stable MANUAL | `2540` |
| Global Non-Stable AUTO | `1846` |
| BS Safe MANUAL | `2289` |
| BS Safe AUTO | `50` |
| BS Safe из all_subs | `429` |
| BS Safe TCP / gRPC / XHTTP | `1868` / `234` / `187` |
| Unknown | `329` |
| Reality | `5981` |
| TLS | `8752` |
| TCP | `5883` |
| WebSocket | `2446` |
| gRPC | `808` |
| XHTTP | `836` |

Для OpenClash при активных блокировках используйте `BS Safe`: в `MANUAL` доступно до 2500 Reality-узлов из базовых LTE/whitelist/bypass-источников, включая `all_subs`, а `AUTO` проверяет только 50, чтобы не перегружать роутер.

Для обычного домашнего или офисного проводного подключения используйте `LAN 5K` или полную `LAN Global`. Обе подписки используют одинаковые LAN-пулы и исключают узлы, специально собранные под белые списки и CIDR-ограничения мобильных операторов; `LAN Global` отличается только отсутствием лимита 5000.

<!-- LAN-EXPERIMENTAL:START -->
## LAN Experimental

`LAN Experimental` собирается только из отдельного набора источников, исключает RU, `UNKNOWN`, непубличные адреса, заблокированные конфигурации, нормализованные дубли и совпадения `server + port + UUID` внутри Experimental и с актуальным `LAN Global`. Ни один экспериментальный источник не входит в рабочие группы источников.

| Источник | URL | Обновление источника | Получено VLESS | Прошло формат | Отфильтровано | Дубли Experimental | Совпало с LAN Global | Добавлено новых |
|----------|-----|---------------------|-----------------|----------------|----------------|---------------------|----------------------|-----------------|
| MorpheusAdam Best | [raw](https://raw.githubusercontent.com/morpheusadam/v2ray-config/main/subs/bundles/best.txt) | `2026-10-11 21:27 МСК` | `1610` | `1517` | `86` | `0` | `44` | `1387` |
| Mehrtat VLESS | [raw](https://raw.githubusercontent.com/mehrtat/vless-collector/main/vless.txt) | `2026-10-12 19:19 МСК` | `299` | `297` | `22` | `4` | `254` | `17` |
| Au1rxx Verified | [raw](https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/main/output/v2ray-base64.txt) | `2026-10-12 19:04 МСК` | `826` | `810` | `0` | `688` | `63` | `59` |

Всего серверов: `1463`. В `AUTO`: `1463` (весь набор без лимита). Исключено дублей внутри Experimental: `692`. Новые узлы источников учитываются по первому появлению в порядке таблицы; повторы последующих источников отражаются как дубли.

`AUTO` — обычная группа Mihomo [`url-test`](https://wiki.metacubex.one/ru/config/proxy-groups/url-test/) с `interval: 900`, `tolerance: 100`, `lazy: true`. Все узлы входят в группу, однако согласно [документации общих полей групп](https://wiki.metacubex.one/ru/config/proxy-groups/) `lazy: true` отключает проверки, пока группа не выбрана. После активации Mihomo проверяет задержку с заданным интервалом и выбирает доступный узел с учётом tolerance; это не гарантирует мгновенное переключение при каждом обрыве.

На NanoPi R3S большой полный `AUTO` может заметно расходовать CPU, RAM, таблицу соединений и канал во время циклов health-check. Подписка не подключается к OpenClash автоматически; оцените нагрузку на своём размере списка перед постоянным использованием.
<!-- LAN-EXPERIMENTAL:END -->
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
| solovyov-jenya2004 all_subs final_sorted | `2026-10-12 17:15 МСК` | `1145` | `745` | `745` | [raw](https://raw.githubusercontent.com/solovyov-jenya2004/all_subs/main/final_sorted) |
| rjsxrd bypass-all | `2026-10-12 17:03 МСК` | `1636` | `1189` | `1188` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| igareck WHITE-SNI-RU-all.txt | `2026-10-12 16:59 МСК` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `2026-10-12 16:59 МСК` | `8` | `0` | `0` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck WHITE-CIDR-RU-all.txt | `2026-10-12 16:59 МСК` | `82` | `35` | `35` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `2026-10-12 16:59 МСК` | `82` | `35` | `35` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| zieng2 vless_lite.txt | `2026-10-12 16:59 МСК` | `73` | `58` | `58` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| zieng2 vless_universal.txt | `2026-10-12 16:59 МСК` | `73` | `58` | `58` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| etoneya whitelist | `2026-10-12 16:48 МСК` | `196` | `65` | `65` | [raw](https://etoneya.su/whitelist) |
| vladvarp Prometheus WhiteList/vless.txt | `2026-10-12 15:06 МСК` | `139` | `87` | `87` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2026-10-12 13:07 МСК` | `596` | `242` | `242` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| AetrisVPN whitelist pool | `2026-10-12 12:55 МСК` | `407` | `317` | `317` | [raw](https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `2026-10-12 11:57 МСК` | `91` | `43` | `43` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `2026-10-12 10:07 МСК` | `115` | `1` | `1` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_all.txt | `2026-10-12 09:54 МСК` | `507` | `107` | `107` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| wlrus wl.txt | `2026-10-12 08:14 МСК` | `1580` | `283` | `283` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
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
| 0xRadikal light/configs.txt | `2026-10-12 17:07 МСК` | `486` | `466` | `66` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| SoliSpirit Protocols/vless.txt | `2026-10-12 17:06 МСК` | `4035` | `3831` | `214` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `2026-10-12 16:49 МСК` | `394` | `374` | `46` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2026-10-12 12:54 МСК` | `3371` | `3209` | `178` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| barry-far V2ray-config vless.txt | `2026-10-12 12:39 МСК` | `3407` | `3229` | `182` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| MatinGhanbari filtered vless.txt | `2026-10-12 11:34 МСК` | `241` | `228` | `32` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| Surfboardv2ray TGParse mixed | `2026-10-12 09:54 МСК` | `3206` | `3040` | `172` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| liMilCo v2r pro/vless.txt | `2026-10-12 08:38 МСК` | `3548` | `3367` | `220` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| MahanKenway configs/vless.txt | `2026-10-12 07:54 МСК` | `144` | `138` | `10` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| Rayan-Config proxy.txt | `2026-08-17 13:30 МСК` | `31` | `30` | `0` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| V2RayRoot Config/vless.txt | `2026-07-05 07:39 МСК` | `201` | `197` | `6` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| FNET00 Config/Main | `2026-01-30 01:58 МСК` | `50` | `48` | `1` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| MahsaNetConfigTopic xray_final.txt | `-` | `0` | `0` | `0` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |

### Специализированные источники

| Источник | Область | Обновление источника | В LAN 5K | Ссылка |
|----------|---------|---------------------|----------|--------|
| VestraNet Nodes protocols/vless.txt | только LAN | `2026-10-12 17:11 МСК` | `1383` | [raw](https://raw.githubusercontent.com/MustafaBaqer/VestraNet-Nodes/main/protocols/vless.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `9328` | `9973` | `+645` |
| Россия | `↑` | `2619` | `2980` | `+361` |
| Global | `↑` | `6709` | `6993` | `+284` |
| Global 5K | `↑` | `1837` | `2540` | `+703` |

| Обновление, МСК | Общая | Россия | Global | Global 5K | Δ общая | Δ Россия | Δ Global | Δ Global 5K |
|-----------------|-------|--------|--------|------------|---------|----------|----------|--------------|
| `2026-10-12 17:22:30 МСК` | `9973` | `2980` | `6993` | `2540` | `+8` | `+70` | `-62` | `+17` |
| `2026-10-12 12:59:42 МСК` | `9965` | `2910` | `7055` | `2523` | `0` | `-8` | `+8` | `+16` |
| `2026-10-12 12:38:24 МСК` | `9965` | `2918` | `7047` | `2507` | `+56` | `+23` | `+33` | `+30` |
| `2026-10-12 11:34:46 МСК` | `9909` | `2895` | `7014` | `2477` | `+480` | `+110` | `+370` | `+668` |
| `2026-10-12 00:34:33 МСК` | `9429` | `2785` | `6644` | `1809` | `+179` | `+67` | `+112` | `+44` |
| `2026-10-11 22:17:26 МСК` | `9250` | `2718` | `6532` | `1765` | `+1` | `+17` | `-16` | `-19` |
| `2026-10-11 22:04:23 МСК` | `9249` | `2701` | `6548` | `1784` | `+1524` | `+1284` | `+240` | `+102` |
| `2026-10-11 15:07:17 МСК` | `7725` | `1417` | `6308` | `1682` | `-1983` | `-1232` | `-751` | `-545` |
| `2026-10-11 08:32:55 МСК` | `9708` | `2649` | `7059` | `2227` | `+380` | `+30` | `+350` | `+390` |
| `2026-10-11 00:09:30 МСК` | `9328` | `2619` | `6709` | `1837` | `+302` | `-1` | `+303` | `+62` |

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
