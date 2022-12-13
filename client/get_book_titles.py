from client import Client


def get_book_titles(client_object, list_of_isbn):
    list_of_titles = []
    for i in list_of_isbn:
        response = client_object.get_book(i)
        if "0" in response.code:
            list_of_titles.append(response.book.title)

    return list_of_titles


if __name__ == "__main__":
    obj = Client("localhost:50051")
    response = get_book_titles(obj, ["1", "2", "10"])
    print(response)
