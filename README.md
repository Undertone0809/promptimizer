# Promptimizer

Promptimizer is "prompt" + "optimizer", which is a prompt optimizer. It aims to build the high-quality LLM prompts for everyone. It can build and optimize an elegant prompt for you.

We use structured prompt templates to guide LLM in building an efficient prompt that can more accurately output the answers users want.

![usage.png](./docs%2Fimages%2Fusage.png)

# Setup

## Pip (Method1 Recommend)

Open terminal and enter the following command.

```shell
pip install promptimizer
```

Using following command to open client.

```text
promptimizer
```

## Git Clone (Method2)

Clone repo to local.

```shell
git clone https://github.com/Undertone0809/promptimizer
```

Install all relevant packages.

```shell
pip install poetry
poetry install 
```

Copy `.env.example` rename it as `.env`, saving it to the root directory of the current project. Fill in your openai key in `.env`.

```text
OPENAI_API_KEY=your-key
```

Run the script.

```shell
python main.py
```
