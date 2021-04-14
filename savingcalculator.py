monthly_income = input("How much money you get from your parent every month: ")
saving = input("How many percent do you want to save: ")
product = input("What do you want to buy: ")
price = input("what is the price for {0}: ".format(product))

saving_amount = 0


def saving_amount_calculation(income, percentage):
    return income * (percentage / 100)

def length_saving(price, saving_amount):
    return price / saving_amount

if monthly_income:
    saving_amount = saving_amount_calculation(int(monthly_income), int(saving))
    length = length_saving(int(price), saving_amount)
    print("You need to save money for {0} months".format(round(length)))
