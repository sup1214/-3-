#1330

A, B = input().split()
A = int(A)
B = int(B)
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')

#9498
score = int(input())

if score in range(90, 101):
    print("A")
elif score in range(80, 90):
    print("B")
elif score in range(70, 80):
    print("C")
elif score in range(60, 70):
    print("D")
else:
    print("F")

#2753
A = input()
A = int(A)

if A % 4 == 0:
    if A % 100 == 0:
        if A % 400 == 0:
            print('1')
        else:
            print('0')
    else:
        print('1')
else:
    print('0')


#14681

x = int(input())
y = int(input())


if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
else:
    print(3)
