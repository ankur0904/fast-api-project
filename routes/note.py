from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schema.note import noteEntity, notesEntity


from fastapi.templating import Jinja2Templates
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")


note = APIRouter()

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        print(doc)
        newDocs.append({
            'id': doc['_id'],
            'title': doc['title'],
            'note': doc['content']
        })
    print(docs)
    return templates.TemplateResponse("index.html", {"request":request, "newDocs":newDocs})


@note.post("/", response_class=HTMLResponse)
async def add_note(request: Request):
    form = await request.form()
    note = conn.notes.notes.insert_one(dict(form))
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        print(doc)
        newDocs.append({
            'id': doc['_id'],
            'title': doc['title'],
            'note': doc['content']
        })
    return templates.TemplateResponse("index.html", {"request":request, "newDocs":newDocs})

@note.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}