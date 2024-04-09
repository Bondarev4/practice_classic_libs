class Runner:
    arr = []

    def __init__(self, name):
        self.name = name
        self.arr.append(self)

    @staticmethod
    def func(x):
        print(x ** 2)

    @classmethod
    def run(cls, num):
        return f'{num} running!'


print(Runner.run(5))
