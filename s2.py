class ANIMAL:
    def __init__(self,intrval,name):
        self.intruval = intrval
        self.count = 0
        self.name = name
        
    def ready(self,val):
        rval = val % self.intruval
        if rval>0:
            return False
        self.count += 1
        return True

    def print_buns(self):
        print(self.name + ":Takes Bun: {0}".format(self.count))
              
        
r = ANIMAL(2,"RAT")
c = ANIMAL(5,"CAT")
d = ANIMAL(10,"DOG")

for j in range(100):
    if d.ready(j):
        print ("Dog Takes Bun at intervel {0}".format(j))
    elif c.ready(j):
        print ("Cat Takes Bun at intervel {0}".format(j))
    elif r.ready(j):
        print ("Rat Takes Bun at intervel {0}".format(j))
 
print("-------------------------------")
 
r.print_buns()       
c.print_buns()
d.print_buns()
