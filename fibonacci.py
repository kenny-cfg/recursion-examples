# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# Exit condition:
#   * if i = 0, then return 0
#   * if i = 1, then return 1
# Recursive definition:
#   * fib(i) = fib(i - 1) + fib(i - 2)

def fib_orig(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fib_orig(index - 1) + fib_orig(index - 2)


def fib(index):
    return index if index <= 1 else fib(index - 1) + fib(index -2)


def fib_without_recursion(index):
    if index <= 1:
        return index
    two_before = 0
    one_before = 1
    for i in range(index - 1):
        current = two_before + one_before
        two_before = one_before
        one_before = current
    return one_before


if __name__ == '__main__':
    result = fib_without_recursion(50)
    print(result)
    result_nice = fib(50)
    print(result_nice)

# For index large (> 30) this is really inefficient
# You can use the https://en.wikipedia.org/wiki/Memoization pattern
