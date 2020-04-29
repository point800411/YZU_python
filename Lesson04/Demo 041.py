e1 = {'name':'John', 'salary':50000, 'program':['Java', 'Python']}
e2 = {'name':'Mary', 'salary':60000, 'program':['VB', 'Python']}
e3 = {'name':'Bob', 'salary':70000, 'program':['C#']}
emps = [e1, e2, e3]

python = []
lan = 'Python'
for emp in emps:
    for p in emp['program']:
        if p == lan :
            python.append(emp['name'])

print(python)
