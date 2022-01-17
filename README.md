# EarnAppHAview

Hello everybody,

This integration allows the visualization of your Dashboard data in "Home Assistant".

![Alt Text](https://c.tenor.com/WCE5JUszKGMAAAAC/tenor.gif)

Please note, this is not functional.

The code is under construction




Platform | Description
-- | --
`sensor` | Show various information about the dashboard.

## Requirements

This component requires :
- Home Assistant
- HACS
- [EarnApp Account](https://bit.ly/3A1NxCJ)
- Oauth Token Refresh

## Installation

### HACS

In the HA UI go to "Community" --> "Integrations" and search for "EarnAppHAview" (if not found, add "Custom reposiories" in 3 small dots menu, past the github repositorie url and choose "Integration" category)

### Oauth Token Refresh

1. Go to your EarnApp [Dashboard](https://earnapp.com/dashboard/)
2. Login with Google Account
3. Open Developer tools with "CTR+SHIFT+I"
4. Goto "Network" TAB
5. Refresh Brownser Page ( F5 )
6. After the page refreshes, enter "google_oauth" in the Filter field
7. Click on "google_oauth.js?xxxxxxxx" line.
8. Goto "Cookies" TAB
9. Copy Value of "oauth-refresh-token" line

## Configuration

Confiugration.yaml or Sensor.yaml :

```yaml

- platform: earnapphaview
    token: !secret EarnappToken
    scan_interval: 3600

```

## If you want

if you like what i do, maybe a coffee ? 🥺👉👈

<a href="https://bit.ly/33I0xRy" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TXFHGM3K6DSAQ)
