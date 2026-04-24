class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print("-" * 20)

book1 = Book("Không Gia Đình", "Hector Malot", 1878)
book2 = Book("Hai Số Phận", "Jeffrey Archer", 1979)

book1.display_info()
book2.display_info()