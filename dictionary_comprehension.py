

## numbers and square 
## normal approach
l=[1,3,4,6,5]
d={}
for i in l:
    d[i]=i**2
print(d)






## numbers and square dictionary comprehension
l=[1,3,4,6,5]
d={i:i**2 for i in l}
print(d)






## odd numbers squares with normal approach
l=[1,3,4,6,5]
d={}
for i in l:
    if i%2!=0:
        d[i]=i**2
print(d)






## odd numbers squares with dictionary comprehension
l=[1,3,4,6,5]
d={i:i**2 for i in l if i%2!=0}
print(d)






## keys is position and values is value
l=[1,3,4,6,5]
d={i:l[i] for i in range(len(l))}
print(d)  ## o/p:- {0: 1, 1: 3, 2: 4, 3: 6, 4: 5}





## example-1
l=[1,3,4,6,5]
s='ABCDE'
d={s[i]:l[i] for i in range(len(l))}
print(d)   ## o/p:- {'A': 1, 'B': 3, 'C': 4, 'D': 6, 'E': 5}






## example-2
s='aBcd'
d={i.upper():i.lower()*3 for i in s}
print(d)  ## o/p:- {'A': 'aaa', 'B': 'bbb', 'C': 'ccc', 'D': 'ddd'}








#* Enumerate Function:- 
e=enumerate([11,22,33,44,55])
print(e)  ## return--> <enumerate object at 0x00000276BA88BD80>
d={i:j for i,j in e}
print(d)







#* Zip function:-
z=zip([11,22,33,44,55],'ABCDE')
print(z)   ## return--> <zip object at 0x00000290B17EBD80>
d={i:j for i,j in z}
print(d)