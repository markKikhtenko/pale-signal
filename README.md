# Pale Signal

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated hourly](https://img.shields.io/badge/update-every%20hour-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-4440-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

Автоматически обновляемые VLESS-подписки для Mihomo/OpenClash.

**Последнее обновление:** `2026-07-17T12:53:46Z`

## Подписки

| Файл | Что внутри | Ссылка |
|------|------------|--------|
| `subscription.yaml` | Все серверы | [скачать](https://markkikhtenko.github.io/pale-signal/subscription.yaml) |
| `subscription-ru.yaml` | Серверы, физически расположенные в России | [скачать](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) |
| `subscription-global.yaml` | Остальные страны и `[UNKNOWN]` | [скачать](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) |

Основная ссылка для OpenClash:

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `4440` |
| Россия | `2100` |
| Global | `2340` |
| Unknown | `55` |
| Reality | `3415` |
| TLS | `3940` |
| TCP | `3090` |
| WebSocket | `717` |
| gRPC | `264` |
| XHTTP | `369` |

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
