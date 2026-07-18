def getURL():
    print("_______Sign in_______\n")
    name = input('Name:')

    print(f"Welcome back {name}!!!\n")

    file = open('links.txt', 'r')
    urls = file.readlines()
    file.close()

    print("Your links--> ", end="")
    for line in urls:
        print(line.strip(), "\n")

    return urls
