# OpenClash overrides

В репозитории есть два routing-модуля и отдельный custom overwrite для режима белых списков.

## Routing-модули

| Назначение | URL |
|------------|-----|
| Бесплатные подписки Pale Signal | `https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing.conf` |
| Платная подписка VPnBot | `https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing-vpnbot.conf` |

Оба модуля используют обновляемые RULE-SET, оставляют обычный трафик на `DIRECT` и не меняют DNS, Fake-IP, TUN, IPv6, серверы или параметры подключения.

- `blacklist-routing.conf` направляет заблокированные ресурсы в группу `PROXY`.
- `blacklist-routing-vpnbot.conf` направляет их в существующую группу `🌐 VPnBot`.

Подключайте только один routing-модуль к одному профилю.

## Custom overwrite для BS Safe

URL подписочного модуля:

`https://markkikhtenko.github.io/pale-signal/openclash/whitelist-routing.conf`

Он предназначен только для `subscription-bs-safe.yaml` на роутере в режиме белых списков Huawei/MegaFon. Модуль загружает сохранённый скрипт в `/etc/openclash/custom/openclash_custom_overwrite.sh` и применяет его без изменения исходной логики:

- выбранные публичные и операторские сервисы идут через `DIRECT`;
- Т-Банк, Сбер и Спортмастер принудительно идут через VPN-политику профиля;
- для DIRECT-доменов возвращаются реальные IP вместо Fake-IP;
- используются локальные сети и DNS Huawei/MegaFon;
- IPv6 внутри Mihomo отключается.

Этот модуль не изменяет `blacklist-routing.conf`, `blacklist-routing-vpnbot.conf` или их RULE-SET.

Важно: путь `openclash_custom_overwrite.sh` общий для всего OpenClash. Модуль заменит существующий локальный custom overwrite и после установки скрипт может выполняться при запуске других профилей на том же роутере.

## Подключение

### Routing-модуль

1. Откройте **OpenClash → Overwrite Settings → Overwrite Modules**.
2. Добавьте URL подходящего routing-модуля и включите автоматическое обновление.
3. Назначьте его нужному профилю и примените профиль в режиме `Rule`.

### BS Safe

1. Сохраните резервную копию `/etc/openclash/custom/openclash_custom_overwrite.sh`.
2. Добавьте URL `whitelist-routing.conf` в **Overwrite Modules**.
3. Используйте его только с `subscription-bs-safe.yaml`.
4. Не включайте routing-модули для того же BS Safe-профиля.

Для отката отключите BS Safe-модуль, восстановите прежний `openclash_custom_overwrite.sh` и перезапустите OpenClash.
