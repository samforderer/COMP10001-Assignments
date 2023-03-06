import random 

#I, Sam Forderer, 000355553, certify that this work is my own effort and that I have not allowed anyone else to copy from it. 

# generate random amount with integer from [0,20] and add random decimal value with two places 
amount = random.randint(0,20) + round( random.randint( 0, 100) /100 , 2 )
print("You owe: $",amount)

# take input from user for payment and round to nearest nickel 
# ASSUME valid input is a float that is > than amount
payment = float(input("How much are you paying?: "))
payment = round(payment / 0.05) * 0.05

# calculate change and round to nearest nickel
change = round(round(payment - amount, 2) / 0.05) * 0.05
change = round(change, 2) 
if(change > 0):
    d = 0
    q = 0
    i = 0
    n = 0

    d = int(change)
    change = round(change - d, 2)
    print(change)
    if(change > 0):
        print(change)
        q = int(change // 0.25)
        change = change - (q * 0.25)  
        
        print(change)
        i = int(change // 0.10)
        change = change - (i * 0.10)

        print(change)
        n = int(change // 0.05)
        change = change - (n * 0.05)
        
        print(change)

    print("You got ", d, "dollars, ", q, "quarters, ", i, "dimes and", n, "nickels back in change")
else:
    print("No change is owed")
