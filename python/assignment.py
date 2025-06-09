'''if children has age less than 12 years then they will pay 100,
they will pay 200 (for 12-60)
if >60 we have price 150 by 2018
hence it has increased by 10% in 2024 apply 5% disc 
if bought more than 5 tickets . calculate a ticket price by the
cinema ticket price calc
'''

def movieTicket(a,n):
  
    if a < 12:
        price=n*(100+0.1*100)
    elif a >= 12 & a<=60:
        price=n*(200+0.1*200)
    else:
        price=n*(150+0.1*150)
    
    if n>5:
        price-=price*0.05

    return round(price,2)

a=int(input("Enter your age:"))
b=input("Enter the Movie name:")
n=int(input(f"How many tickets do you want for {b} : "))
print(f"The total ticket price amounts to : {movieTicket(a,n)}")