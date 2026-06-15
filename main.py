from sistema.biblioteca import Biblioteca

b1 = Biblioteca()
b2 = Biblioteca()

print(
    "Singleton:",
    b1 is b2
)