from autogen import AssistantAgent, UserProxyAgent
import autogen_ext.models
import os

from autogen.agents.experimental import WebSurferAgent
from ddgs import DDGS
WebSurferAgent

# results = DDGS().text("python programming", max_results=5)
# print(results)
# print(results)


api_key = "AIzaSyCDo_ntqtiRweRyPZ6F-EK520oNkwyHv7Q"

llm_config = {"config_list": [{
        "model": "gemini-flash-lite-latest",
        "api_key": api_key,  # Note, add your own API key here
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "price" : [0,0]
    }],
    "temperature": 0.9,
}

assistant = AssistantAgent(
    name= "assistant", llm_config=llm_config)
user_proxy = UserProxyAgent(
    name = "user_proxy",
    code_execution_config={"work_dir":
                           "data/scratch",
                           "use_docker": False},
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
    )

user_proxy.initiate_chat(assistant, message="Find me comparison of NVIDIA and TESLA Stock Price Change")