class Ebook:

    def __init__(self):
        self._Books= [] #empty list of books
        self._listSize = 0 # number of books in e reader 

    #void method no return 
    def _buy(self, book):
        self._Books.append(book)
        self._listSize+=1

    def _books_bought(self):
        if self._listSize >0: 
            if self._listSize == 1:
                return f"There is {self._listSize} book in your library"
            else:
                return f"There are {self._listSize} books in your library"
        else:
            print("Ebook has no books")

    # receives a book name and iterates through list to get the book if exists in reader 
    def _get_book(self, book):
        if self._listSize > 0:
            if book in self._Books:
                return "book exists and is going to be displayed"
            else:
                return "There is no Book in your library with such title"
        else:
            raise ValueError("There is no book with such name in your library")


if __name__ == '__main__':
    myEreader= Ebook()

    myEreader._buy("Harry Potter Vol 1")

    print(myEreader._books_bought())
    print(myEreader._get_book("Harry Potter Vol 1"))
    print(myEreader._get_book("Hunger Games"))

    myEreader._buy("Hunger Games")
    print(myEreader._books_bought())
    print(myEreader._get_book("Hunger Games"))


