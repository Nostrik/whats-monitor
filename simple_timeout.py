# import time
# import threading
#
#
# def decor_timeout(function):
#     def wrapper():
#         print('decor before')
#         t = threading.Thread(target=function)
#         t.start()
#         t.join(timeout=3.0)
#         raise TimeoutError
#         # print('decor after')
#     return wrapper
#
#
# @decor_timeout
# def time_count():
#     for i in range(10, 1, -1):
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     time_count()
import time
import timeout_decorator


@timeout_decorator.timeout(5, timeout_exception=StopIteration)
def mytest():
    print("Start")
    for i in range(1, 10):
        time.sleep(1)
        print("{} seconds have passed".format(i))


if __name__ == '__main__':
    mytest()
