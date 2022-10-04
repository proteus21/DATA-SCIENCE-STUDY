'''
Recursievly function

'''


collatz_list = []


def collatz(n):
    collatz_list.append(n)
    if n == 1:
        return collatz_list
    elif n % 2:
        return collatz(n * 3 + 1)
    else:
        return collatz(n//2)


if __name__ == '__main__':
    print(collatz(11))