class Administrador:
    def _init_(self, coordinadores, docentes, usuario, contraseña):
        self.coordinadores = coordinadores
        self.docentes = docentes
        self.usuario = usuario
        self.contraseña = contraseña
        self.docentes_programas = {}
        self.lista_docentes = []
        self.investigacion = ['Investigacion 1', 'Investigacion 2', 'Investigacion 3']
        self.asignaciones_investigacion = {}

    def autenticacion_coordinador(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == self.usuario and contraseña == self.contraseña:
            print("Autenticación exitosa.")
        else:
            print("Credenciales inválidas.")

    def autenticacion_docente(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == self.usuario and contraseña == self.contraseña:
            print("Autenticación exitosa.")
        else:
            print("Credenciales inválidas.")

    def agregar_docente_programa(self, docente, programa):
        if programa not in self.docentes_programas:
            self.docentes_programas[programa] = []
        self.docentes_programas[programa].append(docente)

    def crear_lista_docentes(self, docente):

        self.lista_docentes.append(docente)


class Coordinador(Administrador):
    def _init_(self, nombre, usuario, contraseña):
        super()._init_(coordinadores=[], docentes=[], usuario=usuario, contraseña=contraseña)
        self.nombre = nombre

    def clasificar_docente_programa(self, programa):
        if programa in self.docentes_programas:
            return [docente for docente in self.docentes_programas[programa]]
        else:
            return []

    def clasificar_docente_gdi(self):
        for investigacion in self.investigacion:
            docente = Docente('usuario', 'contraseña', 'Nombre del docente')
            self.asignaciones_investigacion[investigacion] = docente

class Docente(Administrador):
    def _init_(self, usuario, contraseña, nombre):
        super()._init_(coordinadores=[], docentes=[], usuario=usuario, contraseña=contraseña)
        self.nombre = nombre

class Informacion:
    def _init_(self, producto):
        self.producto = producto