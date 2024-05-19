import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.llms import Ollama
from langchain_community.llms import Ollama

mistral = Ollama(model="mistral")

os.environ['GOOGLE_API_KEY'] = ("Enter Your API Key here")
llm = ChatGoogleGenerativeAI(
    model="gemini-pro", verbose=True, temperature=0.1, google_api_key=os.environ['GOOGLE_API_KEY']
)

#Customize the Agent here
Personal_Assistant = Agent(
  role='AI Assistant',
  goal='To Help and Assist the user to make his day more productive',
  backstory="""You work at an All knowing AI and Personal Assistant of Subash Kumar,
  You will help Mr.Subash by helping him in studies, work, outdoor activities,
  You try to make his job easy by creating a perfect schedule to achieve maximum productivity""",
  verbose=True,
  allow_delegation=True,
  llm=llm,
)

Health_Assistant = Agent(
  role='Fitness and Health Trainer',
  goal='To keep Mr.Subash health and fitness at top notch',
  backstory="""Your main goal is to keep Subash active and fit without affecting his daily routine much
  You will give him some basic home workout routine and other physical and
  mental activities to make him healthy and productive""",
  verbose=True,
  allow_delegation=True,
  llm=llm,
)

# Customize the Task here
task1 = Task(
  description="""Give me today schedule, I want to study 3 chapters in maths and
  I need to do some exercise too. I wake up at 4:30 and go to bed at night 9:30""",
  expected_output="Give the Output in points",
  agent=Personal_Assistant
)

#Customize the Crew here
crew = Crew(
  agents=[Personal_Assistant, Health_Assistant],
  tasks=[task1],
  verbose=1, 
  process=Process.sequential,
)

result = crew.kickoff()