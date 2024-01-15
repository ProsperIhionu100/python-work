# parent class 
class LibaryItem:
    def __init__(self,title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_checked = False
        
    def Check_out(self):
        self.is_checked_out = True
        
    def check_in(self):
        self.is_checked_out = False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    
# Child Classes

class Book(LibaryItem):
    def __init__(self, title, author, item_id , num_pages):
        super().__init__(title, author, item_id)
        self.num_pages =num_pages
        
        
class Magazine(LibaryItem):
    def __init__(self, title, author, item_id,issue_number):
        super().__init__(title, author, item_id)
        self.issue_number =issue_number
        
class DVD(LibaryItem):
    def __init__(self, title, author, item_id, run_item):
        super().__init__(title, author, item_id)
        self.run_item = run_item
        
 #Libary class
 
class Libary:
    def __init__(self,):
        self.catalog = []
        
    def add_item(self, item):
        self.catalog.append(item)
        
    def remove_item(self, item):
        self.catalog.remove(item)
    
    def display_catalog(self):
        for Item in self.catalog:
            print(Item)
    
    def search_catalog(self, search_string):
        results = []
        for item in self.catalog:
            if search_string.lower() in item.title.lower() in item.author.lower():
                results.append()
            return results
            
            
#Example usage 
library = Libary()

book1 = Book('The Great Gatsby', 'F.Scott Fitzegerald', '12345',180)

book2 = Book('To kill a MockingBird','Harper Lee', '67890' ,281)

magazine1 = Magazine('National Geographic', 'Various','13579', 256)

magazine2 = Magazine("The Economist", "Various","24680",96)

dvd1 = DVD('The Godfather', 'Francis Ford coppola','10101',175)

dvd2 = DVD('The Shawshank Redemption', 'Frank Darabont', '20202',142)

print('Testin __str', )

library.add_item(book2)
library.add_item(magazine1)
library.add_item(magazine2)
library.add_item(dvd1)
library.add_item(dvd2)

print('Displaying  the libary catalog :')
library.display_catalog()

print("\n searching for  books by 'Fitzgerrald':")
result = Libary.search_catalog('Fitzgerrald')
for item in result:
    print(item)
    
print("\nchecking out 'The great gatsby':")
book1.Check_out()
print(f"Is 'The Great Gatsby 'checked out ?{book1.is_checked_out}")

print("\nchecking in 'The great gatsby':")
book1.Check_in()
print(f"Is 'The Great Gatsby 'checked out ?{book1.is_checked_out}")