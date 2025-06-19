class pc:
    def __init__(self):
        self.__maxprice=1500
        
    def sell(self):
        print("selling price of a pc:{}".format(self.__maxprice))
    
    def setmaxprice(self,price):
        self.__maxprice=price
c=pc()
c.sell()
c.__maxprice=3000
c.sell
c.setmaxprice(9000)
c.sell()
        