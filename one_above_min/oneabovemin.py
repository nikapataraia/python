def almostMin(lst) :
    if (len(lst) < 2) : return None
    mini = secmini = float('inf')
    for x in lst :
        if(mini >= x):
            mini,secmini = x,mini
        elif(secmini>=x):
            mini,secmini = mini,x
    return secmini