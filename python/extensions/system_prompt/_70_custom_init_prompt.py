import os
from datetime import datetime, timezone
from python.helpers.extension import Extension
from agent import Agent, LoopData
from python.helpers.localization import Localization


class CustomInitPrompt(Extension):

    async def execute(self, system_prompt: list[str]=[], loop_data: LoopData = LoopData(), **kwargs):
        # insert custom init system prompt
        custom_init = get_custom_init_prompt(self.agent)
        system_prompt.insert(0,custom_init)


def get_custom_init_prompt(agent: Agent):
    try:
        return agent.read_prompt("agent.custom.init.md")
    except FileNotFoundError:
        return ""  # Return empty string if file doesn't exist