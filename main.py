class Entregable:  # Interfaz 'Entregable'
    def entregar(self):
        pass

    def devolver(self):
        pass

    def isEntregado(self):
        pass

    def compareTo(self):
        pass


class Serie(Entregable):  # Heredamos los métodos de la interfaz 'Entregable' y los desarrollamos
    # Propiedades
    titulo = ''
    numero_de_temporadas = 3
    entregado = False
    genero = ''
    creador = ''

    # Constructor
    def __init__(self, titulo, genero, creador):
        self.titulo = titulo
        self.genero = genero
        self.creador = creador

    # Get / Set
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_numero_de_temporadas(self):
        return self.numero_de_temporadas

    def set_numero_de_temporadas(self, numero_de_temporadas):
        self.numero_de_temporadas = numero_de_temporadas

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_creador(self):
        return self.creador

    def set_creador(self, creador):
        self.creador = creador

    # Métodos
    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, objeto):
        print('La serie ' + str(self.titulo) + ' tiene ' + str(self.numero_de_temporadas) + ' temporadas')
        print('La serie ' + str(objeto.titulo) + ' tiene ' + str(objeto.numero_de_temporadas) + ' temporadas')

    def __str__(self):  # Sobreescribimos el método Str con los datos del objeto.
        texto = "Titulo: {0} - Numero de temporadas: {1} - Género: {2} - Creador: {3}"
        return texto.format(self.titulo, self.numero_de_temporadas, self.genero, self.creador)


class Videojuego(Entregable):
    # Propiedades:
    titulo = ''
    horas_estimadas = 10
    entregado = False
    genero = ''
    companyia = ''

    # Constructor:
    def __init__(self, titulo, genero, companyia):
        self.titulo = titulo
        self.genero = genero
        self.companyia = companyia

    # Getters y Setters:
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_horas_estimadas(self):
        return self.horas_estimadas

    def set_horas_estimadas(self, horas_estimadas):
        self.horas_estimadas = horas_estimadas

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_companyia(self):
        return self.companyia

    def set_companyia(self, companyia):
        self.companyia = companyia

    # Métodos
    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, objeto):
        print('El videojuego ' + str(self.titulo) + ' tiene ' + str(self.horas_estimadas) + ' horas estimadas')
        print('El videojuego ' + str(objeto.titulo) + ' tiene ' + str(objeto.horas_estimadas) + ' horas estimadas')

    def __str__(self): # Sobreescribimos el método Str con los datos del objeto.
        texto = "Titulo: {0} - Horas estimadas: {1} - Género: {2} - Compañía: {3}"
        return texto.format(self.titulo, self.horas_estimadas, self.genero, self.companyia)


videojuegos = []
series = []

serie1 = Serie('Prison Break', 'Acción', 'Paul Scheuring')
series.append(serie1)
serie2 = Serie('Perdidos', 'Suspense', 'Stephen Williams')
series.append(serie2)
serie3 = Serie('House', 'Suspense', 'David Shore')
series.append(serie3)
serie4 = Serie('The Walking Dead', 'terror', 'Frank Darabont')
series.append(serie4)
serie5 = Serie('The man in the high castle', 'Ciencia ficción', 'Frank Spotnitz')
series.append(serie5)

juego1 = Videojuego('Metal Gear Solid', 'Acción', 'Konami')
videojuegos.append(juego1)
juego2 = Videojuego('Tekken 3', 'Acción', 'Namco')
videojuegos.append(juego2)
juego3 = Videojuego('Final Fantasy VIII', 'Rol', 'Squaresoft')
videojuegos.append(juego3)
juego4 = Videojuego('Sniper Elite', 'Shooter', 'Rebellion')
videojuegos.append(juego4)
juego5 = Videojuego('Counter Strike', 'Shooter', 'Valve')
videojuegos.append(juego5)

Videojuego.entregar(juego1)
Videojuego.entregar(juego2)
Serie.entregar(serie2)
Serie.entregar(serie3)

for e in series:  # Contamos las series entregadas y las devolvemos
    if Serie.isEntregado(e) == True:
        print("La serie " + e.titulo + " estaba entregada, y ahora se ha devuelto\n")
        Serie.devolver(e)

for e in videojuegos:  # Contamos los videojuegos entregados y los devolvemos
    if Videojuego.isEntregado(e) == True:
        print("El videojuego " + e.titulo + " estaba entregado, y ahora se ha devuelto\n")
        Videojuego.devolver(e)


serie1.set_numero_de_temporadas(6)
serie2.set_numero_de_temporadas(4)
juego2.set_horas_estimadas(14)
juego3.set_horas_estimadas(11)

series.sort(key=lambda x: x.numero_de_temporadas, reverse=True)
print("La serie con mayor número de temporadas es: ")
print(series[0])  # La serie con mayor número de temporadas
videojuegos.sort(key=lambda x: x.horas_estimadas, reverse=True)
print("El videojuego con más horas estimadas es: ")
print(videojuegos[0])  # El videojuego con más horas estimadas


