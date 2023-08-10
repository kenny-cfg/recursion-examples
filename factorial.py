def factorial(num):
    product = 1
    for i in range(num):
        product *= (i + 1)
    return product


if __name__ == '__main__':
    result = factorial(5)  # 5 x 4 x 3 x 2 x 1
    print(result)
