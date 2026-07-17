# c=int(input("give value:"))
# f=c*(9/5)+32
# k=273+c
# print(f"fahrenheit:{f}\n kelvin:{k}")
p=int(input("enter temperature:"))
l=input("enter units(K or C or F):")
k=c=f=0
ke=p+273
ce=(p- 32) * 5 / 9
fa=p*(9/5)+32

j=l
if j=="k":
  print(f"Farenheit:{fa}")
  print(f"celcius:{ce}")
elif j=="c":
  print(f"kelvin:{ke}")
  print(f"farenheit:{fa}")
elif j=="f":
  print(f"kelvin:{fa}")
  print(f"celcius:{ce}")
else:
  print("invalid input./")
