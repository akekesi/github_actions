from src.func_00 import func_00


class Class00:
    def __init__(self, config: dict) -> None:
        self.a = config["a"]
        self.b = 0

    def func_00(self):
        self.b = func_00(arg=self.a)


if __name__ == "__main__":
    config = {
        "a": -0.123456789
    }

    class_00 = Class00(config=config)
    print(f"{class_00.a = }")
    print(f"{class_00.b = }")

    class_00.func_00()
    print(f"{class_00.a = }")
    print(f"{class_00.b = }")
