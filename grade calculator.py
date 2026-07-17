mat = int(input("give maths score:"))
sci = int(input("give science score:"))
eng = int(input("give english score:"))
total = mat+eng+sci
average = (mat+eng+sci)/3
percentage= (total/300)*100
print(f"total score:{total}")
print(f"average score:{average}")
if percentage > 90:
    print("grade:A")
elif percentage > 80 and percentage <= 90:
    print("grade :B")
elif percentage > 70 and percentage <= 60:
    print("grade:c")
else:
    print("grade :d")
