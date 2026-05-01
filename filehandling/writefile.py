""" Python program to write a file """

with open('file.txt', 'w') as file:
    file.writelines(['Apple','Pineapple','Grapes','Banana'])
    print()
    file.close()

