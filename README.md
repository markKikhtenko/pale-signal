# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12971-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-20 21:20:46 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Остальные страны и `[UNKNOWN]` | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12971` |
| Россия | `4420` |
| Global | `8551` |
| Unknown | `358` |
| Reality | `8594` |
| TLS | `11267` |
| TCP | `8808` |
| WebSocket | `2648` |
| gRPC | `799` |
| XHTTP | `716` |

<details>
<summary>Источники</summary>

Источники разделены по назначению. БС-группа - это whitelist/bypass/26/CIDR/SNI-источники. Общие global-пулы оставлены как запас иностранных VLESS, но не считаются проверенными под обход БС.

### БС / whitelist / bypass

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| AvenCores githubmirror/26.txt | `4097` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| V.O.I.D VPN Bypass url_work.txt | `3216` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| AvenCores 26_urls.json | `2814` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| rjsxrd bypass-all | `963` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| ByeWhiteLists2 | `633` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| wlunlocker whitelist_all.txt | `522` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| RKP bypass whitelist.txt | `359` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| zieng2 vless_universal.txt | `305` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| zieng2 vless_lite.txt | `305` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `134` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `119` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `115` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `91` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `81` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| igareck WHITE-CIDR-RU-all.txt | `81` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `44` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `22` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck WHITE-SNI-RU-all.txt | `11` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |

### Общие global-пулы

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| SoliSpirit Protocols/vless.txt | `3591` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| liMilCo v2r pro/vless.txt | `2653` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| barry-far V2ray-config vless.txt | `2580` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2507` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2107` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| ALIILAPRO v2rayNG-Config sub.txt | `410` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| 0xRadikal light/configs.txt | `402` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| MatinGhanbari filtered vless.txt | `303` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| V2RayRoot Config/vless.txt | `201` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| MahsaNetConfigTopic xray_final.txt | `181` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |
| MahanKenway configs/vless.txt | `155` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| Rayan-Config proxy.txt | `53` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| FNET00 Config/Main | `50` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `10790` | `12971` | `+2181` |
| Россия | `↑` | `3521` | `4420` | `+899` |
| Global | `↑` | `7269` | `8551` | `+1282` |

| Обновление, МСК | Общая | Россия | Global | Δ общая | Δ Россия | Δ Global |
|-----------------|-------|--------|--------|---------|----------|----------|
| `2026-07-20 21:20:46 МСК` | `12971` | `4420` | `8551` | `-1312` | `+1323` | `-2635` |
| `2026-07-20 18:50:51 МСК` | `14283` | `3097` | `11186` | `+638` | `-682` | `+1320` |
| `2026-07-20 16:50:08 МСК` | `13645` | `3779` | `9866` | `-340` | `-109` | `-231` |
| `2026-07-20 14:39:50 МСК` | `13985` | `3888` | `10097` | `+189` | `+339` | `-150` |
| `2026-07-20 11:42:46 МСК` | `13796` | `3549` | `10247` | `-184` | `-28` | `-156` |
| `2026-07-20 09:32:50 МСК` | `13980` | `3577` | `10403` | `0` | `+3` | `-3` |
| `2026-07-20 09:22:39 МСК` | `13980` | `3574` | `10406` | `+86` | `-18` | `+104` |
| `2026-07-20 09:12:18 МСК` | `13894` | `3592` | `10302` | `+3241` | `-976` | `+4217` |
| `2026-07-20 08:30:42 МСК` | `10653` | `4568` | `6085` | `-137` | `+1047` | `-1184` |
| `2026-07-20 04:54:46 МСК` | `10790` | `3521` | `7269` | `+445` | `-893` | `+1338` |

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
