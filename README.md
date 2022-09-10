# AppleInStockBot

I made the mistake of not seeing [this post](https://www.reddit.com/r/apple/comments/x9q353/psa_new_alarms_in_ios_default_to_the_last_sound/) and accidentally set a silent alarm for 5 AM to buy the 14 Pro Max in Deep Purple. By the time I woke up, the earliest delivery I could get was for [October 10-17](https://imgur.com/NcESxqg). Instead of refreshing the page every 2 minutes to see if one became available for in store pickup, I wrote this script to alert me when the phone becomes available at a store near me. Within a few hours, I was able to get a pickup for [September 17th](https://imgur.com/TU9LMI0) at a store near me.

&#x200B;

**Setup**

Here's what you'll need:

* An account on [repl.it](https://repl.it)
* An account on [https://uptimerobot.com/](https://uptimerobot.com/)
* Telegram (you can modify the code to send yourself notifications through a different method)

&#x200B;

**Telegram**

Open Telegram and send a message to [https://t.me/BotFather](https://t.me/BotFather). Create a new bot and note down the Bot Token, should be something like `270485614:AAHfiqksKZ8WmR2zSjiQ7_v4TMAKdiHm9T0`. Then, send a message to your newly created bot. Once you've sent a message to this bot, go to [`https://api.telegram.org/bot{botToken}/getUpdates`](https://api.telegram.org/bot{botToken}/getUpdates) in your browser, where `botToken` is the token you just got. You should see a JSON response with the message you sent to the bot. Under `"chat"`, you should see an `"id"` that should look something like `1324685187`. Copy this, it's your chat ID.

&#x200B;

**Repl**

On [repl.it](https://repl.it), create a new repl using Python. Copy the code from [here](https://github.com/rajlulla/AppleInStockBot/blob/main/main.py) into the editor, fill in your info, and click run. You can get your model number from [Best Buy](https://imgur.com/Q3U3HJm). When you click run, if everything works correctly, you should see a small browser window open in the top right and get a message from your bot on Telegram with the status of the phone. Copy the URL of the smaller browser window within your repl.

&#x200B;

**Uptime Robot**

On Uptime Robot, set a new HTTPS monitor and input the URL you just copied there. Set the interval to 5 minutes (can be adjusted) and create the monitor. This will keep your repl running and send you notifications every 5 minutes. 

&#x200B;

Once the phone becomes available, you should get a message from your bot saying when it's available, [like this](https://imgur.com/QDQb2IR). As soon as you get that message, go to the Apple website/app, and get your phone.
