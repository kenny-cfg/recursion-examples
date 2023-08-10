def print_pattern(num):
    if num < 1:
        return
    else:
        print(num, end=" ")
        print_pattern(num - 1)
        print(num, end=" ")
        return


# Driver Code
if __name__ == '__main__':
    my_number = 5
    print_pattern(my_number)