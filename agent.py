from llm import chat
from tools.RegisterTool import TOOLS

def tool_to_schema(tool):
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    }

class Agent:

    def __init__(self):
        self.tools = {t.name: t for t in TOOLS}

    def run(self, user_input: str):

        messages = [
            {"role": "system", "content": "你是一个代码助手，可以读取文件并分析代码"},
            {"role": "user", "content": user_input}
        ]

        tool_schemas = [tool_to_schema(t) for t in TOOLS]

        while True:
            response = chat(messages, tool_schemas)

            msg = response.choices[0].message

            # 🧠 如果模型要调用工具
            if msg.tool_calls:
                for call in msg.tool_calls:
                    tool_name = call.function.name
                    args = eval(call.function.arguments)

                    result = self.tools[tool_name].run(args)

                    messages.append(msg)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": result
                    })

            else:
                return msg.content