stock_prices = [('APL',200),('GOOG',400),('MSFT',100)]

for item in stock_prices:
    print(item)


for ticker, prices in stock_prices:
    print(ticker)
    print(prices)



work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    #Return
    return(employee_of_month,current_max)
    
print(employee_check(work_hours))