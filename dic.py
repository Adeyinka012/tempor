square={1:1,3:9,5:25,7:49,9:81}
for i in square:
    print(square[i])
    
test_dict={"Codingal":2,"is":2, "best":2, "for":2, "coding":2}
print("The original dictionary : " + str(test_dict))
k=2
res=0
for i in test_dict:
    if test_dict[i]==k:
        res+=1
        
print("Frequency of k is : " + str(res))