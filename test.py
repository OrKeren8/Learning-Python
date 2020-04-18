import time

class Test:
    @staticmethod
    def print():
        print("momo")
        time.sleep(1)
        print('koko')

class Test2(Test):
    pass


a = Test2()
a.print()