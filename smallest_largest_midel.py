list=[22,33,44,56,78,90,69,85,23,21,55]
list.sort()
print(list)
#smallest number 
print(list[0:1])
#laargest number
list.reverse()
print(list[0:1])
#midel number
sorted_list=sorted(list)
n =len(sorted_list)
median=sorted_list[n//2]
print(median)

