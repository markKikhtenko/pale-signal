# Pale Signal

Автоматически обновляемая VLESS-подписка для Mihomo, OpenClash и FLClash.

## Ссылка для OpenClash

Основная ссылка подписки:

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

Её можно добавить в OpenClash как обычную подписку Clash/Mihomo.

## Файлы подписки

- `subscription.yaml` - основной конфиг Mihomo/OpenClash.
- `merged_flclash.yaml` - тот же конфиг под именем, привычным для FLClash.
- `subscription_base64.txt` - base64-версия YAML.
- `subscription_info.txt` - краткая информация о последней сборке.
- `servers_history.json` - история first seen / last seen по серверам.

## Что делает сборка

- Раз в час запускается GitHub Actions.
- Также есть ручной запуск: `Actions` -> `Regenerate subscription` -> `Run workflow`.
- Скачивает VLESS-ссылки из источника: `https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt`.
- Пропускает некорректные строки.
- Удаляет дубли и делает имена серверов уникальными.
- Поддерживает Reality, TLS, TCP, WebSocket, gRPC и XHTTP.
- Создаёт группы `AUTO`, `FALLBACK`, `PROXY`, а также группы по типам, если такие серверы есть.
- Не проверяет серверы через ping и не пытается подключаться к ним.
- Если источник не скачался, серверов нет или YAML сломан, предыдущие рабочие файлы сохраняются.

## Текущая сборка

- Обновлено: `2026-07-17T09:57:33Z`
- Серверов: `286`
- Reality: `199`
- TLS: `277`
- TCP: `153`
- WebSocket: `21`
- gRPC: `30`
- XHTTP: `82`
