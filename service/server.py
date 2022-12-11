from concurrent import futures

import grpc
import inventory_service_pb2_grpc
import inventory_service_pb2
import book_pb2

class Inventory(inventory_service_pb2_grpc.InventoryServicer):
    books = [
        {
            "isbn": "1",
            "title": "Percy Jackson",
            "genre": book_pb2.Book.FICTION,
            "author": book_pb2.Book.Author(name= "Rick Riordan"),
            "year": 2005
        },
        {
            "isbn": "2",
            "title": "Percy Jackson Sea of monsters",
            "genre": book_pb2.Book.FANTASY,
            "year": 2007,
            "author": book_pb2.Book.Author(name= "Rick Riordan"),
        }
    ]

    def CreateBook(self, request, context):
        book = request.book
        for i in self.books:
            if request.book.isbn == i["isbn"]:
                return inventory_service_pb2.CreateBookReply(message= "ISBN already exists. Could not add book.")

        new_book = {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            'year': book.year
        }
        self.books.append(new_book)
        return inventory_service_pb2.CreateBookReply(message= "Book added successfully.")

    def GetBook(self, request, context):
        response = book_pb2.Book()
        present = False
        for i in self.books:
            if i["isbn"] == request.isbn:
                present = True
                response = book_pb2.Book(isbn=i["isbn"],
                    title= i["title"],
                    genre= i["genre"],
                    author= i["author"],
                    year= i["year"],
                )
        if present:
            return inventory_service_pb2.GetBookReply(book= response, message = "Book found")
        else:
            return inventory_service_pb2.GetBookReply(message = "Book not found")
                      
        

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