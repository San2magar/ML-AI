'''Train ticket calculator based on distance and class
WAp that takes distance in KM where we do have class 1 belongs to first class 2 belongs to 2nd class and 3 belong to sleeper
fare chart per km
1st class 5 $, 2nd class 3 $ ,3rd class 1$
if dist>500km 10% disc'''

def ticketCalculator(c, d):
    if c == 1:
        price = 5
    elif c == 2:
        price = 3
    elif c == 3:
        price = 1
    else:
        return "Invalid class"

    if d > 500:
        price -= price * 0.1  # or price *= 0.9

    return round(price, 2)

c = int(input('Select train class [First Class : 1, Second Class : 2, Sleeper : 3]: '))
d = float(input("Enter distance to travel (in km): "))
print(f"The ticket fare of the passenger is: {ticketCalculator(c, d)} $")