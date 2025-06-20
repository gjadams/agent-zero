import os
from datetime import datetime, timezone
from python.helpers.extension import Extension
from agent import Agent, LoopData
from python.helpers.localization import Localization


class CustomJournalPrompt(Extension):

    async def execute(self, system_prompt: list[str]=[], loop_data: LoopData = LoopData(), **kwargs):
        # append custom journal system prompt
        custom_journal = get_custom_journal_prompt(self.agent)
        system_prompt.append(custom_journal)


def get_custom_journal_prompt(agent: Agent):
    try:
        return agent.read_prompt("agent.custom.journal.md")
    except FileNotFoundError:
        return ""  # Return empty string if file doesn't exist