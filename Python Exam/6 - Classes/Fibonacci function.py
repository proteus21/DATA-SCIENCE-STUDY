
#iteration
def fibb(n):
    result = [1, 1]
    for i in range(n-2):
        result.append(result[i] + result[i+1])
    return result


if __name__ == '__main__':
    print(fibb(10))

#recuresiely

def rec_fibb(n):
    if n<2:
        return 1
    else:
        return rec_fibb(n-2)+rec_fibb(n-1)

def fibb_list(n):
    return [rec_fibb(i) for i in range(n)]

if __name__ == '__main__':
    print(fibb_list(6))