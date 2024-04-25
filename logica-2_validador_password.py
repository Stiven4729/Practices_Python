"""
Desarrolla un programa que solicite al usuario ingresar
una contraseña y verifique si cumple con los siguientes criterios:

La longitud de la contraseña debe ser de al menos 8 caracteres.
La contraseña debe contener al menos una letra mayúscula y una letra minúscula.
La contraseña debe contener al menos un número.
La contraseña no debe contener caracteres especiales distintos de los siguientes:
!@#$%^&*()_+[]{};:,.<>?.

Si la contraseña cumple con todos los criterios, el programa debe imprimir "Contraseña válida".
De lo contrario, debe imprimir un mensaje indicando qué criterios no se cumplieron.
"""

password = input("Password ")
passwordMayusc = password.upper()
passwordMinusc = password.lower()

if len(password) >= 8:
    if password !=  passwordMayusc:
        if password != passwordMinusc:
            if password.count("0") | password.count("1") | password.count("2") | password.count("3") | password.count("4") | password.count("5") | password.count("6") | password.count("7") | password.count("8") | password.count("9"):
                print("porfin")
                if password.count("!") | password.count("@") | password.count("#") | password.count("$") | password.count("%") | password.count("^")| password.count("&") | password.count("*") | password.count("(") | password.count(")")| password.count("_")| password.count("+")| password.count("[")| password.count("]")| password.count("{") | password.count("}") | password.count(";") | password.count(":") | password.count(",") | password.count(".") | password.count("<") | password.count(">") | password.count("?"):
                    print("The password is correct")
                else:
                    print("the password needs one caracter special")
            else:
                print("the password needs a one number")
        else:
            print("the password needs a one leter minusc")
    else:
        print("the password needs a one mayusc")
else:
    print("la contraseña debe de tener mas de 8 caracteres")
    