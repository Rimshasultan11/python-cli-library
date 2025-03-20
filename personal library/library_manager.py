import json
from colorama import Fore, Style, init

init(autoreset=True)

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        print(Fore.CYAN + Style.BRIGHT + "📖 Adding a New Book:")
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print(Fore.GREEN + "✅ Book added successfully!\n")

    def delete_book(self):
        print(Fore.RED + "🗑️ Deleting a Book:")
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print(Fore.GREEN + "✅ Book removed successfully!\n")
                return
        print(Fore.YELLOW + "⚠️ Book not found!\n")

    def find_book(self):
        print(Fore.CYAN + "🔎 Searching for a Book:")
        search_text = input("Enter title or author to search: ").lower()
        found_books = [book for book in self.book_list if search_text in book["title"].lower() or search_text in book["author"].lower()]

        if found_books:
            print(Fore.GREEN + "📚 Matching Books:")
            for index, book in enumerate(found_books, 1):
                status = "✅ Read" if book["read"] else "❌ Unread"
                print(Fore.CYAN + f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            print(Fore.YELLOW + "⚠️ No matching books found.\n")

    def show_all_books(self):
        print(Fore.LIGHTGREEN_EX + "📚 Your Book Collection:")
        if not self.book_list:
            print(Fore.YELLOW + "⚠️ Your collection is empty.\n")
            return
        for index, book in enumerate(self.book_list, 1):
            status = "✅ Read" if book["read"] else "❌ Unread"
            print(Fore.CYAN + f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

    def show_reading_progress(self):
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        print(Fore.MAGENTA + f"📊 Total books: {total_books}")
        print(Fore.MAGENTA + f"📈 Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n============================================\n📚 Welcome to the Personal Library Manager!\n=============================================\n")
        while True:
            print(Fore.GREEN + "1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. View all books")
            print("5. View reading progress")
            print("6. Exit")
            user_choice = input("Choose an option (1-6): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.show_all_books()
            elif user_choice == "5":
                self.show_reading_progress()
            elif user_choice == "6":
                self.save_to_file()
                print(Fore.GREEN + "👋 Thank you for using the Library Manager. Goodbye!")
                break
            else:
                print(Fore.RED + "⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
