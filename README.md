# Pale Signal VLESS Subscription

[![Regenerate subscription](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/markKikhtenko/pale-signal/actions/workflows/update-subscription.yml)
[![Updated](https://img.shields.io/badge/Updated-Every%20Hour-blue)](https://github.com/markKikhtenko/pale-signal)
[![Servers](https://img.shields.io/badge/Servers-225-brightgreen)](https://markkikhtenko.github.io/pale-signal/subscription.yaml)

> Автоматически обновляемая VLESS-подписка для Mihomo, OpenClash и FLClash.
>
> Серверы скачиваются из одного источника каждый час, преобразуются в готовый Clash/Mihomo YAML и публикуются через GitHub Pages.

---

## 📥 Подписка

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

Дополнительные ссылки:

```text
https://markkikhtenko.github.io/pale-signal/merged_flclash.yaml
https://markkikhtenko.github.io/pale-signal/subscription_base64.txt
https://markkikhtenko.github.io/pale-signal/subscription_info.txt
```

---

## 📱 Как установить

### OpenClash

1. Откройте OpenClash в панели роутера.
2. Перейдите в раздел подписок / профилей.
3. Добавьте новую подписку Clash/Mihomo по URL.
4. Вставьте ссылку:

```text
https://markkikhtenko.github.io/pale-signal/subscription.yaml
```

5. Сохраните и обновите подписку.
6. Используйте группу `PROXY`, `AUTO` или нужную группу по типу серверов.

### FLClash / Mihomo-клиенты

1. Откройте раздел `Config`, `Profiles` или `Subscription`.
2. Нажмите `Add`, `URL` или `Remote Config`.
3. Вставьте основную ссылку подписки.
4. Скачайте профиль и включите его.

---

## ✨ Возможности

| Функция | Описание |
|---------|----------|
| 🔄 Автообновление | Каждый час через GitHub Actions |
| 🛠 Ручная перегенерация | `Actions` -> `Regenerate subscription` -> `Run workflow` |
| 🔒 Reality | Поддержка VLESS Reality |
| 🔐 TLS | Поддержка TLS-серверов |
| 🌐 TCP / WS / gRPC / XHTTP | Поддержка основных транспортов Mihomo |
| 🚀 AUTO | URL Test выбирает сервер на стороне клиента |
| 🧯 FALLBACK | Резервное переключение между серверами |
| 🗑 Дедупликация | Повторяющиеся серверы удаляются |
| ✅ Без ping в Actions | Работоспособность проверяет OpenClash/Mihomo |

---

## 📋 Группы серверов

| Группа | Тип | Описание |
|--------|-----|----------|
| `AUTO` | url-test | Автоматический выбор по URL Test |
| `FALLBACK` | fallback | Резервное переключение между серверами |
| `PROXY` | select | Главная группа для правила `MATCH,PROXY` |
| `REALITY` | select | Только Reality-серверы |
| `TLS` | select | Серверы с TLS |
| `WS` | select | WebSocket-серверы |
| `GRPC` | select | gRPC-серверы |
| `XHTTP` | select | XHTTP-серверы |

---

## 🔄 Как работает обновление

```text
Каждый час:
📥 Скачивается свежий список VLESS-ссылок
🧹 Некорректные строки пропускаются
🔄 Ссылки преобразуются в формат Mihomo/OpenClash
🗑 Удаляются дубликаты
💾 Сохраняется новая подписка
🚀 GitHub Pages публикует готовый YAML
📡 OpenClash забирает обновление по ссылке
```

Если источник не скачался, серверов нет или итоговый YAML сломан, предыдущий рабочий файл остаётся опубликованным.

---

## 📁 Файлы в репозитории

| Файл | Назначение |
|------|------------|
| `subscription.yaml` | Основная подписка для OpenClash/Mihomo |
| `merged_flclash.yaml` | Та же подписка под именем для FLClash |
| `subscription_base64.txt` | Base64-версия подписки |
| `subscription_info.txt` | Краткая информация о последней сборке |
| `servers_history.json` | История появления и обновления серверов |
| `scripts/build_subscription.py` | Скрипт сборки подписки |
| `.github/workflows/update-subscription.yml` | Джоба перегенерации и публикации |

---

## 🛠 Источник серверов

1. zieng2 - VLESS lite list

```text
https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt
```

---

## ⚠️ Важно

- Серверы берутся из внешнего публичного списка.
- GitHub Actions не проверяет серверы через ping и не подключается к ним.
- Реальную работоспособность проверяет OpenClash/Mihomo через `AUTO` и `FALLBACK`.
- Для роутера обычно достаточно добавить только `subscription.yaml`.

---

## 💡 Советы

**Если медленно:**

- Используйте группу `AUTO`.
- Подождите несколько минут, пока клиент выполнит URL Test.
- Попробуйте вручную выбрать сервер из `REALITY`, `TLS`, `WS`, `GRPC` или `XHTTP`.

**Если не подключается:**

- Обновите подписку в OpenClash.
- Переключитесь с `AUTO` на `FALLBACK`.
- Попробуйте выбрать сервер вручную из `PROXY`.

**Если серверы пропали:**

- Проверьте статус последнего workflow.
- Дождитесь следующей часовой перегенерации.
- Предыдущая рабочая подписка сохраняется, если новая сборка сломалась.

---

## 📊 Статус

- ✅ Обновлено: `2026-07-17T10:06:17Z`
- ✅ Серверов: `225`
- ✅ Reality: `153`
- ✅ TLS: `217`
- ✅ TCP: `134`
- ✅ WebSocket: `11`
- ✅ gRPC: `17`
- ✅ XHTTP: `63`
- ✅ Автообновление: работает через GitHub Actions
- ✅ Публикация: GitHub Pages
