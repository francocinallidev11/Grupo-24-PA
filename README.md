# Grupo-24-PA

[![Ejecutar tests con assert](https://github.com/francocinallidev11/Grupo-24-PA/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/francocinallidev11/Grupo-24-PA/actions/workflows/tests.yml)

## Trabajo Práctico Integrador Final

Sistema de Gestión de Biblioteca Digital desarrollado en Python para la materia Programación Avanzada.

## Integrantes

* Alejo Hernandez
* Franco Cinalli
* Tomás Ferrufino
* Ariel Dinocco

## Descripción

El proyecto consiste en el desarrollo de un sistema para administrar una biblioteca digital utilizando Programación Orientada a Objetos (POO).

El sistema permitirá:

* Gestión de libros.
* Gestión de usuarios.
* Registro de préstamos y devoluciones.
* Consulta de préstamos activos.

## Conceptos Aplicados

* Encapsulamiento
* Herencia
* Polimorfismo
* Agregación
* Composición
* Decoradores
* Metaclases
* Patrón de Diseño Singleton

## Estructura del Proyecto

```text
Grupo-24-PA/
│
├── modelos/
│   ├── libro.py
│   ├── persona.py
│   ├── usuario.py
│   └── prestamo.py
│
├── sistema/
│   └── biblioteca.py
│
├── utilidades/
│   ├── decoradores.py
│   └── metaclases.py
│
├── uml/
│
├── main.py
└── README.md
```

## Tecnologías Utilizadas

* Python 3
* Git
* GitHub
* Mermaid (UML)

## Ejecución

Clonar el repositorio:

```bash
git clone https://github.com/francocinallidev11/Grupo-24-PA.git
```

Ingresar al proyecto:

```bash
cd Grupo-24-PA
```

Ejecutar:

```bash
python main.py
```

## UML

```mermaid
classDiagram
    class Persona {
        +str nombre
        +str apellido
        +str dni
        +mostrar_info()
    }
    class Usuario {
        +str correo
        +mostrar_info()
    }
    class Libro {
        +str titulo
        +str autor
        +int anio
        +str isbn
        +int paginas
        +mostrar_info()
    }
    class Prestamo {
        +date fecha_prestamo
        +date fecha_devolucion
        +bool activo
        +devolver()
        +mostrar_info()
    }
    class Biblioteca {
        <<Singleton>>
        +list libros
        +list usuarios
        +list prestamos
        +buscar_libro(isbn)
        +agregar_libro(libro)
        +eliminar_libro(isbn)
        +modificar_libro(isbn, cambios)
        +listar_libros()
        +buscar_usuario(dni)
        +agregar_usuario(usuario)
        +eliminar_usuario(dni)
        +modificar_usuario(dni, cambios)
        +listar_usuarios()
        +buscar_prestamo_activo(isbn)
        +registrar_prestamo(isbn, dni)
        +registrar_devolucion(isbn)
        +listar_prestamos_activos()
        +listar_prestamos()
    }
    Persona <|-- Usuario : herencia
    Biblioteca o-- Libro : agregacion
    Biblioteca o-- Usuario : agregacion
    Biblioteca o-- Prestamo : agregacion
    Prestamo *-- Libro : composicion
    Prestamo *-- Usuario : composicion
```

## Estado del Proyecto

Finalizado.
