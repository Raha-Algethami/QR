def getData():
    print("_______Sign in_______\n")
    name = input('Name:')

    print(f"Welcome back {name}!!!\n")

    file = open('links.txt', 'r')
    lines = file.readlines()
    file.close()

    return lines
