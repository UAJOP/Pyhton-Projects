salaries = [2000, 5000, 4000, 6000]


def new_salary(salary):
    return salary + salary * 20 / 100


for salary in salaries:
    print(new_salary(salary))


# superWay


salaries = [2000, 5000, 4000, 6000]

print(list(map(new_salary, salaries)))

# ultraSuperWay

salaries = [2000, 5000, 4000, 6000]

print(list(map(lambda salary: salary + salary * 20 / 100, salaries)))
