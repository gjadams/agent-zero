import os
from datetime import datetime, timezone
from python.helpers.extension import Extension
from agent import Agent, LoopData
from python.helpers.localization import Localization


class CustomFinalCheckPrompt(Extension):

    async def execute(self, system_prompt: list[str]=[], loop_data: LoopData = LoopData(), **kwargs):
        # append custom final system check
        custom_final_check_prompt = get_custom_final_check_prompt(self.agent)
        system_prompt.append(custom_final_check_prompt)


def get_custom_final_check_prompt(agent: Agent):
    try:
        return agent.read_prompt("agent.custom.final_check.md")
    except FileNotFoundError:
        return "# Final Check\n\n# Ready\n\n"  # Return empty string if file doesn't exist