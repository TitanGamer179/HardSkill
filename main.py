from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OrderLine(BaseModel):
    item_name: str = Field(min_length=1)
    quantity: int = Field(gt=0)

class Order(BaseModel):
    table_number: int = Field(gt=0)
    items: List[OrderLine]

class OrderStatusUpdate(BaseModel):
    status: Literal[
        "Order Preview",
        "Preparing",
        "Cooling Down",
        "Ready to Serve",
        "Concluded",
    ]

menu_db = {
    "Entradas": [
        {"id": 1, "nome": "Camarão frito", "descricao": "Camarão empadado e frito em óleo", "preco": 10.00},
        {"id": 2, "nome": "Pão de alho", "descricao": "Pão de alho com manteiga", "preco": 5.00},
        {"id": 3, "nome": "Pão de alho com queijo", "descricao": "Pão de alho com queijo", "preco": 7.00},
        {"id": 4, "nome": "Salada de tomate", "descricao": "Salada com tomates e pepino", "preco": 6.00},
        {"id": 5, "nome": "Salada de alface", "descricao": "Salada com alface e tomates", "preco": 5.00}
    ],
    "Sopas": [
        {"id": 6, "nome": "Sopa de legumes", "descricao": "Sopa feita com legumes frescos", "preco": 4.00},
        {"id": 7, "nome": "Sopa de peixe", "descricao": "Sopa feita com peixe fresco", "preco": 6.00},
        {"id": 8, "nome": "Sopa de frango", "descricao": "Sopa feita com frango fresco", "preco": 5.00}
    ],
    "Carne": [
        {"id": 9, "nome": "Bife de vaca", "descricao": "Bife de vaca grelhado", "preco": 15.00},
        {"id": 10, "nome": "Frango grelhado", "descricao": "Frango grelhado com ervas", "preco": 12.00},
        {"id": 11, "nome": "Costeletas de porco", "descricao": "Costeletas de porco grelhadas", "preco": 14.00}
    ],
    "Peixe": [
        {"id": 12, "nome": "Salmão grelhado", "descricao": "Salmão grelhado com limão", "preco": 18.00},
        {"id": 13, "nome": "Bacalhau à Brás", "descricao": "Bacalhau desfiado com batatas e ovos", "preco": 16.00},
        {"id": 14, "nome": "Filetes de peixe", "descricao": "Filetes de peixe empanados e fritos", "preco": 14.00}
    ],
    "Sobremesas": [
        {"id": 15, "nome": "Pudim de chocolate", "descricao": "Pudim de chocolate com calda", "preco": 5.00},
        {"id": 16, "nome": "Mousse de maracujá", "descricao": "Mousse de maracujá com chantilly", "preco": 6.00},
        {"id": 17, "nome": "Tarte de maçã", "descricao": "Tarte de maçã com canela", "preco": 4.00}
    ]
}
orders_db = []

def get_order_by_id(order_id: int):
    for order in orders_db:
        if order["id"] == order_id:
            return order
    return None

@app.get("/api/menu")
def get_menu():
    return menu_db

@app.post("/api/orders")
def create_order(order: Order):
    new_order = {
        "id": len(orders_db) + 1,
        "table": order.table_number,
        "items": [{"name": item.item_name, "qty": item.quantity} for item in order.items],
        "status": "Order Preview", 
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    orders_db.append(new_order)
    return {"message": "Pedido recebido com sucesso!", "order_id": new_order["id"]}
