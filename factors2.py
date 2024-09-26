print('type a number in')
factors = []

number = int(input())
for i in range(number):
    if number % (i+1)==0:
        factors.append(i+1)

        print(factors) 