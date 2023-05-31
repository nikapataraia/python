x = input()
onind = 0
while(x[onind] != ' '):
    onind = onind + 1
y = int(x[0:onind])
while(y <= 0 and y > 1000):
    x = input()
    y = int(x[0:onind])
onind = onind + 1
newstr = x[onind:]
myar = newstr.split(' ')
if(len(myar) > y):
    myar = myar[:y]
myar = list(map(lambda x : float(x),myar))

for ind in range(len(myar)):
    if(myar[ind] < 0):
        myar[ind] = - myar[ind]
print(myar)
def norm(num):
    res = 0
    for el in myar:
        res = res + el**num
    return res**(1/num)

def infnorm():
    max = 0
    for el in myar:
        if(el > max):
            max = el
    return max

print(str(round(norm(1) , 6)) + " " +str(round(norm(2) , 6)) + " " +str(round(norm(3),6)) + " " +str(round(infnorm() , 6)))
