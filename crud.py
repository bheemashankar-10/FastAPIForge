from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel



books =[
    {
        "id":1,
        "title":"jaeugwufgw",
        "author":"jgbuqeguqn",
        "public data":"19-20-2000"

    },
    {
        "id":2,
        "title":"jaeguenufgw",
        "author":"jgeefbeuguqn",
        "public data":"12-10-2000"
    },
    {
        "id":3,
        "title":"lnmrmnufgw",
        "author":"jrhnnfbeuguqn",
        "public data":"22-10-2000"
    },
    {
        "id":4,
        "title":"kbmrmbufgw",
        "author":"jrjngnwuguqn",
        "public data":"02-10-2000"
    }
]
app=FastAPI()

@app.get("/book")
def get_book():
    return books

@app.get("/book/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book["id"]==book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="book not found"
    )

class booka(BaseModel):
    id:int
    title:str
    author:str
    publicdata:str

@app.post("/book")
def create_book(book: booka):
    new_book=book.model_dump()
    books.append(new_book)
    return new_book

class bookupdate(BaseModel):
    title:str
    author:str
    publicdata:str


@app.put("/book/{book_id}")
def update_book(book_id: int, book_update: bookupdate):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["public data"] = book_update.publicdata
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="book not found"
    )
@app.delete("/book/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book["id"]==book_id:
            books.remove(book)
            return "book deleted"
            
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="book not found"
    )