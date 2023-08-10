# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# Exit condition:
#   * if i = 0, then return 0
#   * if i = 1, then return 1
# Recursive definition:
#   * fib(i) = fib(i - 1) + fib(i - 2)

def fib(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fib(index - 1) + fib(index - 2)


if __name__ == '__main__':
    result = fib(10)
    print(result)
