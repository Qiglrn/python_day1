print("hello", "world", sep="-",end="\n")
print("hello", "world", sep="-",end="\n")
hello = 'hello world'
product = 9+9
savenumber = product
print (savenumber)
print (product)
print (hello)

li = [1, '2', 3.0, 4j, None,True]
li2 = li
print(li is li2)
print('id of li and li2 are ', id(li),id(li2))
print (li+li)
print (type(li))
for i in li: print (i, type(i), id(i))
print('T = True + True =', True+True)
print(dir(li))
li.index(3.0)
print (li.index(3.0))
li.append('mine')
print (li)
li[-1] = 'yours'
print (li)
li3 = li.copy()
print(li is li3)
print('id of li and li3 are ', id(li),id(li3))
tu = (1,5,4,7,8,1,4)
print(set(tu))
newdict = {'a':1, 'b':2}
print(newdict)
def addition(n):
    """"return a list of squares
    >>> list_power()
    """"
    li = []
    for i in range(1,n+2):
        #print(i**2)
        li.append(i**2)
    #print()
    return li
for i in addition(10):
    print(i, end = ',')

print ("third file to check if the diff is compareation between iniatial and new file")

print(__name__)

if __name__ == "__main__":
    for i in addition(5):
        print(i)
print("First commit")
