class hotel:
    def __init__(self,category, number, price):
        self.number = number
        self.category = category
        self.price = price
        self.booked = False
        



    def is_reserved(self):
         return f"{self.number} by {self.category} and {self.price}" 
        
    def is_not_reserved(self):
        self.is_checked_out = False
    
    def __str__(self):
        return f"{self.number} by {self.category} and {self.price}"
    
room = hotel('5star',89, 10000)

room.is_reserved()