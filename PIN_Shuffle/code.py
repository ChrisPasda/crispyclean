
user = input('bitte Namen eingeben').lower()
i = 0
preName = user[0]+user[1]
print(user[0])
for char in user:
    i+=1
    if(char == ' '):
        surName = user[i]
    else:
        surName = ''

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
codes = {1:1,2:1,3:1,4:2,5:2,6:2,7:3,8:3,9:3,10:4,11:5,12:5,13:6,14:6,15:6,16:7,17:7,18:7,19:8,20:8,21:8,22:9,23:9,24:9,25:0,26:0}

#alphabetList = [i for i in alphabet]

def shuffle(chars):
    myList = []
    for char in chars:
        j = 0
        for letter in alphabet:
            j+=1
            if char == letter:
                myList.append(j)
                myList.append(j+2)
    return myList

for item in (shuffle(preName)):
    for code in codes:
        if item == code:
            print(codes.get(code))
