import os
from datetime import datetime, timezone
from python.helpers.extension import Extension
from agent import Agent, LoopData
from python.helpers.localization import Localization


class CustomInstancePrompt(Extension):

    async def execute(self, system_prompt: list[str]=[], loop_data: LoopData = LoopData(), **kwargs):
        # insert custom instance system prompt
        custom_instance = get_custom_instance_prompt(self.agent)
        system_prompt.insert(0,custom_instance)


def get_custom_instance_prompt(agent: Agent):
    try:
        return agent.read_prompt("agent.custom.instance.md")
    except FileNotFoundError:
        return ""  # Return empty string if file doesn't exist