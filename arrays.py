ages= [21,34,12,45,78,12,13,25,26,27]
names=["carey","john","martin","antony","lynne","pius","kevin","sira"]
#functions
ages.append(31)
ages.sort()
ages.reverse()
print(ages)

names.sort()
print(names)

john_count=names.count("john")
print(john_count)

print(len(names))
print(len(ages))

print(sum(ages))
print("the average is: ",sum(ages)/len(ages))

print("my name is", names[0])
print(ages[0:3])
#set
#tuple
#dictionary