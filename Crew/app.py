from crewai import Agent, Task, Crew,LLM

local_llm = LLM(
    model="openai/llama-3",  # the model name served by your backend
    base_url="http://192.168.1.15:1234/v1/",  # Ollama default; LM Studio uses :1234
    api_key="na"  # still required but ignored locally
)

info_agent = Agent(
    role="Information Agent",
    goal="Give concise information about a certain topic",
    backstory="You love to do in depth research.",
    llm = local_llm
)

task1 = Task(
    description="Tell me about Sonichu",
    expected_output="Give me a quick one line summary",
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=True,
    memory=False
)

result = crew.kickoff()
print("################ RESULT ###############")
print(result)
