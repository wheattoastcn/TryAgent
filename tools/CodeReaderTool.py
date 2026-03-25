from .BaseTool import BaseTool

class CodeReaderTool(BaseTool):
    name = "read_codefile"
    description = "读取本地代码文件内容"

    def run(self, args: dict):
        path = args.get("path")

        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return str(e)