def division(numero1, numero2):
    """
    Realiza la división de dos números con validaciones.

    Parámetros:
        numero1 (int | float): El dividendo.
        numero2 (int | float): El divisor.

    Retorna:
        float: El resultado de la división.

    Excepciones:
        TypeError: Si los parámetros no son números (int o float).
        ZeroDivisionError: Si el divisor es cero.
    """
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        raise TypeError("Los valores deben ser números (int o float)")

    if numero2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero")

    return numero1 / numero2


# Programa principal con hasta 3 intentos
intentos = 3

while intentos > 0:
    try:
        numero1 = float(input("Ingresa un número: "))
        numero2 = float(input("Ingresa otro número: "))
        resultado = division(numero1, numero2)
        print("✅ El resultado es:", resultado)
        break  # sale del bucle si todo salió bien

    except ValueError:
        intentos -= 1
        if intentos > 0:
            print(f"❌ Error: Debes ingresar un número válido. Te quedan {intentos} intentos.")
        else:
            print("❌ Error: Te quedaste sin intentos.")

    except ZeroDivisionError as e:
        intentos -= 1
        if intentos > 0:
            print(f"❌ {e}. Te quedan {intentos} intentos.")
        else:
            print("❌ Error: Te quedaste sin intentos.")

    except TypeError as e:
        intentos -= 1
        if intentos > 0:
            print(f"❌ {e}. Te quedan {intentos} intentos.")
        else:
            print("❌ Error: Te quedaste sin intentos.")

"""
def division(numero1, numero2):
    resultado = numero1 / numero_2
    return resultado


numero1 = input("Ingresa un número: "
numero2 = input("Ingresa otro número: ")
resultado = dividir_dos_numeros(numero1, numero2)
print("El resultado es: ", resultado) """

# Opción 1
"""
def division(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

# Pedir números al usuario (convertir a float para admitir decimales)
numero1 = float(input("Ingresa un número: "))
numero2 = float(input("Ingresa otro número: "))

resultado = division(numero1, numero2)
print("El resultado es:", resultado)
"""
#Opción mejorada
"""
def division(numero1, numero2):
    if numero2 == 0:
        return "Error: no se puede dividir por cero"
    return numero1 / numero2

try:
    numero1 = float(input("Ingresa un número: "))
    numero2 = float(input("Ingresa otro número: "))
    resultado = division(numero1, numero2)
    print("El resultado es:", resultado)
except ValueError:
    print("Error: Debes ingresar un número válido")
"""
# Opción 3
"""
def division(numero1, numero2):
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        raise TypeError("Los valores deben ser números (int o float)")

    if numero2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero")

    return numero1 / numero2


# Programa principal
try:
    numero1 = float(input("Ingresa un número: "))
    numero2 = float(input("Ingresa otro número: "))
    resultado = division(numero1, numero2)
    print("El resultado es:", resultado)

except ValueError:
    print("Error: Debes ingresar un número válido")
except ZeroDivisionError as e:
    print("Error:", e)
except TypeError as e:
    print("Error:", e)

# Opción con intentos
def division(numero1, numero2):
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        raise TypeError("Los valores deben ser números (int o float)")

    if numero2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero")

    return numero1 / numero2


# Programa principal con hasta 3 intentos
intentos = 3

while intentos > 0:
    try:
        numero1 = float(input("Ingresa un número: "))
        numero2 = float(input("Ingresa otro número: "))
        resultado = division(numero1, numero2)
        print("✅ El resultado es:", resultado)
        break  # sale del bucle si todo salió bien

    except ValueError:
        intentos -= 1
        if intentos > 0:
            print(f"❌ Error: Debes ingresar un número válido. Te quedan {intentos} intentos.")
        else:
            print("❌ Error: Te quedaste sin intentos.")

    except ZeroDivisionError as e:
        intentos -= 1
        if intentos > 0:
            print(f"❌ {e}. Te quedan {intentos} intentos.")
        else:
            print("❌ Error: Te quedaste sin intentos.")

    except TypeError as e:
        intentos -= 1
        if intentos > 0:
            print(f"❌ {e}. Te quedan {intentos} intentos.")
        else:
            print("❌ Error: Te quedaste sin intentos.")
"""