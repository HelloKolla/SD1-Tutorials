try:
    x = 45 / 0
    print(x)
except ZeroDivisionError:
    print('This value is invalid')