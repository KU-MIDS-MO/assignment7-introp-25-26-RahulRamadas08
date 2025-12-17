def make_account(initial_balance):
    balance = initial_balance
    
    def deposit(money):
        nonlocal balance
        
        if money < 0:
            raise ValueError
        else:
            balance += money
            
        return balance
    
    def withdraw(money):
        nonlocal balance
        
        if (money < 0) or (money > balance):
            raise ValueError
        else:
            balance -= money
            
        return balance
            
    return deposit, withdraw
