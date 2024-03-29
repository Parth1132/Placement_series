import csv

class Item:
    
    pay_rate = 0.8 #the pay rate after 20% discount
    all=[]
    def __init__(self, name: str, price: float, quantity=0):
        
         #Run Validation to the received arguments
        assert price >= 0 , f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        
        # Assign to self objects
        
        
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
            return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
        
        
       
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod    
    def instantiate_from_csv(cls):
        with open('Python/Object Oriented Programming/item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        #we will count out the floats that are point zero
        # For example 5.0,10.0
        if isinstance(num,float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
            
    
    
            
        
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

    
