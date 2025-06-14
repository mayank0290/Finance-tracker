from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default = False):
    data_str = input(prompt)
    if allow_default and not data_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(data_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy format.")
        return get_date(prompt, allow_default)
    
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    

def get_category():
    category = input("Enter the category: (I for Income, E for Expense) ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please I for Income or E for Expense.")
    return get_category()    
    

def get_description():
    return input("Enter a description: ")
 