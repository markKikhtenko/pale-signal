# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-10653-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-20 08:30:42 МСК`

## Подписки

| Подписка | Что внутри | Ссылка для OpenClash | Скачать |
|----------|------------|----------------------|---------|
| **pale-signal подписка - общая** | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml | [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| **pale-signal подписка - Россия** | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml | [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| **pale-signal подписка - Global** | Остальные страны и `[UNKNOWN]` | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml | [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `10653` |
| Россия | `4568` |
| Global | `6085` |
| Unknown | `113` |
| Reality | `8586` |
| TLS | `9919` |
| TCP | `7898` |
| WebSocket | `1505` |
| gRPC | `672` |
| XHTTP | `578` |

<details>
<summary>Последние 10 обновлений и тренд</summary>

| Подписка | Тренд | Первое | Последнее | Разница |
|----------|-------|--------|-----------|---------|
| Общая | `↑` | `9939` | `10653` | `+714` |
| Россия | `↑` | `3217` | `4568` | `+1351` |
| Global | `↓` | `6722` | `6085` | `-637` |

| Обновление, МСК | Общая | Россия | Global | Δ общая | Δ Россия | Δ Global |
|-----------------|-------|--------|--------|---------|----------|----------|
| `2026-07-20 08:30:42 МСК` | `10653` | `4568` | `6085` | `-137` | `+1047` | `-1184` |
| `2026-07-20 04:54:46 МСК` | `10790` | `3521` | `7269` | `+445` | `-893` | `+1338` |
| `2026-07-20 02:47:26 МСК` | `10345` | `4414` | `5931` | `+212` | `+54` | `+158` |
| `2026-07-20 01:42:25 МСК` | `10133` | `4360` | `5773` | `-146` | `-47` | `-99` |
| `2026-07-20 00:42:00 МСК` | `10279` | `4407` | `5872` | `-78` | `+38` | `-116` |
| `2026-07-19 23:03:11 МСК` | `10357` | `4369` | `5988` | `+230` | `+7` | `+223` |
| `2026-07-19 22:37:20 МСК` | `10127` | `4362` | `5765` | `+245` | `+296` | `-51` |
| `2026-07-19 21:49:37 МСК` | `9882` | `4066` | `5816` | `-57` | `+849` | `-906` |
| `2026-07-19 21:17:40 МСК` | `9939` | `3217` | `6722` | `-148` | `-1076` | `+928` |

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

Если источники не скачались, серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
