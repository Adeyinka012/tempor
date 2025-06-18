class Dad:

    def __init__(self,eye,aggressive):

      self.eye=eye

      self.aggressive=aggressive

    def display(self):

        print("Your eye color is ", self.eye)

        print("Your are aggressive ",self.aggressive)


class Son(Dad):

 def __init__(self, eye, aggressive, name,age):

  self.name=name

  self.age=age

  super().__init__(eye,aggressive)

obj=Son("blue",True,"Penguin",10)

obj.display()

obj2=Dad("Blue","False")

obj2.display()