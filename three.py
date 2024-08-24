x1 = input()

print("첫째 수,첫째 자리 : "+x1)

x2 = input()

print("첫째 수,둘째 자리 : " +x2)

x3 = input()

print("첫째 수,셋째 자리 : "+x3)

y1 = input()

print("둘째 수,첫째 자리 : "+y1)

y2 = input()

print("둘째 수,둘째 자리 : "+y2)

y3 = input()

print("둘째 수,셋째 자리 : "+y3)


print("첫째 수 : "+x1+x2+x3)

print("둘째 수 : "+y1+y2+y3)


z1 = int(0)
z2 = int(0)
z3 = int(0)
z4 = int(0)
z5 = int(0)
z6 = int(0)


a1 = x1
a1 = int(a1)
a2 = x2
a2 = int(a2)
a3 = x3
a3 = int(a3)
b1 = y1
b1 = int(b1)
b2 = y2
b2 = int(b2)
b3 = y3
b3 = int(b3)



if a3+b3>2: #nnp게이트
    z2 = 1
    if a3 == b3:    #nd게이트
        z1 = 1
    else:
        z1 = 0
else:
    z2 = 0
    if a3+b3==2:    #nn게이트
        z1 = 2
    elif a3+b3<2:
        if a3 == b3:    #dn게이트
            z1 = 0
        else:
            z1 = 1

print("----------------------")
print(z1)
print(z2)
print("----------------------")


if a2+b2>2: #nnp게이트
    z4 = 1
    if a2 == b2:    #nd게이트
        z3 = 1
    else:
        z3 = 0
else:
    z4 = 0
    if a2+b2==2:    #nn게이트
        z3 = 2
    elif a2+b2<2:
        if a2 == b2:    #dn게이트
            z3 = 0
        else:
            z3 = 1

print("----------------------")
print(z3)
print(z4)
print("----------------------")


if a1+b1>2: #nnp게이트
    z6 = 1
    if a1 == b1:    #nd게이트
        z5 = 1
    else:
        z5 = 0
else:
    z6 = 0
    if a1+b1==2:    #nn게이트
        z5 = 2
    elif a1+b1<2:
        if a1 == b1:    #dn게이트
            z5 = 0
        else:
            z5 = 1

print("----------------------")
print(z5)
print(z6)
print("----------------------")






if z2+z3>2:    #nnp게이트
    z3 = 0
    z4 = 1
elif z2+z3 == 2:    #nn게이트
    z3 = 2
else:
    if z2 == z3:    #dn게이트
        z3 = 0
    else:
        z3 = 1




if z4+z5>2:    #nnp게이트
    z5 = 0
    z6 = 1
elif z4+z5 == 2:    #nn게이트
    z5 = 2
else:
    if z4 == z5:    #dn게이트
        z5 = 0
    else:
        z5 = 1

print(z1)
print(z3)
print(z5)
print(z6)
