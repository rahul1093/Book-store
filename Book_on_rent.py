class Book_Store:
    """In class we define instance variable which can be accessed
    inside of instance method"""

    def __init__(self, name, days, cate='no catg'):
        self.bookName = name
        self.Noofdays = days
        self.bookCategory = cate

    def __str__(self):
        return f'\n {self.__dict__}'

    def __repr__(self):
        return str(self)

    def book_rent(self):
        """In this instance method we give prices before the alter new prices"""
        if self.bookCategory == 'no catg':
            print("Total charge on book Rs:", self.Noofdays * 1)

        elif self.bookCategory == 'regular' or self.bookCategory == 'fiction' or self.bookCategory == 'novel':
            if self.bookCategory == 'regular':
                print("Total charge on book Rs:", self.Noofdays * 1.5)

            elif self.bookCategory == 'fiction':
                print("Total charge on book Rs:", self.Noofdays * 3)

            else:
                print("Total charge on book Rs:", self.Noofdays * 1.5)

    def book_rent_after_alter(self):
        """In this instance method we give new prices for rent"""
        if self.bookCategory == 'regular' or self.bookCategory == 'novel':
            if self.bookCategory == 'regular':
                if self.Noofdays == 2:
                    print("Total new charge on book Rs:", self.Noofdays * 1)
                elif self.Noofdays > 2:
                    print("Total new charge on book Rs:", self.Noofdays * 1.5)
                elif self.Noofdays < 2:
                    print("Total new charge on book Rs:", self.Noofdays * 2)

            elif self.bookCategory == 'novel':
                if self.Noofdays >= 3:
                    print("Total new charge on book Rs:", self.Noofdays * 1.5)
                elif self.Noofdays < 3:
                    print("Total new charge on book Rs:", self.Noofdays * 4.5)

        else:
            print("please provide correct catagory..!")


b = Book_Store
b1 = Book_Store(name="aaaa", days=0, cate='novel')
print(b1)
b.book_rent(b1)
b.book_rent_after_alter(b1)
