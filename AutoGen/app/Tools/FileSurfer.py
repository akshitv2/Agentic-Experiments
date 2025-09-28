from autogen import AssistantAgent, UserProxyAgent
from autogen_ext.agents.file_surfer import FileSurfer
from autogen_ext.models.openai import OpenAIChatCompletionClient

OpenAIChatCompletionClient


assistant = AssistantAgent(name="assistant")
user = UserProxyAgent(name="user", human_input_mode="ALWAYS")

# Register File Surfer so the assistant can use it
file_surfer = FileSurferAgent(
    name="file_surfer",
    root_dir=".",       # The sandbox base directory
    allow_write=True,   # Optional: allow creating/updating files
)
# Create a file surfer that works in the current directory
file_surfer = FileSurferAgent(
    name="file_surfer",
    root_dir=".",   # base directory to surf
)
