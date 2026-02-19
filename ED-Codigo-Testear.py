# archivo: registro_usuario.py

def pedir_nombre():
    return input("Introduce el nombre: ")


def pedir_edad():
    edad = input("Introduce la edad: ")
    if not edad.isdigit():
        return None
    return int(edad)


def pedir_email():
    return input("Introduce el email: ")


def pedir_dni():
    return input("Introduce el DNI: ")


def validar_nombre(nombre):
    return nombre != ""


def validar_edad(edad):
    if edad is None:
        return False
    return edad >= 0


def validar_email(email):
    if "@" not in email:
        return False
    if email.startswith("@") or email.endswith("@"):
        return False
    return True


def validar_dni(dni):
    if len(dni) != 9:
        return False
    if not dni[:8].isdigit():
        return False
    if not dni[8].isalpha():
        return False
    return True


def crear_usuario(nombre, edad, email, dni):
    if not validar_nombre(nombre):
        return None
    if not validar_edad(edad):
        return None
    if not validar_email(email):
        return None
    if not validar_dni(dni):
        return None

    return {
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "dni": dni
    }


def mostrar_usuario(usuario):
    if usuario is None:
        print("Usuario no válido")
    else:
        print("Usuario creado correctamente")
        print("Nombre:", usuario["nombre"])
        print("Edad:", usuario["edad"])
        print("Email:", usuario["email"])
        print("DNI:", usuario["dni"])


def main():
    nombre = pedir_nombre()
    edad = pedir_edad()
    email = pedir_email()
    dni = pedir_dni()

    usuario = crear_usuario(nombre, edad, email, dni)
    mostrar_usuario(usuario)


if __name__ == "__main__":
    main()
