a = int(input('введите число '))
c = a // 1000
for i in range (1 , c+1) :
    print('M',end='')
k = (a%1000)//100
if k >=1 and k<=3 :
    for i in range (1 , k+1) :
        print ('C',end='')
elif i == 4 :
    print ('CD')
elif k>=5 and k<=8 :
    print ('D',end='')
    for i in range (1, k-4) :
            print ('C',end='')
elif i == 9 :
    print('CM')

k = (a%100)//10
if k >=1 and k<=3 :
    for i in range (1 , k+1) :
        print ('X',end='')
elif i == 4 :
    print ('XL')
elif k>=5 and k<=8 :
    print ('L',end='')
    for i in range (1, k-4) :
            print ('X',end='')
elif i == 9 :
    print('XC')
    
k =a%10
if k >=1 and k<=3 :
    for i in range (1 , k+1) :
        print ('I',end='')
elif i == 4 :
    print ('IV')
elif k>=5 and k<=8 :
    print ('V',end='')
    for i in range (1, k-4) :
            print ('I',end='')
elif i == 9 :
    print('IX')
