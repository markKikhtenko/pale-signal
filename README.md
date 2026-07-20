# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-12463-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-21 02:07:08 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Остальные страны и `[UNKNOWN]` | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `12463` |
| Россия | `3277` |
| Global | `9186` |
| Unknown | `2594` |
| Reality | `8259` |
| TLS | `10875` |
| TCP | `8347` |
| WebSocket | `2549` |
| gRPC | `861` |
| XHTTP | `706` |

<details>
<summary>Источники</summary>

Источники разделены по назначению. БС-группа - это whitelist/bypass/26/CIDR/SNI-источники. Общие global-пулы оставлены как запас иностранных VLESS, но не считаются проверенными под обход БС.

### БС / whitelist / bypass

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| AvenCores githubmirror/26.txt | `4153` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| V.O.I.D VPN Bypass url_work.txt | `3184` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| AvenCores 26_urls.json | `2894` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `1656` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| rjsxrd bypass-all | `920` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| ByeWhiteLists2 | `633` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| wlunlocker whitelist_all.txt | `525` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| etoneya whitelist | `389` | [raw](https://etoneya.su/whitelist) |
| zieng2 vless_universal.txt | `352` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| zieng2 vless_lite.txt | `352` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `150` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `119` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `115` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| RKP bypass whitelist.txt | `106` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `91` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| igareck WHITE-CIDR-RU-all.txt | `91` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `91` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `44` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `18` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| igareck WHITE-SNI-RU-all.txt | `9` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |

### Общие global-пулы

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| SoliSpirit Protocols/vless.txt | `3363` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| liMilCo v2r pro/vless.txt | `2653` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2486` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| barry-far V2ray-config vless.txt | `2486` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2120` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| 0xRadikal light/configs.txt | `413` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| ALIILAPRO v2rayNG-Config sub.txt | `409` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| MatinGhanbari filtered vless.txt | `281` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| V2RayRoot Config/vless.txt | `201` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| MahsaNetConfigTopic xray_final.txt | `181` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |
| MahanKenway configs/vless.txt | `157` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| Rayan-Config proxy.txt | `54` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| FNET00 Config/Main | `50` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `13796` | `12463` | `-1333` |
| Россия | `↓` | `3549` | `3277` | `-272` |
| Global | `↓` | `10247` | `9186` | `-1061` |

| Обновление, МСК | Общая | Россия | Global | Δ общая | Δ Россия | Δ Global |
|-----------------|-------|--------|--------|---------|----------|----------|
| `2026-07-21 02:07:08 МСК` | `12463` | `3277` | `9186` | `-20` | `+428` | `-448` |
| `2026-07-21 01:05:49 МСК` | `12483` | `2849` | `9634` | `+418` | `-301` | `+719` |
| `2026-07-21 00:04:11 МСК` | `12065` | `3150` | `8915` | `-783` | `-278` | `-505` |
| `2026-07-20 22:45:47 МСК` | `12848` | `3428` | `9420` | `+30` | `-6` | `+36` |
| `2026-07-20 22:28:30 МСК` | `12818` | `3434` | `9384` | `-153` | `-986` | `+833` |
| `2026-07-20 21:20:46 МСК` | `12971` | `4420` | `8551` | `-1312` | `+1323` | `-2635` |
| `2026-07-20 18:50:51 МСК` | `14283` | `3097` | `11186` | `+638` | `-682` | `+1320` |
| `2026-07-20 16:50:08 МСК` | `13645` | `3779` | `9866` | `-340` | `-109` | `-231` |
| `2026-07-20 14:39:50 МСК` | `13985` | `3888` | `10097` | `+189` | `+339` | `-150` |
| `2026-07-20 11:42:46 МСК` | `13796` | `3549` | `10247` | `-184` | `-28` | `-156` |

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
