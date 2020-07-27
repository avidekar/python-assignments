with open("demofile.txt", "r") as a_file:

    # printing lines in-order
    # for line in a_file:
    #     print(line.strip())

    # printing lines in reverse
    for line in reversed(list(a_file)):
        print(line)

    # for index, line in enumerate(a_file):
    #     if index % 2 == 0:
    #         print index, line.strip()
