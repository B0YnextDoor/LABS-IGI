from utils import stopFunction


def RunTask(Class):
    def RunningDecorator(func):
        def RunLoop(self):
            print(func.__doc__)
            obj = Class()
            while True:
                res = func(self, obj)
                if res is not None or stopFunction('finish task') != "0":
                    break
            print('Task exit')
        return RunLoop
    return RunningDecorator
