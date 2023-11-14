import discord
from discord.ext import commands

import os
from apikeys import *
from logger import *

# Setup intents
intents: discord.Intents = discord.Intents.default()
intents.message_content = True

'''
CHESS BOT CLASS
'''
class ChessBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix='c',
            intents = intents,
            help_command = None
            )
        self.logger: logging.Logger = logger
        return
    
    async def loadCogs(self) -> None:
        '''
        Load cogs when bot starts
        '''
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
            if file.endswith(".py"):
                extension: str = file[:-3]
                try:
                    await self.load_extension(f"cogs.{extension}")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    self.logger.error(f"Failed to load extension {extension}\n{exception}")


bot: ChessBot = ChessBot()
bot.run(TOKEN)