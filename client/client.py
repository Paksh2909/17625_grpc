from __future__ import print_function
import sys

sys.path.append('./service/')
import grpc
import inventory_service_pb2_grpc
import inventory_service_pb2
import book_pb2


class Client:

    def __init__(self, url):
        self.channel = grpc.insecure_channel(url)
        self.stub = inventory_service_pb2_grpc.InventoryStub(self.channel)

    def create_book(self, book):
        new_book = book_pb2.Book(isbn=book["isbn"],
                                 title=book["title"],
                                 genre=book["genre"],
                                 author=book["author"],
                                 year=book["year"],
                                 )
        response = self.stub.CreateBook(inventory_service_pb2.CreateBookRequest(book=new_book))
        return response

    def get_book(self, isbn):
        response = self.stub.GetBook(inventory_service_pb2.GetBookRequest(isbn=isbn))
        return response


if __name__ == '__main__':
    obj = Client('localhost:50051')
    response1 = obj.get_book(isbn="1")
    response2 = obj.create_book({
            "isbn": "4",
            "title": "Percy Jackson Titans Curse",
            "genre": book_pb2.Book.FANTASY,
            "year": 2007,
            "author": book_pb2.Book.Author(name="Rick Riordan"),
        })
    print(response1)
    print("*****************************")
    print(response2)
