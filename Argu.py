def total_bill(bill,tip):
    total= bill * (1 + 0.01 *tip)
    total= round(total,2)
    print("Please pay total of $", total)
total_bill(150,20) 

def cube(number):
    return number*number*number
def by_three(number):
    if number % 3 ==0:
        return cube(number) 
    else:
        return False
print(by_three(3))  