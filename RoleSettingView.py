from typing import Any, Coroutine
import discord

class testChannelSelect(discord.ui.ChannelSelect):
    async def callback(self, interaction: discord.Interaction) -> Coroutine[Any, Any, Any]:
        interaction.response.pong()
        for channel in self.values:
            print(channel.id)

class RoleSettingView(discord.ui.View):
    def __init__(self, *, timeout: float = None):
        super().__init__(timeout=timeout)
        select = testChannelSelect(custom_id= "testSelect")
        self.add_item(select)