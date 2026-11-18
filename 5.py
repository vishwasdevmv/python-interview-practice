class Mobile:
    def __init__(self,model,price):
        self.model=model
        self.price=price
        
    def display(self):
        print("Model:",self.model)
        print("Price:",self.price)

obj = Mobile("Samsung", 20000)
obj.display()