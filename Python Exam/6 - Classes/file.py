if __name__ == '__main__':
    with open("file.txt", "w") as f:
        for i in range(1, 101):
            f.write(f"{i}\n")

    with open("file.txt") as f:
        for i in f:
            print(int(i)*2)

    with open("file.txt") as f:
        print(sum([int(i) for i in f.readlines()]))


     # Second solution

    with open("file.txt", "w+") as f:

        for i in range(1, 101):
            f.write(f"{i}\n")
        f.seek(0)
        int_list = [int(i) for i in f.readlines()]
        for i in int_list:
            print(i*2)
        print(sum(int_list))