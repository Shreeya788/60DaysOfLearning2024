try:
    with open('file_doesnot_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")