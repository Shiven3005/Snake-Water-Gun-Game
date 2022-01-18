import random
def gamewin(comp,user):
    if comp==user:
        return None
    elif comp=='s':
        if user=='w':
            return False
        elif user=='g':
            return True
    elif comp=='w':
        if user=='g':
            return False
        elif user=='s':
            return True
    elif comp=='g':
        if user=='s':
            return False
        elif user=='w':
            return True    





print("Computer turn :Snake(s) ,WATER(w) , GUN(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

user=input("Your turn :Snake(s) ,WATER(w) , GUN(g)?")
a=gamewin(comp,user)

print(f"Computer choose {comp}")
print(f"You choose {user}")

if a==None:
    print("Your match is tie!")
elif a:
    print("You win , hurrayyyyyy")
else:
    print("You loose!,Sorry PLay again")
