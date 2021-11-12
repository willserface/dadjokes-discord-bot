# Dad Jokes Bot
© 2021 - Will Serface. [Contact me here](https://www.willserface.com/contact)

### Usage
 - To use this bot, either:
   - Use this [link](https://discord.com/oauth2/authorize?client_id=908798748493217843&permissions=2048&scope=bot%20applications.commands) to add the bot to your server
     - Bot will request message read and command creation permissions
   - Use your own computer to run `bot.py` and supply your own bot
     - You will be prompted to `input()` your bot's token

### Features
 - On startup, bot will set it's status to be "Listening to the news"
 - When bot hears 'dad', 'father', 'parent', or 'papa', it will pretend it can't hear
 - When bot hears a message that contains "tell me a joke", it will respond with a random line from `jokes.txt`
 - When bot hears any variation of 'I am', it will respond by addressing the author as whatever follows