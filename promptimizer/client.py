import click
from typing import Optional

import questionary

from promptimizer.utils.color_print import print_text
from promptimizer import prompt_builder, prompt_optimizer


def get_user_input() -> Optional[str]:
    """Receive multiple lines of input from users."""
    marker = (
        "# You input are here (please delete this line)\n"
        "You should save it and close the notebook after writing the prompt. (please delete this line)\n"
    )
    message = click.edit(marker)
    if message is not None:
        return message
    return None


def startup():
    print_text("Welcome to Prompt Optimizer", "pink")

    while True:
        choose = questionary.select(
            "What do you want to do?",
            choices=["Prompt Optimizer", "Prompt Builder", "Exit"],
        ).ask()

        if choose == "Prompt Optimizer":
            print_text("Please input your original prompt:", "pink")
            user_input = get_user_input()
            print_text(f"[User] {user_input}")
            res = prompt_builder.build_prompt(user_input)
        elif choose == "Prompt Builder":
            print_text("Please input your demand:", "pink")
            user_input = get_user_input()
            print_text(f"[User] {user_input}")
            res = prompt_optimizer.optimize_prompt(user_input)
        else:
            exit()

        print_text(f"[Answer] {res}", "blue")


if __name__ == "__main__":
    startup()
