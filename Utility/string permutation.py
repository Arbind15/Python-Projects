"""This program calculate the number of possible combination of given string"""

def fact(number):
    """Return the factorial of number"""
    prod=1
    ind=number
    if number==0:
        return 1
    for temp in range(1,number):
        prod=prod*ind
        ind-=1
    return prod

def per(string):
    "this function return the combination of list"
    i=0
    list = []
    permutation=tim(string)
    for i in range(len(string)):
        temp=permutation[i:i + len(string)]
        srt=""
        for we in temp:
            srt=srt+we
        list.append(srt)
        i += 1
    return list

def tim(string):
    permutation = []
    times=fact(len(string))
    for itm in range(times):
        for char in string:
            permutation.append(char)
    return permutation
global tem,i
def rev(strng):
    global tem,i
    i=0
    for itm in strng:
        if len(tem) == fact(len(string)):
            return tem
        tem.append(''.join(reversed(itm)))
        i+=1
    rev(strng)


def final(strng):
    final=[]
    list1=per(strng)
    lis2=rev(list1)
    print(rev(string))
    print(len(rev(string)))

string=str(input())
tem=[]
temp_string=""
i=0
l=len(string)
final(string)