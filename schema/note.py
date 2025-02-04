def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "content": item["content"],
        "important": item["important"]
    }


def notesEntity(entity) -> list:
    return [noteEntity(item) for item in entity]