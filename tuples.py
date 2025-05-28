tuple1=("zakir", "Fareed", "david",False,3,5, 5,10)
print(tuple1)
print(len(tuple1))
print(tuple1.count(5))
tuple2=("h","g","y")
tuple3=tuple1 +tuple2
print(tuple3)
print(tuple1[2])
print(tuple1[-1])
print(tuple1[1:4])


weather =(1,0,0,0,0,1,0,1)
sunny=0
rainy=0
for i in range(0,8):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if(sunny > rainy):
    print("The weather is good today you do not need unbrella")
else:
    print("please carry your umbrella its raining too much today")
    