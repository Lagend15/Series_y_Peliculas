class Pelicula:
    id: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    titulo: str = None

    def GetTitulo(self) -> str:
        return self.titulo
    def SetTitulo(self, value: str) -> None:
        self.titulo = value

    categoria: int = 0

    def GetCategoria(self) -> int:
        return self.categoria
    def SetCategoria(self, value: int) -> None:
        self.categoria = value

    estado: int = 0

    def GetEstado(self) -> int:
        return self.estado
    def SetEstado(self, value: int) -> None:
        self.estado = value

    director: int = 0

    def GetDirector(self) -> int:
        return self.director
    def SetDirector(self, value: int) -> None:
        self.director = value

    duracion: int = 0

    def GetDuracion(self) -> int:
        return self.duracion
    def SetDuracion(self, value: int) -> None:
        self.duracion = value

    anio_estreno: int = 0

    def GetAnioEstreno(self) -> int:
        return self.anio_estreno
    def SetAnioEstreno(self, value: int) -> None:
        self.anio_estreno = value
