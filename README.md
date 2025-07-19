# SDS-dashboard-demo
Example dashboard made with Streamlit showcasing some of its capabilties

## What there is
1. Dataframe and plots page
2. Map integration
3. SQL database and query page
4. Embed with `iframe`
5. Chatbot with OpenAI LLM
6. File Q&A with Anthropic LLM

## Setting up the environment
Clone this github repo into the SDS cluster after opening up VSCode by opening the terminal with `Ctrl` + `~` and pasting in this: `git clone https://github.com/DontSlipOnDirt/SDS-dashboard-demo.git`. This will copy and create a folder with all the files of this repo in your own portion of the SDS cluster. Navigate by terminal into the folder and if you are using `[uv](https://docs.astral.sh/uv/)` as package manager for Python, use `uv sync uv.lock` to make environment with requirements. Then run the dashboard with `uv run streamlit run Intro.py`.
