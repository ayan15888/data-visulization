def fun(list):
    vowels =["a","e","i","o","u"]
    arr=[]

    for i in list:
        if i[0].lower() in vowels:
           arr.append(i)
                
    print(arr)            

list =["sanjay","sneha","sanjay2","ayan"]
fun(list)