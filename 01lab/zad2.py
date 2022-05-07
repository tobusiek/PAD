class Worker:
    def __init__(self, number, name, age, salary):
        self.number = number
        self.name = name
        self.age = age
        self.salary = salary
    
    
    def get_salary(self):
        return self.salary


workers = {
    Worker(1, 'Adam', 1983, 1500),
    Worker(2, 'Anna', 1981, 1700),
    Worker(3, 'Błażej', 1990, 1800),
    Worker(4, 'Beata', 1992, 1600),
    Worker(5, 'Czesław', 1980, 2000),
    Worker(6, 'Cecylia', 1983, 2100),
    Worker(7, 'Daniel', 1976, 1900)
}


def avg(workers):
    salary_sum = 0
    for w in workers:
        salary_sum += w.get_salary()
    avg_salary = salary_sum / len(workers)
    return avg_salary

print("Average salary for workers is", avg(workers))

workers_aged_30_and_below = {x for x in workers if 2022 - x.age <= 30}
avg_lte_30 = avg(workers_aged_30_and_below)
print("Avg salary for workers aged 30 and below:", avg_lte_30)

workers_aged_more_than_30 = workers - workers_aged_30_and_below
avg_mt_30 = avg(workers_aged_more_than_30)
print("Avg salary for workers aged more than 30:", avg_mt_30)

if avg_lte_30 < avg_mt_30:
    print("Workers past 30 earn more")
elif avg_lte_30 > avg_mt_30:
    print("Workers below and equal 30yo earn more")
else:
    print("No difference between workers salaries")
