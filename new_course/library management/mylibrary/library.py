from tabulate import tabulate

class Library():

    def __init__(self):
        # used gpt for generate this library
        self.books_list = [
    ("To Kill a Mockingbird", "Harper Lee"),
    ("1984", "George Orwell"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Fahrenheit 451", "Ray Bradbury"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("Jane Eyre", "Charlotte Brontë"),
    ("Animal Farm", "George Orwell"),
    ("Moby-Dick", "Herman Melville"),
    ("Wuthering Heights", "Emily Brontë"),
    ("Brave New World", "Aldous Huxley"),
    ("The Picture of Dorian Gray", "Oscar Wilde"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky"),
    ("Crime and Punishment", "Fyodor Dostoevsky"),
    ("Les Misérables", "Victor Hugo"),
    ("Great Expectations", "Charles Dickens"),
    ("Dracula", "Bram Stoker"),
    ("Frankenstein", "Mary Shelley"),
    ("The Odyssey", "Homer"),
    ("The Iliad", "Homer"),
    ("The Divine Comedy", "Dante Alighieri"),
    ("War and Peace", "Leo Tolstoy"),
    ("Anna Karenina", "Leo Tolstoy"),
    ("Don Quixote", "Miguel de Cervantes"),
    ("The Stranger", "Albert Camus"),
    ("The Metamorphosis", "Franz Kafka"),
    ("The Alchemist", "Paulo Coelho"),
    ("The Little Prince", "Antoine de Saint-Exupéry"),
    ("One Hundred Years of Solitude", "Gabriel García Márquez"),
    ("Love in the Time of Cholera", "Gabriel García Márquez"),
    ("The Old Man and the Sea", "Ernest Hemingway"),
    ("A Farewell to Arms", "Ernest Hemingway"),
    ("Of Mice and Men", "John Steinbeck"),
    ("East of Eden", "John Steinbeck"),
    ("The Grapes of Wrath", "John Steinbeck"),
    ("Slaughterhouse-Five", "Kurt Vonnegut"),
    ("Catch-22", "Joseph Heller"),
    ("Beloved", "Toni Morrison"),
    ("The Color Purple", "Alice Walker"),
    ("Invisible Man", "Ralph Ellison"),
    ("The Handmaid's Tale", "Margaret Atwood"),
    ("A Clockwork Orange", "Anthony Burgess"),
    ("Life of Pi", "Yann Martel"),
    ("The Kite Runner", "Khaled Hosseini"),
    ("A Thousand Splendid Suns", "Khaled Hosseini"),
    ("Memoirs of a Geisha", "Arthur Golden"),
    ("The Book Thief", "Markus Zusak")
]
        
    def add_book(self, title, author='unknown'):
        self.books_list.append((title, author))
        return f'"{title}" from {author} succesfully added to the library'
    
    def remove_book(self, title, author):
        self.books_list.remove((title,author))
        return f'The book {title} from {author} was successfully removed from the library.'
    
    def search_book(self, title):
        results = [book for book in self.books_list if title.lower() in book[0].lower()]
        if results:
            print(tabulate(results, headers=["Title", "Author"], tablefmt="fancy_grid"))
        else:
            print(f"No book found with title containing '{title}'.")
    
    def show_books(self):
        print(tabulate(self.books_list, headers=["Title", "Author"], tablefmt="grid"))
    
library = Library()

