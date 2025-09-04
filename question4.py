def fun():
    list =[]
    for i in range(10):
        n= input()
        list.append(n) 
    s= set(list)
    t= tuple(list)
    print(s)
    print(t)
fun()