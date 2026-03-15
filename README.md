# HardSkill - Sistema de Gestão de Restaurante

Projeto de um sistema de gestão de restaurante em Python, composto por um servidor backend em **FastAPI** e um cliente de linha de comandos (CLI) para efetuar pedidos.

---

## Estrutura do Projeto

```
HardSkill/
├── main.py          # Servidor backend (FastAPI)
├── restaurant.py    # Cliente CLI para fazer pedidos
└── README.md
```

### `main.py` — Servidor Backend (FastAPI)

Servidor REST que expõe dois endpoints:

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/menu` | Devolve o menu completo por categorias |
| `POST` | `/api/orders` | Cria um novo pedido para uma mesa |

O servidor mantém os pedidos em memória com os seguintes estados possíveis:
- `Order Preview` → `Preparing` → `Cooling Down` → `Ready to Serve` → `Concluded`

### `restaurant.py` — Cliente CLI

Interface interativa de linha de comandos para os clientes do restaurante. Permite:
- Navegar pelas categorias do menu (Entradas, Sopas, Carne, Peixe, Sobremesas)
- Adicionar itens ao pedido com a quantidade desejada
- Ver o resumo do pedido e o total
- Confirmar e enviar o pedido para a cozinha via API

---

## Requisitos

- Python 3.10 ou superior
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## Instalação

### 1. Criar e ativar ambiente virtual

```bash
python -m venv .venv
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install fastapi uvicorn
```

---

## Como Executar

O sistema requer **dois terminais** a correr em simultâneo.

### Terminal 1 — Iniciar o Servidor

```bash
uvicorn main:app --reload
```

O servidor ficará disponível em `http://127.0.0.1:8000`.

> A documentação interativa da API (Swagger UI) pode ser acedida em `http://127.0.0.1:8000/docs`.

### Terminal 2 — Iniciar o Cliente CLI

```bash
python restaurant.py
```

Siga as instruções no ecrã para navegar pelo menu e efetuar pedidos.

---

## Exemplo de Utilização

```
Por favor, insira o número da sua mesa: 3

Bem vindo ao Restaurant!
1. Entradas
2. Sopas
3. Carne
4. Peixe
5. Sobremesas
6. Ver pedido atual
7. Acabar o pedido
Por favor, selecione uma categoria (1-7): 1

Entradas:
1. Camarão frito (10.00€)
2. Pão de alho (5.00€)
...
```

---

## Notas

- Os pedidos são guardados em memória — ao reiniciar o servidor, os dados são perdidos.
- O servidor deve estar em execução **antes** de iniciar o cliente CLI.
- O número de mesa deve ser um número inteiro positivo.

