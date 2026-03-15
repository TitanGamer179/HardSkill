import json
from urllib import error, request

API_BASE = "http://127.0.0.1:8000"
    
def enviar_pedido(pedido):
    try:
        data = json.dumps(pedido).encode('utf-8')
        req = request.Request(f"{API_BASE}/api/orders", data=data, headers={'Content-Type': 'application/json'})
        with request.urlopen(req) as response:
            if response.status == 200:
                print("Pedido enviado com sucesso para a Cozinha!")
            else:
                print(f"Erro ao enviar o pedido: {response.status}")
    except error.URLError as e:
        print(f"Erro de conexão: {e.reason} - O servidor FastAPI está a correr?")

def clear_screen():
    input("Pressione Enter para continuar...")
    print("\033[H\033[J", end="")

def quantity_input(prompt):
    while True:
        quantity = input(prompt)
        if quantity.isdigit():
            return int(quantity)
        else:
            print("Por favor, insira um número válido para a quantidade.")

def entradas(itens_pedido, total):
    while True:
        print("\nEntradas:")
        print("1. Camarão frito (10.00€)")
        print("2. Pão de alho (5.00€)")
        print("3. Pão de alho com queijo (7.00€)")
        print("4. Salada de tomate (6.00€)")
        print("5. Salada de alface (5.00€)")
        print("6. Voltar ao menu principal")
        choice = input("Por favor, selecione uma entrada: ").strip()
        
        if choice.startswith('1'):
            quality = quantity_input("Quantos camarões fritos você gostaria de pedir? ")
            itens_pedido.append({"item_name": "Camarão frito", "quantity": quality})
            total += 10.00 * quality
            clear_screen()
        elif choice.startswith('2'):
            quality = quantity_input("Quantos pães de alho você gostaria de pedir? ")
            itens_pedido.append({"item_name": "Pão de alho", "quantity": quality})
            total += 5.00 * quality
            clear_screen()
        elif choice.startswith('3'):
            quality = quantity_input("Quantos pães de alho com queijo gostaria de pedir? ")
            itens_pedido.append({"item_name": "Pão de alho com queijo", "quantity": quality})
            total += 7.00 * quality
            clear_screen()
        elif choice.startswith('4'):
            quality = quantity_input("Quantas saladas de tomate gostaria de pedir? ")
            itens_pedido.append({"item_name": "Salada de tomate", "quantity": quality})
            total += 6.00 * quality
            clear_screen()
        elif choice.startswith('5'):
            quality = quantity_input("Quantas saladas de alface gostaria de pedir? ")
            itens_pedido.append({"item_name": "Salada de alface", "quantity": quality})
            total += 5.00 * quality
            clear_screen()
        elif choice.startswith('6') or choice.casefold().startswith('voltar'):
            clear_screen()
            break
        else:
            print("Seleção inválida. Por favor, tente novamente.")
    return total

def sopas(itens_pedido, total):
    while True:
        print("\nSopas:")
        print("1. Sopa de legumes (4.00€)")
        print("2. Sopa de peixe (6.00€)")
        print("3. Sopa de frango (5.00€)")
        print("4. Voltar ao menu principal")
        choice = input("Por favor, selecione uma sopa: ").strip()
        
        if choice.startswith('1'):
            quality = quantity_input("Quantas tigelas de sopa de legumes gostaria de pedir? ")
            itens_pedido.append({"item_name": "Sopa de legumes", "quantity": quality})
            total += 4.00 * quality
            clear_screen()
        elif choice.startswith('2'):
            quality = quantity_input("Quantas tigelas de sopa de peixe gostaria de pedir? ")
            itens_pedido.append({"item_name": "Sopa de peixe", "quantity": quality})
            total += 6.00 * quality
            clear_screen()
        elif choice.startswith('3'):
            quality = quantity_input("Quantas tigelas de sopa de frango gostaria de pedir? ")
            itens_pedido.append({"item_name": "Sopa de frango", "quantity": quality})
            total += 5.00 * quality
            clear_screen()
        elif choice.startswith('4'):
            clear_screen()
            break
        else:
            print("Seleção inválida.")
    return total

def carne(itens_pedido, total):
    while True:
        print("\nCarne:")
        print("1. Bife de vaca (15.00€)")
        print("2. Frango grelhado (12.00€)")
        print("3. Costeletas de porco (14.00€)")
        print("4. Voltar ao menu principal")
        choice = input("Por favor, selecione um prato de carne: ").strip()
        
        if choice.startswith('1'):
            quality = quantity_input("Quantos bifes de vaca gostaria de pedir? ")
            itens_pedido.append({"item_name": "Bife de vaca", "quantity": quality})
            total += 15.00 * quality
            clear_screen()
        elif choice.startswith('2'):
            quality = quantity_input("Quantos pratos de frango grelhado gostaria de pedir? ")
            itens_pedido.append({"item_name": "Frango grelhado", "quantity": quality})
            total += 12.00 * quality
            clear_screen()
        elif choice.startswith('3'):
            quality = quantity_input("Quantos pratos de costeletas de porco gostaria de pedir? ")
            itens_pedido.append({"item_name": "Costeletas de porco", "quantity": quality})
            total += 14.00 * quality
            clear_screen()
        elif choice.startswith('4'):
            clear_screen()
            break
    return total

