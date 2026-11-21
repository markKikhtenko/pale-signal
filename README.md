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
| [subscription-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global.yaml) | Все серверы вне России |
| [subscription-global-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-global-5k.yaml) | Global, до 5000 серверов |
| [subscription-lan-5k.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-5k.yaml) | Основной LAN-пул, до 5000 серверов |
| [subscription-lan-global.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global.yaml) | Полный LAN-пул без лимита |
| [subscription-lan-global-fast-check.yaml](https://markkikhtenko.github.io/pale-signal/subscription-lan-global-fast-check.yaml) | Тот же LAN Global с более быстрой проверкой |
| [subscription-bs-safe.yaml](https://markkikhtenko.github.io/pale-signal/subscription-bs-safe.yaml) | Reality-узлы для режима белых списков |
| [subscription-mobile.txt](https://markkikhtenko.github.io/pale-signal/subscription-mobile.txt) | Мобильная Reality-подписка для Happ/Happ Plus |
| [subscription-zapret.yaml](https://markkikhtenko.github.io/pale-signal/subscription-zapret.yaml) | Изолированный VLESS/VMess/Shadowsocks-пул Zapret из страниц 1–25 |

## Быстрый выбор

- Обычный роутер: `subscription-lan-5k.yaml`.
- Максимальный LAN-пул: `subscription-lan-global.yaml`.
- Частая перепроверка узлов: `subscription-lan-global-fast-check.yaml`.
- Режим белых списков: `subscription-bs-safe.yaml` вместе с отдельным BS Safe override ниже.
- Телефон: `subscription-mobile.txt`.
- Отдельный контур Zapret: `subscription-zapret.yaml`.

## Статус

| Показатель | Значение |
|------------|----------|
| Всего серверов | `8733` |
| Россия | `1868` |
| Global | `6910` |
| Global 5K | `2378` |
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

Два существующих routing-модуля используют общие обновляемые RULE-SET и оставляют обычный трафик на `DIRECT`:

| Подписка | Override Module |
|----------|-----------------|
| Бесплатные подписки Pale Signal | [`blacklist-routing.conf`](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing.conf) |
| Платная подписка VPnBot | [`blacklist-routing-vpnbot.conf`](https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing-vpnbot.conf) |

Они не меняют DNS, Fake-IP, серверы или параметры подключения. Подключайте только один routing-модуль к одному профилю.

### Custom overwrite для BS Safe

Подписочный модуль для `subscription-bs-safe.yaml`:

`https://markkikhtenko.github.io/pale-signal/openclash/whitelist-routing.conf`

Модуль не изменяет два routing-модуля выше. Он загружает сохранённый shell-overwrite в штатный путь `/etc/openclash/custom/openclash_custom_overwrite.sh` и настраивает DIRECT/VPN, DNS и Fake-IP для режима белых списков Huawei/MegaFon.

Перед подключением:

1. Сохраните резервную копию существующего `openclash_custom_overwrite.sh`.
2. Добавьте URL `whitelist-routing.conf` в **Overwrite Settings → Overwrite Modules**.
3. Используйте его только с BS Safe и не включайте routing-модули для того же профиля.

Путь custom overwrite общий для всего OpenClash. Для отката отключите BS Safe-модуль, восстановите прежний файл и перезапустите OpenClash.
## Обновление

Сборка запускается в 09:00 и 21:00 МСК. Некорректные конфигурации не публикуются. Наличие узла в подписке не гарантирует его доступность у конкретного провайдера.
