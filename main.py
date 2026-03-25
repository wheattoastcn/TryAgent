from agent import Agent

agent = Agent()

while True:
    q = input(">>> ")

    if q == "exit":
        break

    result = agent.run(q)
    print(result)
