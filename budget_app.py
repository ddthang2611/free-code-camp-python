class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance
        
    def check_funds(self, amount):
        current_balance = self.get_balance()
        return amount <= current_balance
        
    def deposit(self, amount, description = ""):
        new_transaction = {"amount": amount, "description": description}
        self.ledger.append(new_transaction)
    
    def withdraw(self, amount, description = ""):
        withdraw_amount = 0 - amount
        withdraw_result = False
        if self.check_funds(amount):
            withdraw_result = True
            new_transaction = {"amount": withdraw_amount, "description": description}
            self.ledger.append(new_transaction)
        else:
            withdraw_result = False
        return withdraw_result
                
    def transfer(self, amount, destination):
        transfer_result = False
        if self.check_funds(amount):
            transfer_result = True
            withdraw_description = f"Transfer to {destination.name}"
            self.withdraw(amount, withdraw_description)
            transfer_description = f"Transfer from {self.name}"
            destination.deposit(amount, transfer_description)
        else:
            transfer_result = False
        return transfer_result          
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        
        items = ""
        for transaction in self.ledger:
            desc = f"{transaction['description'][:23]:23}"
            amount = f"{transaction['amount']:>7.2f}"
            items += f"{desc}{amount}\n"
            
        total = total = f"Total: {self.get_balance():.2f}"
        return title + items + total
            
def create_spend_chart(categories):
    
    spent_list = []
    for category in categories:
        total_withdraw = 0
        for item in category.ledger:
            if(item["amount"] < 0):
                total_withdraw -= item["amount"]
        spent_list.append(total_withdraw)
    
    total_spend = sum(spent_list)
    amount_percentages = []
    
    for item in spent_list:
        if total_spend > 0:
            percent = (item / total_spend) * 100
            round_percent = (percent // 10) * 10
            amount_percentages.append(round_percent)
        else:
            amount_percentages.append(0)
    
    chart = "Percentage spent by category\n"    
    counter = 100
    while counter >= 0:
        chart_line = f"{counter:3}| "
        for percent in amount_percentages:
            if percent >= counter:
                chart_line += "o  "
            else:
                chart_line += "   "
        counter -= 10
        chart += chart_line + "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"  
                
    extra_height = max(len(category.name) for category in categories)
    for i in range(extra_height):
        chart += "    "
        for category in categories:
            try:
                chart += f" {category.name[i]} "
            except IndexError:
                chart += "   "
        
        chart += " "
        if i < extra_height - 1:
            chart += "\n"
    print(chart)
    return chart
    
market = Category("Market")
market.deposit(100)
market.deposit(900, 'deposit')
market.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')

supermarket = Category("Supermarket")
supermarket.deposit(1000, 'deposit')
supermarket.withdraw(10.15, 'groceries')
supermarket.withdraw(15.89, 'restaurant and more food for dessert')

create_spend_chart([market, supermarket])