def peixe(itens_pedido, total):
    while True:
        print("\nPeixe:")
        print("1. Salmão grelhado (18.00€)")
        print("2. Bacalhau à Brás (16.00€)")
        print("3. Filetes de peixe (14.00€)")
        print("4. Voltar ao menu principal")
        choice = input("Por favor, selecione um prato de peixe: ").strip()
        
        if choice.startswith('1'):
            quality = quantity_input("Quantos pratos de salmão grelhado gostaria de pedir? ")
            itens_pedido.append({"item_name": "Salmão grelhado", "quantity": quality})
            total += 18.00 * quality
            clear_screen()
        elif choice.startswith('2'):
            quality = quantity_input("Quantos pratos de bacalhau à Brás gostaria de pedir? ")
            itens_pedido.append({"item_name": "Bacalhau à Brás", "quantity": quality})
            total += 16.00 * quality
            clear_screen()
        elif choice.startswith('3'):
            quality = quantity_input("Quantos pratos de filetes de peixe gostaria de pedir? ")
            itens_pedido.append({"item_name": "Filetes de peixe", "quantity": quality})
            total += 14.00 * quality
            clear_screen()
        elif choice.startswith('4'):
            clear_screen()
            break
    return total

def sobremesas(itens_pedido, total):
    while True:
        print("\nSobremesas:")
        print("1. Pudim de chocolate (5.00€)")
        print("2. Mousse de maracujá (6.00€)")
        print("3. Tarte de maçã (4.00€)")
        print("4. Voltar ao menu principal")
        choice = input("Por favor, selecione uma sobremesa: ").strip()
        
        if choice.startswith('1'):
            quality = quantity_input("Quantos pudins de chocolate gostaria de pedir? ")
            itens_pedido.append({"item_name": "Pudim de chocolate", "quantity": quality})
            total += 5.00 * quality
            clear_screen()
        elif choice.startswith('2'):
            quality = quantity_input("Quantas mousses de maracujá gostaria de pedir? ")
            itens_pedido.append({"item_name": "Mousse de maracujá", "quantity": quality})
            total += 6.00 * quality
            clear_screen()
        elif choice.startswith('3'):
            quality = quantity_input("Quantas tartes de maçã gostaria de pedir? ")
            itens_pedido.append({"item_name": "Tarte de maçã", "quantity": quality})
            total += 4.00 * quality
            clear_screen()
        elif choice.startswith('4'):
            clear_screen()
            break
    return total

def menu():
    itens_pedido = []
    total = 0
    mesa = input("Por favor, insira o número da sua mesa: ")
    
    while True:
        print("\nBem vindo ao Restaurant!")
        print("1. Entradas")
        print("2. Sopas")
        print("3. Carne")
        print("4. Peixe")
        print("5. Sobremesas")
        print("6. Ver pedido atual")
        print("7. Acabar o pedido")
        choice = input("Por favor, selecione uma categoria (1-7): ").strip()
        
        if choice.startswith('1'):
            total = entradas(itens_pedido, total)
        elif choice.startswith('2'):
            total = sopas(itens_pedido, total)
        elif choice.startswith('3'):
            total = carne(itens_pedido, total)
        elif choice.startswith('4'):
            total = peixe(itens_pedido, total)
        elif choice.startswith('5'):
            total = sobremesas(itens_pedido, total)
        elif choice.startswith('6'):
            print("\n--- Pedido Atual ---")
            for item in itens_pedido:
                print(f"{item['quantity']}x {item['item_name']}")
            print(f"Total: {total:.2f}€")
            print("--------------------")
            clear_screen()
        elif choice.startswith('7'):
            print("\n--- Pedido Final ---")
            for item in itens_pedido:
                print(f"{item['quantity']}x {item['item_name']}")
            print(f"Total: {total:.2f}€")
            print("--------------------")
            
            confirm = input("Deseja confirmar o pedido? (sim/não): ").strip().lower()
            if confirm == 'sim':
                feedback = input("Deseja dar um feedback? (sim/não): ").strip().lower()
                if feedback == 'sim':
                    feedback_text = input("Por favor, deixe seu feedback: ")
                    print("Obrigado pelo seu feedback!")
                order = {
                    "table_number": int(mesa) if mesa.isdigit() else 1,
                    "items": itens_pedido,
                }
                enviar_pedido(order) 
                itens_pedido.clear()
                total = 0
                mesa = input("\nPor favor, insira o número de uma nova mesa (ou CTRL+C para sair): ")
            else:
                print("Pedido cancelado. Pode continuar a adicionar itens.")
        else:
            print("Seleção inválida. Por favor, tente novamente.")

if __name__ == "__main__":    
    menu()