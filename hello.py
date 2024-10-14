from crewai import Agent, Task, Crew
import os

os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama3-70b-8192"
os.environ["OPENAI_API_KEY"] = "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"

email = """ 
you won a milion dollar you have to clain it today harry up fill up the form and get your reward !
"""

classifier = Agent(
    role = "email classifier",
    goal = "accurately classify emails based in their importance. give every email one of these rating: important, causal or spam",
    backstory = "you are an ai assistance whose only job is to classify email accurately and honestly. Do not be afraid to give to email bad rating if they are not important. your job is to help the user manage their inboxs.",
    verbose = True,
    allow_delegation = False
)

responder = Agent(
    role = "email responder",
    goal = "based on the importance of the email, write a concise and simple response. if the email is rated 'importance' write a formal response and if the email is rated 'causal' write a causal response, and if the email is 'spam' write a better explanation about it being spam and why it was classified as such. no matter what, be vary concise.",
    backstory = "you are an ai assistance whose only job is to write short response to email based on thire importance. the importance will be provided to you by 'clasifier' agent.",
    verbose = True,
    allow_delegation = False
)

classify_email = Task(
    description = f"Respond to the email: '{email}'",
    agent = classifier,
    expected_output = "One of these three options: 'important', 'causal', 'spam' ",
)

respond_to_email = Task(
    description = f"Respond to the email: '{email}' based on the importance provided by the 'classifier' agent.",
    agent = responder,
    expected_output = "A short response to the email",
)

crew = Crew(
    agents = [classifier, responder],
    tasks = [classify_email, respond_to_email],
    verbose = True
)

output = crew.kickoff()
print(output)