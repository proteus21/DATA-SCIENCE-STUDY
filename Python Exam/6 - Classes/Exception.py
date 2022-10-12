if __name__ == '__main__':
    try:
        a=(1/0)
    except Exception as e:
        print(e.__class__, e)
    else:
        print(a)