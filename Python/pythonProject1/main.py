a=float(input('какова дистанция в первый день'))
b=float(input('требуемая дистанция'))
day=1
c=a
while a<b:
    a=a+0.1*a
    day+=1
    c=c+a
print("вы получите результат на",day,'день')


counter = 3
while counter > 0:
    print("Counter ", counter)
    counter = counter - 1
else:
    print("Done!")

