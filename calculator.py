n = int(input("give 1 number:"))
m = int(input("give 2 number:"))
opt = input("give operation(+,*,-,/):")
if opt == "+":
    print(f"{n}+{m}={n+m}.")
elif opt == "-":
    print(f"{n}-{m}={n-m}.")
elif opt == "*":
    print(f"{n}*{m}={n*m}")
elif opt == "/":
    if m != 0:
        print(f"{n}/{m}={n/m}")
    else:
        print("undefine.")
else:
    print("error:invalid operator.")
