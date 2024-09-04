grades=[[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a=grades[0]
a1=(sum(a))/(len(a))

b=grades[1]
b1=(sum(b))/(len(b))

c=grades[2]
c1=(sum(c))/(len(c))

d=grades[3]
d1=(sum(d))/(len(d))

e=grades[4]
e1=(sum(e))/(len(e))

empty_list = []
empty_list.append(a1)
empty_list.append(b1)
empty_list.append(c1)
empty_list.append(d1)
empty_list.append(e1)


res=list(students) # Преобразовала в список
res.sort()  # Отсортировала по алфавиту


dictionary = {}
for i in range(0, len(res)):
   dictionary[res[i]] = empty_list[i]

print(dictionary)
