'''print("ok")
age = 9

if age <20:
    print(age)

name = "omar"

if name is "Ahmed":
    print(name)
elif name is "omar":
    print(name)
else:
    print("no name")

foods = ['chicken','turkey','eggs']

for f in foods:
    print("The length of ",f," is ",len(f))
  print(len(f))


for x in range(5,10,2):
    print(x)

x = 1

while x < 10:
    print(x)
    x+=1


def function():
    print("my function printed")

def Conversion(bit):
    amount = bit*5
    print(amount)

bit = 9
Conversion(bit)


class Enemy:
    life = 3

    def attack(self):
        print("ouch")
        self.life -= 1
    def checklife(self):
        if self.life<=0:
            print("Enemy dead")
        else:
            print(self.life, "life left")

enemy1 = Enemy()

enemy1.attack()
enemy1.checklife()
enemy1.attack()
enemy1.attack()
enemy1.checklife()



def health(age,apples,cigs):
    answer = (100-age) + (apples *3) - cigs
    print(answer)

mylist = [27,9,10]

health(mylist[0],mylist[1],mylist[2])
health(*mylist)
'''

'''

'''

y = 10 

if y != 9 or y != 11:
    print("ok")