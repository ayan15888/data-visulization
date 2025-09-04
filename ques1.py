sentence = "Jkf sdf sdfsdf sdfs sdfsf sdfsf"

print(sentence.lower())

words = sentence.split()

dict ={}

for i in words:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] =1

print(dict)