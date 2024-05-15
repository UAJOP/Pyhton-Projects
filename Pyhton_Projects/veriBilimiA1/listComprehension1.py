salaries = [2000, 5000, 4000, 6000, 1000, 3000]


# classicWay

def new_salary(salary):
    return salary + salary * 20 / 100


new_salaries = []

for salary in salaries:
    new = new_salary(salary)
    new_salaries.append(new)

for salary in new_salaries:
    if salary > 3000:
        print(salary)

# list comprehension

salaries = [2000, 5000, 4000, 6000, 1000, 3000]
last_list = [salary * 2 for salary in salaries if salary < 3000]
print(last_list)

# 2 koşul

salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

last_salaries = [item * 2 if item <= 5000 else item * 1 for item in salaries]

print(last_salaries)

