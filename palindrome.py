# checking plaindrome
x = input("enter palindrome:")


def palindrome(n):
    if n == n[::-1]:
        print("palindrome..")
    else:
        print("is not a palindrome..")


palindrome(x)
