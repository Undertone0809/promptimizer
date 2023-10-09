from typing import List, Optional

from promptulate.llms import ChatOpenAI

from promptimizer.prompt import builder_prompt


def build_prompt(prompt: str, model: str) -> str:
    messages = builder_prompt.prompt_builder_prompts
    messages.add_user_message(f"[Prompt Usage] {prompt}")
    return ChatOpenAI(temperature=0.0, model=model).predict(messages).content
