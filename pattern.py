# print("Half pyramid pattern of stars (*):")
# row= int(input("Enter the number of rows:  "))
# for i in range(row):
#     for j in range(i + 1):
#         print("* ", end="")
#     print()

rows=int(input("Please enter the total number of rows "))
number = 1
for i in range(1,rows + 1):
    for j in range(1, i + 1):
        print(number, end='')
        number+=1
    print()    