# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-11840-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-21 23:40:56 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Остальные страны и `[UNKNOWN]` | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `11840` |
| Россия | `3107` |
| Global | `8733` |
| Unknown | `2715` |
| Reality | `7980` |
| TLS | `10266` |
| TCP | `8128` |
| WebSocket | `2237` |
| gRPC | `825` |
| XHTTP | `650` |

<details>
<summary>Источники</summary>

Источники разделены по назначению. БС-группа - это whitelist/bypass/26/CIDR/SNI-источники. Общие global-пулы оставлены как запас иностранных VLESS, но не считаются проверенными под обход БС.

### БС / whitelist / bypass

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| AvenCores githubmirror/26.txt | `4043` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/26.txt) |
| V.O.I.D VPN Bypass url_work.txt | `2950` | [raw](https://raw.githubusercontent.com/VOID-Anonymity/V.O.I.D-VPN_Bypass/main/url_work.txt) |
| AvenCores 26_urls.json | `2730` | [raw](https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/source/config/26_urls.json) |
| wlrus wl.txt | `1604` | [raw](https://s3c3.001.gpucloud.ru/wlr/wl.txt) |
| rjsxrd bypass-all | `764` | [raw](https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt) |
| ByeWhiteLists2 | `633` | [raw](https://raw.githubusercontent.com/ByeWhiteLists/ByeWhiteLists2/refs/heads/main/ByeWhiteLists2.txt) |
| wlunlocker whitelist_all.txt | `542` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_all.txt) |
| etoneya whitelist | `305` | [raw](https://etoneya.su/whitelist) |
| zieng2 vless_universal.txt | `248` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt) |
| zieng2 vless_lite.txt | `248` | [raw](https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt) |
| vladvarp Prometheus WhiteList/vless.txt | `145` | [raw](https://raw.githubusercontent.com/vladvarp/Prometheus/main/WhiteList/vless.txt) |
| Epodonios Sub26.txt | `119` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Sub26.txt) |
| wlunlocker whitelist_cidr2_ru.txt | `115` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr2_ru.txt) |
| RKP bypass whitelist.txt | `97` | [raw](https://raw.githubusercontent.com/RKPchannel/RKP_bypass_configs/main/whitelist.txt) |
| igareck Vless-Reality-White-Lists-Rus-Mobile.txt | `96` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt) |
| igareck WHITE-CIDR-RU-all.txt | `96` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt) |
| wlunlocker whitelist_cidr1_ru.txt | `91` | [raw](https://raw.githubusercontent.com/wlunlocker/vpn-configs/main/whitelist_cidr1_ru.txt) |
| igareck WHITE-SNI-RU-all.txt | `19` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt) |
| igareck WHITE-CIDR-RU-checked.txt | `14` | [raw](https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-checked.txt) |
| PrinceVSFX Adapt-Configs White_list.txt | `7` | [raw](https://raw.githubusercontent.com/PrinceVSFX/Adapt-Configs/main/Configs/White_list.txt) |

### Общие global-пулы

| Источник | Серверов в подписке | Ссылка |
|----------|---------------------|--------|
| SoliSpirit Protocols/vless.txt | `3445` | [raw](https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Protocols/vless.txt) |
| liMilCo v2r pro/vless.txt | `2605` | [raw](https://raw.githubusercontent.com/liMilCo/v2r/main/pro/vless.txt) |
| barry-far V2ray-config vless.txt | `2473` | [raw](https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt) |
| Epodonios Splitted-By-Protocol/vless.txt | `2465` | [raw](https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt) |
| Surfboardv2ray TGParse mixed | `2107` | [raw](https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed) |
| ALIILAPRO v2rayNG-Config sub.txt | `404` | [raw](https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt) |
| 0xRadikal light/configs.txt | `350` | [raw](https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/light/configs.txt) |
| MatinGhanbari filtered vless.txt | `280` | [raw](https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt) |
| V2RayRoot Config/vless.txt | `201` | [raw](https://raw.githubusercontent.com/V2RayRoot/V2RayConfig/main/Config/vless.txt) |
| MahanKenway configs/vless.txt | `154` | [raw](https://raw.githubusercontent.com/MahanKenway/Freedom-V2Ray/main/configs/vless.txt) |
| MahsaNetConfigTopic xray_final.txt | `134` | [raw](https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt) |
| Rayan-Config proxy.txt | `54` | [raw](https://raw.githubusercontent.com/Rayan-Config/C-Sub/refs/heads/main/configs/proxy.txt) |
| FNET00 Config/Main | `50` | [raw](https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main) |

</details>

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↓` | `12463` | `11840` | `-623` |
| Россия | `↓` | `3277` | `3107` | `-170` |
| Global | `↓` | `9186` | `8733` | `-453` |

| Обновление, МСК | Общая | Россия | Global | Δ общая | Δ Россия | Δ Global |
|-----------------|-------|--------|--------|---------|----------|----------|
| `2026-07-21 23:40:56 МСК` | `11840` | `3107` | `8733` | `-19` | `-62` | `+43` |
| `2026-07-21 21:45:03 МСК` | `11859` | `3169` | `8690` | `-243` | `-809` | `+566` |
| `2026-07-21 19:47:16 МСК` | `12102` | `3978` | `8124` | `-131` | `+1211` | `-1342` |
| `2026-07-21 17:25:43 МСК` | `12233` | `2767` | `9466` | `+251` | `-338` | `+589` |
| `2026-07-21 15:03:47 МСК` | `11982` | `3105` | `8877` | `-57` | `-854` | `+797` |
| `2026-07-21 12:49:02 МСК` | `12039` | `3959` | `8080` | `-629` | `+890` | `-1519` |
| `2026-07-21 10:37:44 МСК` | `12668` | `3069` | `9599` | `-154` | `-148` | `-6` |
| `2026-07-21 08:02:16 МСК` | `12822` | `3217` | `9605` | `+232` | `-483` | `+715` |
| `2026-07-21 04:31:46 МСК` | `12590` | `3700` | `8890` | `+127` | `+423` | `-296` |
| `2026-07-21 02:07:08 МСК` | `12463` | `3277` | `9186` | `-20` | `+428` | `-448` |

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

GitHub Actions запускает пересборку примерно раз в час, сейчас cron стоит на 17-й минуте часа. GitHub может задерживать scheduled-запуски; ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.

Если часть источников не скачалась, она пропускается. Если серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
