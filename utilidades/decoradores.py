def registrar_accion(func):

    def wrapper(*args, **kwargs):

        print(f"[LOG] Ejecutando {func.__name__}")

        resultado = func(*args, **kwargs)

        print(f"[LOG] Finalizó {func.__name__}")

        return resultado

    return wrapper