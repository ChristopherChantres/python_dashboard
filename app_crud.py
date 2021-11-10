import time, random, os

# Juego de adivinar el número
def guess_game(user, password):
    vidas = 7
    numero_aleatorio = random.randint(1, 100)
    print(f"\n|———————————————— Adivina el número ———————————————————|\n")
    print(f"Hola {user} tienes " + str(vidas) + " vidas, ¡Suerte!")
    numero_elegido = int(input("Elige un numero del 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("BUSCA UN NÚMERO MÁS GRANDE")
            vidas -= 1
        else:
            print("BUSCA UN NÚMERO MÁS PEQUEÑO")
            vidas -= 1
        print("[Te quedan " + str(vidas) + " vidas]")
        numero_elegido = int(input("Elige otro número: "))

        if vidas == 1:
            print("LO SIENTO, HAS PERDIDO")
            time.sleep(2)
            clearConsole()
            dashboard(user, password)

        resultado = 8 - vidas
    print("¡FELICIDADES GANASTE CON " + str(resultado) + " INTENTOS" )
    time.sleep(5)
    clearConsole()
    dashboard(user, password)

# Agregar tareas y borrar las tareaaaas (nuevoooo)
def add_task(user, password, tasks):
    print(f"\n|———————————————— Tareas para hacer ———————————————————|\n")
    task_to_do = input(f"{user} agrega tu tarea: ")

    if not task_to_do:
        print("\nAgrega contenido en tu tarea :)\n")
        clearConsole()
        add_task(user, password, tasks)
    tasks.append(task_to_do)
    clearConsole()
    show_task(user, password, tasks)

# Mostrar tareas
def show_task(user, password, tasks):
    print(f"\nTus tareas son: {tasks}")
    try:
        go_to_dashboard = int(input("Deseas volver al menú principal Sí[1] No[2]: "))
    except ValueError:
        print("*Ingresa un número válido*")
        clearConsole()
        show_task(user, password, tasks)

    if not go_to_dashboard:
        print("*Ingresa un número :)*")
        clearConsole()
        show_task(user, password, tasks)
    elif go_to_dashboard == 1:
        print("Volviendo al menú principal...") #Hay error en la eleccion
        time.sleep(3)
        clearConsole()
        dashboard(user, password)        
    elif go_to_dashboard == 2:
        clearConsole()
        add_task(user, password, tasks)
    else:
        print("Debes ingresar un número válido, bye :)")
        time.sleep(3)
        clearConsole()
        dashboard(user, password)

# Estas son las acciones del dashboard de la aplicación
def dashboard_actions(user, password):
    try:
        action1 = int(input("¿Qué desas hacer?: "))
        if action1 == 1:
            print("Saliendo...")
            time.sleep(2)
            clearConsole()
            run(user, password)
        elif action1 == 2:
            clearConsole()
            add_task(user, password, tasks)
        elif action1 == 3:
            clearConsole()
            guess_game(user, password)
        elif action1 == 4:
            if tasks:
                print(f"Tareas que tienes PENDIENTES:\n{tasks}")
            else:
                print("Aún no has agregado tareas :)")
            time.sleep(3)
            clearConsole()
            dashboard(user, password)
        elif action1 == 5:
            tasks.clear()
            print("Borrando cuenta...")
            time.sleep(3)
            clearConsole()
            create_user()
        else:
            dashboard(user, password)
    except ValueError:
        print("Ingresa un número válido")
        time.sleep(2)
        clearConsole()
        dashboard(user, password)

# Este es el dashboard de la aplicación
def dashboard(user, password):
    print(f"\n|———————————————————————————————————|\n    Bienvenido {user}")
    print(f" \nTu contraseña es: {password}\n                         Salir[1]")
    print("                 Agregar Tarea[2]")
    print("     Juego *Adivina el número*[3]")
    print("            Mostrar las tareas[4]\n")
    print("                 Borrar Cuenta[5]\n")
    dashboard_actions(user, password)

def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

# Función para cargar
def loading():
    for i in range(4):
        print("|")
        time.sleep(0.1)
        print("/")
        time.sleep(0.1)
        print("—")
        time.sleep(0.1)
    clearConsole()
    print("*Yay, has accedidio a tu cuenta*")

# Creación del usuario
def create_user():
    print("================= Bienvedido Regístrate =================")
    user = str(input("Registra tu usuario: "))
    password = str(input("Registra tu contraseña: "))
    if user and password:
        run(user, password)
    else:
        print("*Debes llenar ambos campos*")
        time.sleep(2)
        clearConsole()
        create_user()

# Inicio de sesión
def run(user, password):
    print("\n================= Inicia Sesión =================")
    a = str(input("Ingresa tu usuario: "))
    b = str(input("Ingresa tu contraseña: "))

    if user == a and password == b:
        clearConsole()
        all_users = []
        all_passwords = []
        all_users.append(user)
        all_passwords.append(password)
        loading()
        dashboard(user, password)
    else:
        print("\n*Los datos no son correctos*")
        time.sleep(2)
        clearConsole()
        run(user, password)


if __name__ == "__main__":
    tasks  = []
    create_user()
# Crear un registro de los usuarios
# Borrar la cuenta cuando se le da a borrar cuenta