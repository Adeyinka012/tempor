def plane_cost(city):
    if "lagos"==city:
        return 183
    elif 'Nairobi'==city:
        return 220
    elif 'Tanpa'==city:
        return 222
    elif 'los angeles'==city:
        return 475
def rental_car_cost(days):
    if days >=7:
        return 40*days -50
    elif days >=3:
        return 40*days-20
    else:
        return 40*days
def hotel_cost(night):
    return 140 *night
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_cost(city) + spending_money
print("cost of rental car", rental_car_cost(7))
print("cost of the plane ride", plane_cost("Nairobi"))
print("The total cost of hotel room",hotel_cost(7))
print("The total cost of the trip: ", trip_cost("Nairobi",7,80000))
print(trip_cost("los angeles", 8,10000))