class Layar:
    def __init__(self,d,t,id):
        self.datasize = d
        self.datatype =t
        self.id = id
list = []
list.append(Layar(10,'y',0))
list.append(Layar(12,'y',1))
list.append(Layar(8,'y',2))
list.append(Layar(6,'y',3))
list.append(Layar(18,'y',4))

for l in list:
    print(l.datasize)
    l.datasize += 1

i = len(list)
print ('Countlist 1:{0}'.format(i))

for l in list:
    print(l.datasize)

list2 = list


list2.insert(2,Layar(100,'n',5))
i = len(list2)
print ('Count list2:{0}'.format( i))

for l in list2:
    print(l.datasize)

i = len(list)
print ('Count:{0}'.format( i))
for l in list:
    print(l.datasize)