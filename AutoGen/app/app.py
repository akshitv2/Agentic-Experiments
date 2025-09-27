from autogen import AssistantAgent, UserProxyAgent
import os


results = DDGS().text("python programming", max_results=5)
print(results)
print(results)


# api_key = "Something"
#
# llm_config = {"config_list": [{
#         "model": "google/gemma-3n-e4b",
#         "api_key": api_key,  # Note, add your own API key here
#         "base_url": "http://100.97.1.1:1234/v1/",
#         "price" : [0,0]
#     }],
#     "temperature": 0.9,
# }
#
# assistant = AssistantAgent(
#     name= "assistant", llm_config=llm_config)
# user_proxy = UserProxyAgent(
#     name = "user_proxy",
#     code_execution_config={"work_dir":
#                            "data/scratch",
#                            "use_docker": False},
#     human_input_mode="NEVER",
#     is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
#     )
#
# user_proxy.initiate_chat(assistant, message="Find me comparison of NVIDIA and TESLA Stock Price Change")