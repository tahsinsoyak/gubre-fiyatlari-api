import fastapi as _fastapi
import json
from typing import Optional
from fastapi import Query


app = _fastapi.FastAPI()


with open('gubrefiyatlari.json','r') as f:
    gubreler = json.load(f)

@app.get("/")
def root():
    return {"message": "hosgeldiniz"}


#tüm ürünler ve arama için
@app.get('/search',status_code=200)
def search_urun(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        return gubreler
    else:
        people2 = [p for p in gubreler if name.lower() in p ['urunismi'].lower()]
        return people2
