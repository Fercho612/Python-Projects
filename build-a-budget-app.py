class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
    
    def deposit(self, amount, description = ""):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.balance -= amount
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True
    
    def check_funds(self, amount):
        return True if self.balance >= amount else False

    def __str__(self):
        title = f"{self.name:*^30s}\n"
        body = ""
        for item in self.ledger:
            body += f"{item['description']:<23.23s}{item['amount']:>7.2f}\n"

        return title + body + f"Total: {self.balance:.2f}"

def create_spend_chart(categories):
    spend_for_category = []

    for index, category in enumerate(categories):
        spend_for_category.append(0)
        for item in category.ledger:
            if item['amount'] < 0:
                spend_for_category[index] += abs(item['amount'])
    
    total = sum(spend_for_category)

    for index, spend in enumerate(spend_for_category):
        spend_for_category[index] = spend / total * 100

    title = "Percentage spent by category\n"
    chart_bars = ""
    for num in range(100, -10, -10):
        chart_bars += f"{num:>3}|"
        for percentage in spend_for_category:
            chart_bars += f"{'o':^3}" if num <= percentage else "   "
        chart_bars += ' \n'
    chart_bars += f"    {'---'*len(categories)}-"
    
    lenght_names = []
    for category in categories:
        lenght_names.append(len(category.name))
    max_lenght = max(lenght_names)

    for letter in range(0, max_lenght):
        chart_bars += "\n"
        chart_bars += "    "
        for index in range(0, len(categories)):
            if len(categories[index].name) <= letter:
                 chart_bars += " " * 3
            else:
                chart_bars += f"{categories[index].name[letter]:^3}"
        chart_bars += " "
    return title + chart_bars



food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(400, 'groceries')
clothing = Category('Clothing')
clothing.deposit(1000, 'inital deposit')
clothing.withdraw(500, 'groceries')
auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(100, 'groceries')

print(create_spend_chart([food, clothing, auto]))