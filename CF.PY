class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if(self.a < other.a):
            return "obl is less than obz"
        else:
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "both object one and object two are equal"
        else:
            return "both object are not equal"
ob1=A(2)
ob2=A(3)
print("Passed value: ", ob1.a,ob2.a)
print(ob1 < ob2)

class Flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + '('+ self.meaning + ')'
flash=[]
print("Welcome to flashcard application")
while(True):
    word=input("Enter the name you want to add to flashcard")
    meaning=input("Enter the meaning of the word:  ")
    flash.append(Flashcard(word,meaning))
    option=int(input("Enter 0, if you want to add another flashcard otherwise enter 1 :  "))
    if(option):
        break
    print("\nYour flashcard")
    for i in flash:
        print(">", i)
    