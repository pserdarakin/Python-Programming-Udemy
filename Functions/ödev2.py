def ebob(a,b):
    i=1
    ebob=1
    while (i <= a and i<=2):
        if (not(a%i) and not(b%i)):
            ebob=i
        i += 1
    return(ebob)
a=int(input('Sayı-1:'))
b=int(input('Sayı-2:'))
print('Ebob:',ebob(a,b))

