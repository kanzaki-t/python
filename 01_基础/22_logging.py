import logging


def func1(x, y):
    return x / y


x = 10
y = 0

try:
    func1(x, y)
except Exception as e:
    logging.error("出错了" + str(e))  # ERROR:root:出错了division by zero
    logging.error(e)  # ERROR:root:division by zero
