y=int(input("give year:"))
l=False
if y%100==0 and y%400!=0:
    l=False
elif y%4==0:
    l=True

else:
    l=False
print(l)