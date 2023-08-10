def factorial(num):
    product = 1
    for i in range(num):
        product *= (i + 1)
    return product


def factorial_recursion(num):
    return 1 if num <= 0 else factorial_recursion(num - 1) * num # ternary notation


if __name__ == '__main__':
    result = factorial(5)  # 5 x 4 x 3 x 2 x 1
    print(result)
    result_with_recursion = factorial_recursion(5)
    print(result)

