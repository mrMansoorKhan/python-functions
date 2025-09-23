def calc_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i

    print(fact)

m = int(input("enter the number :"))

calc_fact(m)