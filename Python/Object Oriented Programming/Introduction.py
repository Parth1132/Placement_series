import csv

class Item:
    
    pay_rate = 0.8 #the pay rate after 20% discount
    all=[]
    def __init__(self, name: str, price: float, quantity=0):
        
        #Run Validation to the received arguments
        assert price >= 0 , f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        
        # Assign to self objects
        
        
        self.name=name
        self.price=price
        self.quantity=quantity
        
        #Actions to execute
        Item.all.append(self)
        
        
       
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod    
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
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
        return f"Item('{self.name}',{self.price},{self.quantity})"


class Phone(Item ):
    all=[]
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        
        #Run Validation to the received arguments
        assert price >= 0 , f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        
        # Assign to self objects
        
        
        self.name=name
        self.price=price
        self.quantity=quantity
        self.broken_phones = broken_phones
        
        #Actions to execute
        Phone.all.append(self)
        

phone1 = Phone("jscpjonev10",500,5,1)
print(phone1.calculate_total_price())


phone2 = Phone("jscpjonev20",700,5,2)

