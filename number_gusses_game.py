import random
n = random.randint( 1, 100)
a = -1
gusses = 1
while a != n:
    
    a = int(input("guess the number:"))
    if a > n:
        print("lower number please")
        gusses +=1
    elif a < n:
        print("Higher number please")
        gusses +=1
print(f"you gussed the number {n} correctly in {gusses} attempts !")       

