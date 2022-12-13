from concurrent import futures

import grpc
import inventory_service_pb2_grpc
import inventory_service_pb2
import book_pb2


class Inventory(inventory_service_pb2_grpc.InventoryServicer):
    # Storing the books in a list of objects.
    books = [
        {
            "isbn": "1",
            "title": "Percy Jackson",
            "genre": book_pb2.Book.FICTION,
            "author": book_pb2.Book.Author(name="Rick Riordan"),
            "year": 2005
        },
        {
            "isbn": "2",
            "title": "Percy Jackson Sea of monsters",
            "genre": book_pb2.Book.FANTASY,
            "year": 2007,
            "author": book_pb2.Book.Author(name="Rick Riordan"),
        }
    ]

    def CreateBook(self, request, context):
        book = request.book

        if request.book.isbn == "" or request.book.isbn is None:
            return inventory_service_pb2.CreateBookReply(message="ISBN incorrect.",
                                                         code="3: INVALID_ARGUMENT")

        if request.book.title == "" or request.book.title is None:
            return inventory_service_pb2.CreateBookReply(message="Title incorrect.",
                                                         code="3: INVALID_ARGUMENT")

        if request.book.author == "" or request.book.author is None:
            return inventory_service_pb2.CreateBookReply(message="Author incorrect.",
                                                         code="3: INVALID_ARGUMENT")

        if request.book.year is None or request.book.year < 800:
            return inventory_service_pb2.CreateBookReply(message="Year incorrect.",
                                                         code="3: INVALID_ARGUMENT")

        for i in self.books:
            # Checking is ISBN already exists
            if request.book.isbn == i["isbn"]:
                return inventory_service_pb2.CreateBookReply(message="ISBN already exists. Could not add book.",
                                                             code="6: ALREADY_EXISTS")

        # Creating a new book object from request
        new_book = {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            'year': book.year
        }

        # Adding new book to list of books
        self.books.append(new_book)
        return inventory_service_pb2.CreateBookReply(message="Book added successfully.", code="0: OK")

    def GetBook(self, request, context):

        if request.isbn == "" or request.isbn is None:
            return inventory_service_pb2.CreateBookReply(message="ISBN incorrect.",
                                                         code="3: INVALID_ARGUMENT")

        response = book_pb2.Book()
        present = False
        for i in self.books:
            # Checking if requested ISBN exists
            if i["isbn"] == request.isbn:
                present = True
                response = book_pb2.Book(isbn=i["isbn"],
                                         title=i["title"],
                                         genre=i["genre"],
                                         author=i["author"],
                                         year=i["year"],
                                         )

        # If found, returns Book details
        if present:
            return inventory_service_pb2.GetBookReply(book=response, message="Book found", code="0: OK")
        # Else returns not found message
        else:
            return inventory_service_pb2.GetBookReply(message="Book not found", code="5: NOT_FOUND")


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_service_pb2_grpc.add_InventoryServicer_to_server(Inventory(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
