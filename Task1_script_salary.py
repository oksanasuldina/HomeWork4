from sys import argv


def salary_staff(production, salary_rate, prize):
    salary = production * salary_rate + prize
    return salary


script_name, productions, salary_rates, prizes = argv
print(f'Зарплата сотрудника: {salary_staff(int(productions), int(salary_rates), int(prizes))} рублей')
