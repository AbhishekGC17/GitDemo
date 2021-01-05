try:

    with open("simpe.txt","r") as file:
        print(file.read())
except Exception as e:

    print(e)