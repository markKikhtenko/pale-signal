# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12065-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-21 00:04:11 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Остальные страны и `[UNKNOWN]` | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12065` |
| Россия | `3150` |
| Global | `8915` |
| Unknown | `2641` |
| Reality | `7857` |
| TLS | `10477` |
| TCP | `8035` |
| WebSocket | `2582` |
| gRPC | `782` |
| XHTTP | `666` |

<details>
<summary>Источники</summary>

Источники разделены по назначению. БС-группа - это whitelist/bypass/26/CIDR/SNI-источники. Общие global-пулы оставлены как запас иностранных VLESS, но не считаются проверенными под обход БС.

### БС / whitelist / bypass

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| AvenCores githubmirror/26.txt | `4086` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| AvenCores 26_urls.json | `2871` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| V.O.I.D VPN Bypass url_work.txt | `2867` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| wlrus wl.txt | `1656` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| rjsxrd bypass-all | `947` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| ByeWhiteLists2 | `633` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| wlunlocker whitelist_all.txt | `532` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| etoneya whitelist | `389` | [raw](https://etoneya.su/whitelist) |
| zieng2 vless_universal.txt | `305` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| zieng2 vless_lite.txt | `305` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `160` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `119` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `115` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `91` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `90` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| igareck WHITE-CIDR-RU-all.txt | `90` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| RKP bypass whitelist.txt | `81` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `44` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| igareck WHITE-SNI-RU-all.txt | `20` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `18` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |

### Общие global-пулы

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| SoliSpirit Protocols/vless.txt | `3480` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| liMilCo v2r pro/vless.txt | `2653` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2532` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| barry-far V2ray-config vless.txt | `2483` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2068` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| 0xRadikal light/configs.txt | `410` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `409` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| MatinGhanbari filtered vless.txt | `303` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| V2RayRoot Config/vless.txt | `201` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| MahsaNetConfigTopic xray_final.txt | `181` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |
| MahanKenway configs/vless.txt | `155` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| FNET00 Config/Main | `50` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |
| Rayan-Config proxy.txt | `45` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `13980` | `12065` | `-1915` |
| Россия | `↓` | `3574` | `3150` | `-424` |
| Global | `↓` | `10406` | `8915` | `-1491` |

| Обновление, МСК | Общая | Россия | Global | Δ общая | Δ Россия | Δ Global |
|-----------------|-------|--------|--------|---------|----------|----------|
| `2026-07-21 00:04:11 МСК` | `12065` | `3150` | `8915` | `-783` | `-278` | `-505` |
| `2026-07-20 22:45:47 МСК` | `12848` | `3428` | `9420` | `+30` | `-6` | `+36` |
| `2026-07-20 22:28:30 МСК` | `12818` | `3434` | `9384` | `-153` | `-986` | `+833` |
| `2026-07-20 21:20:46 МСК` | `12971` | `4420` | `8551` | `-1312` | `+1323` | `-2635` |
| `2026-07-20 18:50:51 МСК` | `14283` | `3097` | `11186` | `+638` | `-682` | `+1320` |
| `2026-07-20 16:50:08 МСК` | `13645` | `3779` | `9866` | `-340` | `-109` | `-231` |
| `2026-07-20 14:39:50 МСК` | `13985` | `3888` | `10097` | `+189` | `+339` | `-150` |
| `2026-07-20 11:42:46 МСК` | `13796` | `3549` | `10247` | `-184` | `-28` | `-156` |
| `2026-07-20 09:32:50 МСК` | `13980` | `3577` | `10403` | `0` | `+3` | `-3` |
| `2026-07-20 09:22:39 МСК` | `13980` | `3574` | `10406` | `+86` | `-18` | `+104` |

</details>

## Группы

Во всех трех подписках оставлены только группы `AUTO`, `MANUAL` и `PROXY`.

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
- Узлы без определенной страны попадают в `subscription-global.yaml` и получают `[UNKNOWN]` в имени.

## Обновление

GitHub Actions пересобирает подписки раз в час. Ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.

Если часть источников не скачалась, она пропускается. Если серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
