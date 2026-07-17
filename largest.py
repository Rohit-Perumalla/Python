a=input("give values with separate ',':")
x,y,z=a.split(",")
n1=int(x)
n2=int(y)
n3=int(z)
gr=0
if n1>=n2:
    if n1>=n3:
        gr=n1
    else:
        gr=n3
elif n2>n1:
    if n2>n3:
        gr=n2
    else :
        gr=n3
elif n3>n1:
    if n3>n2:
        gr=n3
    else:
        gr=n2

print(f"gratest :{gr}")
