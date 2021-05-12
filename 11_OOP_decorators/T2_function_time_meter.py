import time


def timepassed(func):
    def time_meter():
        t0 = time.time()
        func()
        t1 = time.time() - t0
        print(f"Duration of given function: {t1} seconds")
    return time_meter


@timepassed
def example_function():
    print("start")
    time.sleep(2)
    print("end")


example_function()