# ==========================================================
# CLASE: Usuario
# ----------------------------------------------------------
# Esta clase representa a un usuario dentro de un sistema
# de biblioteca digital.
#
# Cada objeto creado a partir de esta clase almacenará la
# información básica de una persona que puede solicitar,
# consultar o gestionar libros dentro del sistema.
#
# Atributos:
# - nombre : Nombre completo del usuario.
# - correo : Correo electrónico del usuario.
#
# Ejemplo de creación:
#
# usuario1 = Usuario(
#     "María López",
#     "maria.lopez@correo.com"
# )
# ==========================================================

class Usuario:

    def __init__(self, nombre, correo):
        """
        Constructor de la clase Usuario.

        Este método se ejecuta automáticamente cuando se crea
        un nuevo objeto Usuario.

        Parámetros:
            nombre (str): Nombre del usuario.
            correo (str): Correo electrónico del usuario.

        Los datos recibidos se almacenan como atributos de
        instancia para que cada objeto tenga su propia
        información.
        """

        # Almacena el nombre del usuario.
        self.nombre = nombre

        # Almacena el correo electrónico del usuario.
        self.correo = correo

    def mostrar_informacion(self):
        """
        Devuelve una cadena de texto con la información
        principal del usuario.

        Retorna:
            str: Nombre y correo electrónico del usuario.

        Ejemplo de salida:
            María López (maria.lopez@correo.com)
        """
        return f"{self.nombre} ({self.correo})"

    def __str__(self):
        """
        Método especial utilizado por Python para definir
        cómo se mostrará el objeto cuando se imprima con
        la función print().

        Retorna:
            str: Nombre del usuario.

        Ejemplo:
            print(usuario)

        Salida:
            María López
        """
        return self.nombre