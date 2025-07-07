
import random
import sys

def generar_numero_unico(tickets_existentes):
    """
    Genera un número de ticket aleatorio y único entre 1000 y 9999.

    Verifica que el número no exista ya en el diccionario de tickets
    antes de devolverlo. Si el rango de números se agota, lo cual es
    muy improbable, lanzará una excepción.

    Args:
        tickets_existentes (dict): El diccionario de tickets actual.

    Returns:
        int: Un número de ticket único.
    """
    intentos = 0
    max_intentos = 9000 # Rango de 1000 a 9999
    while intentos < max_intentos:
        num = random.randint(1000, 9999)
        if num not in tickets_existentes:
            return num
        intentos += 1
    # Si se agotan los números, es una situación excepcional
    raise OverflowError("No hay más números de ticket disponibles.")

def mostrar_ticket(numero, ticket):
    """
    Muestra los detalles de un ticket de forma formateada.

    Args:
        numero (int): El número del ticket.
        ticket (dict): El diccionario con los datos del ticket.
    """
    print("\n--- DETALLES DEL TICKET ---")
    print(f"  NÚMERO:   {numero}")
    print(f"  Nombre:   {ticket['nombre']}")
    print(f"  Sector:   {ticket['sector']}")
    print(f"  Asunto:   {ticket['asunto']}")
    print(f"  Problema: {ticket['problema']}")
    print("---------------------------\n")


def alta_ticket(tickets):
    """
    Permite crear uno o varios tickets, validando las entradas.

    - Pide nombre, sector, asunto y descripción. No permite campos vacíos.
    - Genera un número de ticket único.
    - Muestra el ticket generado y ofrece crear otro.
    """
    while True:
        print("\n--- ALTA DE TICKET (deja un campo vacío para cancelar) ---")
        
        # Solicitar y validar entradas del usuario
        nombre = input("Nombre del solicitante: ").strip()
        if not nombre: break
        
        sector = input("Sector: ").strip()
        if not sector: break
        
        asunto = input("Asunto: ").strip()
        if not asunto: break
        
        problema = input("Descripción del problema: ").strip()
        if not problema: break

        try:
            num = generar_numero_unico(tickets)
            tickets[num] = {
                "nombre": nombre,
                "sector": sector,
                "asunto": asunto,
                "problema": problema
            }
            print("\n✅ ¡Ticket generado con éxito!")
            mostrar_ticket(num, tickets[num])
            print("¡No olvides tu número de ticket!\n")

        except OverflowError as e:
            print(f"Error: {e}")
            break

        otra = input("¿Deseas crear otro ticket? (s/n): ").lower()
        if otra != 's':
            break

def leer_ticket(tickets):
    """
    Permite consultar uno o varios tickets por su número.
    """
    if not tickets:
        print("\nℹ️ No hay tickets cargados en el sistema.\n")
        return

    while True:
        print("\n--- LECTURA DE TICKET ---")
        entrada = input("Ingresa el número de ticket (o presiona Enter para volver): ")
        if not entrada:
            break

        try:
            num = int(entrada)
            if num in tickets:
                ticket_encontrado = tickets[num]
                mostrar_ticket(num, ticket_encontrado)
            else:
                print(f"\n❌ No se encontró un ticket con el número {num}.\n")
        except ValueError:
            print("\n❌ Número inválido. Por favor, ingresa solo dígitos.\n")
            continue

        otra = input("¿Deseas leer otro ticket? (s/n): ").lower()
        if otra != 's':
            break

def confirmar_salida():
    """
    Pide confirmación antes de cerrar el programa y sale si es afirmativo.
    
    Returns:
        bool: True si el usuario confirma la salida, False en caso contrario.
    """
    resp = input("\n¿Seguro que quieres salir? (s/n): ").lower()
    if resp == 's':
        print("\n¡Hasta luego! 👋")
        return True
    else:
        print("\nRegresando al menú principal...\n")
        return False

def menu_principal():
    """
    Muestra el menú principal y gestiona el flujo del programa.
    """
    tickets = {}
    
    while True:
        print("====== SISTEMA DE TICKETS ======")
        print("  1) Alta de Ticket")
        print("  2) Leer Ticket")
        print("  3) Salir")
        print("==============================")
        elec = input("Selecciona una opción: ").strip()

        if elec == '1':
            alta_ticket(tickets)
        elif elec == '2':
            leer_ticket(tickets)
        elif elec == '3':
            if confirmar_salida():
                sys.exit(0)
        else:
            print("\n❌ Opción inválida. Intenta otra vez.\n")

# --- Punto de entrada principal del programa ---
# Esta construcción asegura que el menú solo se ejecute
# cuando el archivo es corrido directamente.
if __name__ == "__main__":
    menu_principal()