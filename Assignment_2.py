n = int(input("Enter your first number: "))
m = int(input("Enter your first number: "))
p = input("Choose your function(+,-,*,/): ")

def add(a,b):
    result = a+b
    return result

def sub(a,b):
    result = a-b
    return result

def multi(a,b):
    result = a*b
    return result

def div(a,b):
    result = a/b
    return result

if p == "+":
    answer = add(n,m)
    print(answer)

elif p == "-":
    answer = sub(n,m)
    print(answer)

elif p == "*":
    answer = multi(n,m)
    print(answer)

elif p == "/":
    if p!=0:
        answer = div(n,m)
        print(answer)
    else:
        print("Cannot divide by zero!")



