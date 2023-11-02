"""
range(num)
获取一个从0开始，到num结束的数组序列，不包含num本身

range(num1, num2)
获取一个从num1开始，到num2结束的数字序列，不包含num2本身

range(num1, num2, step)
获取一个从num1开始，到num2结束的数字序列，不包含num2本身
数字之前的步长，以step为准，默认是1
"""

for x in range(3):
    print(x)  # 0 1 2

for x in range(1, 3):
    print(x)  # 1 2

for x in range(1, 6, 2):
    print(x)  # 1 3 5
