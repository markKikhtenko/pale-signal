# pale-signal

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated 09:00 and 21:00 MSK](https://img.shields.io/badge/update-09%3A00%20%2F%2021%3A00%20MSK-blue)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Servers](https://img.shields.io/badge/servers-8733-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

Готовые автоматически обновляемые подписки для Mihomo, OpenClash и Happ/Happ Plus.

**Последнее обновление:** `2026-11-21 14:47:05 МСК`

## Подписки

| Файл | Назначение |
|------|------------|
| [subscription.yaml](https://markkikhtenko.github.io/pale-signal/subscription.yaml) | Полный VLESS-пул |
| [subscription-ru.yaml](https://markkikhtenko.github.io/pale-signal/subscription-ru.yaml) | Серверы России |
| [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) | Полный Global-пул, включая источники для белых списков |
| [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) | Приоритетный пул для белых списков, до 5000 серверов |
| [subscription-lan-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml) | Основной LAN-пул, до 5000 серверов |
| [subscription-lan-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml) | Полный LAN-пул без лимита |
| [subscription-lan-global-fast-check.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global-fast-check.yaml) | Тот же LAN Global с более быстрой проверкой |
| [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) | Отдельный Reality-only пул для режима белых списков |
| [subscription-mobile.txt](https://markkikhtenko.github.io/pale-signal/subscription-mobile.txt) | Мобильная Reality-подписка для Happ/Happ Plus |
| [subscription-zapret.yaml](https://markkikhtenko.github.io/pale-signal/subscription-zapret.yaml) | Изолированный VLESS/VMess/Shadowsocks-пул Zapret из страниц 1–25 |

## Быстрый выбор

- Обычный роутер: `subscription-lan-5k.yaml`.
- Максимальный LAN-пул: `subscription-lan-global.yaml`.
- Частая перепроверка узлов: `subscription-lan-global-fast-check.yaml`.
- Режим белых списков: `subscription-global.yaml` (полный пул), `subscription-global-5k.yaml` (приоритетный пул до 5000) или `subscription-bs-safe.yaml` (Reality-only). Для всех трёх используйте `whitelist-routing.conf`.
- Телефон: `subscription-mobile.txt`.
- Отдельный контур Zapret: `subscription-zapret.yaml`.

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `8733` |
| Россия | `1868` |
| Global | `6829` |
| Global 5K | `2387` |
| LAN 5K | `5000` |
| LAN Global | `5210` |
| LAN Global Fast Check | `5210` |
| LAN Experimental | `2143` |
| BS Safe (MANUAL / AUTO) | `1632 / 50` |
| Happ Mobile | `494` |
| Zapret | `2766` |

<!-- LAN-EXPERIMENTAL:START -->
## Тестовые подписки

- [subscription-global-non-stable.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-non-stable.yaml) — тестовый Global-пул.
- [subscription-lan-experimental.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-experimental.yaml) — изолированный LAN-пул на `2143` серверов; все серверы входят в `AUTO`, пересечения с LAN Global удаляются.

Эти варианты могут меняться заметнее основных подписок и не рекомендуются как единственный рабочий профиль.
<!-- LAN-EXPERIMENTAL:END -->

<!-- LAN-SOURCE-STATS:START -->
<!-- LAN-SOURCE-STATS:END -->

## Подключение

### Mihomo/OpenClash

1. Скопируйте нужную ссылку из таблицы.
2. Добавьте её в `Config Subscription` OpenClash без конвертации.
3. Используйте `PROXY` → `AUTO` для автовыбора или `MANUAL` для ручного выбора.

Для `BS Safe` требуется Mihomo/Meta Core v1.19.24 или новее.

### Happ/Happ Plus

Добавьте URL `subscription-mobile.txt` как обычную подписку.

### Zapret

Добавьте `subscription-zapret.yaml` как отдельный профиль. Эта подписка не смешивается с остальными пулами.

## Маршрутизация

Для OpenClash доступны три Override Module:

| Подписка | Override Module |
|----------|-----------------|
| Бесплатные подписки Pale Signal — blacklist | [`blacklist-routing.conf`](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing.conf) |
| Платная подписка VPnBot — blacklist | [`blacklist-routing-vpnbot.conf`](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing-vpnbot.conf) |
| BS Safe — whitelist | [`whitelist-routing.conf`](https://markkikhtenko.github.io/pale-signal/openclash/whitelist-routing.conf) |

Добавьте подходящий URL в **Overwrite Settings → Overwrite Modules** и подключите только один модуль к профилю. `whitelist-routing.conf` предназначен для отдельного BS Safe-роутера и заменяет на нём `/etc/openclash/custom/openclash_custom_overwrite.sh`, поэтому перед включением сохраните резервную копию этого файла.
## Обновление

Сборка запускается в 09:00 и 21:00 МСК. Некорректные конфигурации не публикуются. Наличие узла в подписке не гарантирует его доступность у конкретного провайдера.
