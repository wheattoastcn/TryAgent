class BaseTool:
    name = ""
    description = ""

    def run(self, args: dict):
        raise NotImplementedError