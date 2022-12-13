import unittest
from unittest.mock import MagicMock

import sys

sys.path.append('./service/')

import get_book_titles
import book_pb2
import inventory_service_pb2
from client import Client

mock_data = [
    book_pb2.Book(
        isbn="3",
        title="The Lost Hero",
        genre=book_pb2.Book.FICTION,
        author=book_pb2.Book.Author(name="Rick Riordan"),
        year=2005),
    book_pb2.Book(
        isbn="4",
        title="Son Of Neptune",
        genre=book_pb2.Book.FANTASY,
        year=2007,
        author=book_pb2.Book.Author(name="Rick Riordan"))
]


class TestGetBookTitles(unittest.TestCase):

    def mock_get_book(self, isbn):
        for book in mock_data:
            if book.isbn == isbn:
                return inventory_service_pb2.GetBookReply(book=book, message="Book found", code="0: OK")

    def test_client_mock(self):
        print("Running test with mock client")
        mock_client = MagicMock()
        mock_client.get_book = self.mock_get_book
        list_of_isbns = ["3", "4"]
        list_of_titles = get_book_titles.get_book_titles(client_object=mock_client, list_of_isbn=list_of_isbns)
        self.assertEqual(list_of_titles, ['The Lost Hero', 'Son Of Neptune'])

    def test_client_live(self):
        print("Running test with live client")
        client = Client(url="localhost:50051")
        list_of_titles = get_book_titles.get_book_titles(client_object=client, list_of_isbn=["1", "2"])
        self.assertEqual(list_of_titles, ["Percy Jackson", "Percy Jackson Sea of monsters"])


if __name__ == '__main__':
    unittest.main()
