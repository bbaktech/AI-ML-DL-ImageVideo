class RAT:
    def __init__(self):
        self.intruval = 1
        self.count = 0
        self.fdcnt = 0

    def ready(self,val):
        if self.fdcnt == 0 :
            self.count += 1
            self.fdcnt = self.intruval
            return True
        self.fdcnt -=1
        return False

    def print_buns(self):
        print("RAT Takes:  {0}".format(self.count))

class CAT:
    def __init__(self):
        self.intruval = 4
        self.count = 0
        self.fdcnt = 0
    def ready(self,val):
        if self.fdcnt == 0 :
            self.count += 1
            self.fdcnt = self.intruval
            return True
        self.fdcnt -=1
        return False
    def print_buns(self):
        print("CAT Takes Bun: {0}".format(self.count))

class DOG:
    def __init__(self):
        self.intruval = 9
        self.count = 0
        self.fdcnt = 0

    def ready(self,val):
        if self.fdcnt == 0 :
            self.count += 1
            self.fdcnt = self.intruval
            return True
        self.fdcnt -=1
        return False

    def print_buns(self):
        print("DOG Takes Bun: {0}".format(self.count))

c = CAT()
r = RAT()
d = DOG()

for j in range(100):
    if d.ready(j):
        print ("Dog Takes Bun at intervel {0}".format(j))
    elif c.ready(j):
        print ("Cat Takes Bun at intervel {0}".format(j))
    elif r.ready(j):
        print ("Rat Takes Bun at intervel {0}".format(j))

r.print_buns()
c.print_buns()
d.print_buns()
