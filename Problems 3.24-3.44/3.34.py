print("Muhammad Osama - 18B-003-CS - Sec'A'")
print("Detailed Assignment")
print("Problem No: 3.34 ")

def pay(hourly, hours):
    print('hourly wage: ', hourly, 'hr')
    print('hourly pay: ','10$')
    if hours >= 40:
        sal = 40 * hourly
        over_time = sal + hourly * (hours - 40) *1.5
        return over_time
    else:
        not_over_time = hours * hourly
        return not_over_time
