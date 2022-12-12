from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "title", "year"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Author(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    FANTASY: Book.Genre
    FICTION: Book.Genre
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    MYSTERY: Book.Genre
    NONFICTION: Book.Genre
    ROMANCE: Book.Genre
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: Book.Author
    genre: Book.Genre
    isbn: str
    title: str
    year: int
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., year: _Optional[int] = ..., genre: _Optional[_Union[Book.Genre, str]] = ..., author: _Optional[_Union[Book.Author, _Mapping]] = ...) -> None: ...
