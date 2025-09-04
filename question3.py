def a():
    list =[]
    for i in range(5):
        n = int(input())
        list.append(n)
    tup = tuple(list)
    sum =0

    for i in tup:
        sum+=i
    average = sum/5
    print("sum is",sum)
    print("average is",average)

a()