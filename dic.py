emp_1={122:45 ,123:89,567:69,670:69}
emp_2={222:67,566:90}
emp_1.update(emp_2)
print(emp_1)
emp_3=emp_1.copy()
print(emp_3)
emp_1.popitem()
print(emp_1)
emp_1.pop(567)
print(emp_1)
emp_1.clear()
print(emp_1)
for i in emp_1.keys():
    print(i)