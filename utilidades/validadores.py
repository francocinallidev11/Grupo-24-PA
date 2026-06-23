# Para validar ISBN de 10 digitos se usa
# isbn[0] * 1 + isbn[1] * 2 + ... + isbn[8] * 9 + isbn[9] * 10 => CHECK DE 10
# El numero puede ser un numero de + de 1 digito, por ej puede darte 93 => haces el modulo (%) de 93 / 11 => 3 => CHECK DE 10

# Para validar ISBN de 13 digitos se usa
# isbn[0] * 1 + isbn[1] * 3 + isbn[2] * 1 + isbn[3] * 3 + ... + isbn[11] * 3 => CHECK DE 13 # Posicion par => * 1, Posicion impar => * 3
# El numero puede ser un numero de + de 1 digito, por ej puede darte 93 => haces el modulo (%) de 93 / 10 => 3 => CHECK DE 13

# def validar_isbn(isbn):
    # 1. Limpiar el ISBN de guiones y espacios
    # 2. Validar que empiece por 978 o 979 | no cumple -> fuera
    # 3. Validar que tenga 10 o 13 digitos | no cumple -> fuera
    # 4. Validar check digit
    # 4.1. Si tiene 10 digitos => valido si el check digit es igual al resultado del calculo del check de 10 | no cumple -> fuera
    # 4.2. Si tiene 13 digitos => valido si el check digit es igual al resultado del calculo del check de 13 | no cumple -> fuera

    
# Los codigos ISBN tienen 10 o 13 caracteres y estos ultimos siempre empiezan con 978 o 979 (sin contar guiones o espacios), eso lo checkea el codigo?
def validar_isbn(isbn):
    limpio = isbn.replace("-", "").replace(" ", "")
    if len(limpio) == 10:
        return _validar_isbn10(limpio)
    if len(limpio) == 13:
        return _validar_isbn13(limpio)
    return False

# Como se busca el modulo de 11 el maximo posible es 10 y como 10 son 2 digitos se representa con una X
def _validar_isbn10(isbn):
    if not isbn[:9].isdigit():
        return False
    if not (isbn[9].isdigit() or isbn[9].upper() == "X"):
        return False
    total = 0
    for i, caracter in enumerate(isbn[:9]):
        total += int(caracter) * (10 - i)
    checksum = (11 - (total % 11)) % 11
    expected = "X" if checksum == 10 else str(checksum)
    return isbn[9].upper() == expected

# A diferencia del ISBN-10, el ISBN-13 utiliza base 10 por lo que su maximo numero va a ser un 9 y no va a encontrarse nunca una X al final del codigo ademas se verifica que el codigo empiece con 978 o 979, si no es asi se descarta el codigo
def _validar_isbn13(isbn):
    if not isbn.isdigit():
        return False
    if not (isbn.startswith("978") or isbn.startswith("979")):
        return False
    total = 0
    for i, caracter in enumerate(isbn[:12]):
        peso = 1 if i % 2 == 0 else 3
        total += int(caracter) * peso
    checksum = (10 - (total % 10)) % 10
    return str(checksum) == isbn[12]


if __name__ == "__main__":
    # ------------ ISBN-13 VALIDOS ------------
    assert validar_isbn("9780306406157")    
    assert validar_isbn("9790000000001")        # prefijo 979
    assert validar_isbn("978-0-306-40615-7")    # con guiones

    # ------------ ISBN-13 INVALIDOS ------------
    assert not validar_isbn("9780306406158")    # Check digit incorrecto
    assert not validar_isbn("1234567890128")    # No empieza con 978 o 979
    assert not validar_isbn("97803064061AB")    # Tiene letras

    #------------ ISBN-10 VALIDOS ------------
    assert validar_isbn("0306406152")           
    assert validar_isbn("097522980X")           # Check digit es X
    assert validar_isbn("0-306-40615-2")        # con guiones

    #------------ ISBN-10 INVALIDOS ------------
    assert not validar_isbn ("0306406153")      # Check digit incorrecto
    assert not validar_isbn ("03X6406152")      # X en el medio, no al final

    #------------ CASOS GENERALES ------------
    assert not validar_isbn ("12345")           # Longitud invalida
    assert not validar_isbn ("")                # Cadena vacia

    print("Todos los tests de ISBN pasaron correctamente")