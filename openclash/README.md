# OpenClash Override Modules

Доступны три модуля:

| Назначение | URL |
|------------|-----|
| Бесплатные подписки Pale Signal — blacklist | `https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing.conf` |
| Платная подписка VPnBot — blacklist | `https://markkikhtenko.github.io/pale-signal/openclash/blacklist-routing-vpnbot.conf` |
| BS Safe — whitelist | `https://markkikhtenko.github.io/pale-signal/openclash/whitelist-routing.conf` |

`blacklist-routing.conf` направляет заблокированные ресурсы в группу `PROXY`, а `blacklist-routing-vpnbot.conf` — в существующую группу `🌐 VPnBot`. Оба используют обновляемые RULE-SET и оставляют обычный трафик на `DIRECT`.

`whitelist-routing.conf` предназначен только для `subscription-bs-safe.yaml` на отдельном роутере в режиме белых списков Huawei/MegaFon. Он устанавливает `whitelist-routing.sh` в `/etc/openclash/custom/openclash_custom_overwrite.sh` и настраивает DIRECT/VPN, DNS и Fake-IP.

Подключайте только один routing-модуль к одному профилю.

## Подключение

1. Откройте **OpenClash → Overwrite Settings → Overwrite Modules**.
2. Добавьте URL нужного модуля и включите автоматическое обновление.
3. Назначьте его нужному профилю и примените профиль в режиме `Rule`.

Перед включением `whitelist-routing.conf` сохраните резервную копию `/etc/openclash/custom/openclash_custom_overwrite.sh`: этот путь общий для OpenClash на данном роутере. Для отката отключите модуль, восстановите файл и перезапустите OpenClash.
