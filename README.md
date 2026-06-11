# 📚 Biblioteca App - Programación Orientada a Objetos en Python

## 📖 Descripción del Proyecto

Biblioteca App es una aplicación desarrollada en Python utilizando el paradigma de **Programación Orientada a Objetos (POO)**.

El objetivo del proyecto es demostrar la creación e interacción de clases, objetos, atributos y métodos mediante un sistema básico de gestión de biblioteca. La aplicación permite registrar libros y usuarios dentro de una biblioteca digital y visualizar la información almacenada.

Este proyecto ha sido estructurado siguiendo una organización modular para facilitar el mantenimiento, la reutilización del código y la comprensión de los conceptos fundamentales de la POO.

---

## 🎯 Objetivos de Aprendizaje

Mediante este proyecto el estudiante podrá:

- Comprender el concepto de clase y objeto.
- Crear e instanciar objetos en Python.
- Definir atributos y métodos.
- Aplicar la modularización del código.
- Organizar proyectos mediante carpetas y módulos.
- Relacionar múltiples clases dentro de una misma aplicación.
- Aplicar buenas prácticas de programación orientada a objetos.

---

## 🏗️ Estructura del Proyecto

```text
biblioteca_app/
│
├── modelos/
│   ├── libro.py
│   └── usuario.py
│
├── servicios/
│   └── biblioteca.py
│
└── main.py
```

### Descripción de Carpetas

| Carpeta | Función |
|----------|----------|
| modelos | Contiene las clases que representan las entidades principales del sistema. |
| servicios | Contiene la lógica de gestión y administración de objetos. |
| main.py | Punto de entrada de la aplicación. |

---

## 📚 Clases Implementadas

### Libro

Representa un libro dentro del sistema.

**Atributos:**

- titulo
- autor
- isbn

**Métodos:**

- mostrar_informacion()
- __str__()

---

### Usuario

Representa un usuario registrado en la biblioteca.

**Atributos:**

- nombre
- correo

**Métodos:**

- mostrar_informacion()
- __str__()

---

### Biblioteca

Administra la colección de libros y usuarios.

**Atributos:**

- libros
- usuarios

**Métodos:**

- agregar_libro()
- agregar_usuario()
- mostrar_libros()
- mostrar_usuarios()

---

## 🔄 Funcionamiento General

El programa realiza las siguientes acciones:

1. Crea objetos de tipo Libro.
2. Crea objetos de tipo Usuario.
3. Crea una instancia de Biblioteca.
4. Registra libros en la biblioteca.
5. Registra usuarios en la biblioteca.
6. Muestra la información almacenada.

---

## 💻 Ejecución del Programa

Ubicarse en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

---

## 🖥️ Salida Esperada

```text
=== LIBROS REGISTRADOS ===
Python para Principiantes - Juan Pérez
Programación Orientada a Objetos - María Gómez

=== USUARIOS REGISTRADOS ===
Carlos López
```

---

## 🧩 Conceptos de Programación Orientada a Objetos Aplicados

### Clase

Una clase funciona como una plantilla para crear objetos.

Ejemplo:

```python
class Libro:
    pass
```

---

### Objeto

Un objeto es una instancia creada a partir de una clase.

Ejemplo:

```python
libro1 = Libro(
    "Python para Principiantes",
    "Juan Pérez",
    "ISBN001"
)
```

---

### Atributos

Son las características que describen a un objeto.

Ejemplo:

```python
self.titulo
self.autor
self.isbn
```

---

### Métodos

Son las acciones que puede realizar un objeto.

Ejemplo:

```python
def mostrar_informacion(self):
    pass
```

---

### Modularización

El proyecto se encuentra dividido en varios archivos para mejorar la organización y facilitar el mantenimiento del software.

Ventajas:

- Mayor claridad.
- Reutilización de código.
- Escalabilidad.
- Mantenimiento simplificado.
- Mejor trabajo colaborativo.

---

## 🚀 Posibles Mejoras Futuras

Este proyecto puede ampliarse incorporando funcionalidades como:

- Registro de préstamos.
- Devolución de libros.
- Búsqueda por ISBN.
- Eliminación de registros.
- Persistencia de datos en archivos JSON.
- Persistencia de datos en bases de datos.
- Interfaz gráfica con Tkinter.
- Sistema de autenticación de usuarios.

---

## 👨‍💻 Tecnologías Utilizadas

- Python 3.14.x
- Programación Orientada a Objetos (POO)

---

## 📑 Autor

DevOsLink

---

## 📄 Licencia

Este proyecto puede utilizarse con fines académicos y de aprendizaje.