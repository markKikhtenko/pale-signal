# pale-signal подписки

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
<<<<<<< HEAD
[![Servers](https://img.shields.io/badge/servers-4791-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)
=======
[![Servers](https://img.shields.io/badge/servers-4479-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)
>>>>>>> 2e30e3c (Clarify subscription links in README)

pale-signal автоматически собирает VLESS-подписки для Mihomo/OpenClash.

<<<<<<< HEAD
**Последнее обновление:** `2026-07-17T13:01:22Z`
=======
**Последнее обновление:** `2026-07-17T13:11:50Z`
>>>>>>> 2e30e3c (Clarify subscription links in README)

## Подписки

| Название | Что внутри | Ссылка |
|----------|------------|--------|
| pale-signal подписка — общая | Все серверы | https://markkikhtenko.github.io/pale-signal/subscription.yaml |
| pale-signal подписка — Россия | Серверы, физически расположенные в России | https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml |
| pale-signal подписка — Global | Остальные страны и `[UNKNOWN]` | https://markkikhtenko.github.io/pale-signal/subscription-global.yaml |

Прямые ссылки для OpenClash:

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml
https://markkikhtenko.github.io/pale-signal/subscription-global.yaml
```

## Статус

| Показатель | Значение |
|------------|----------|
<<<<<<< HEAD
| Всего серверов | `4791` |
| Россия | `2194` |
| Global | `2597` |
| Unknown | `55` |
| Reality | `3684` |
| TLS | `4279` |
| TCP | `3370` |
| WebSocket | `734` |
| gRPC | `270` |
| XHTTP | `417` |
=======
| Всего серверов | `4479` |
| Россия | `2111` |
| Global | `2368` |
| Unknown | `55` |
| Reality | `3414` |
| TLS | `3978` |
| TCP | `3120` |
| WebSocket | `716` |
| gRPC | `258` |
| XHTTP | `385` |
>>>>>>> 2e30e3c (Clarify subscription links in README)

## Группы

Во всех трёх подписках оставлены только:

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
- Узлы без определённой страны попадают в `subscription-global.yaml` и получают `[UNKNOWN]` в имени.

## Обновление

GitHub Actions пересобирает подписки раз в час. Ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.

Если источник не скачался, серверов нет или YAML сломан, предыдущие рабочие файлы не заменяются.
