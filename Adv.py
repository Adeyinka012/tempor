# number=[1,2,4,6,7,8]
# even=[x for x in number if x %2 ==0]
# print("List of even number from number is: ",even)


# # dictionary comprehension
# myDict={str(x):x**2 for x in [1,3,7,8,9,5]}
# print(myDict)

# def square(n):
#     return n*n
# number=(1,2,3,4)
# result=map(square,number)
# print(list(result))


# name=["Zakir","Fareed","david","kevin"]
# grade=[3,5,7,10]
# mapped=zip(name,grade)
# print(list(mapped))


ages=[19,45,12,78]
for age in ages:
    if age <18:
        print("You are not allowed to vote since you are ", age, "years old")
        exit()
    else:
        print("you can vote")