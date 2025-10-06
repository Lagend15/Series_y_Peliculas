class Serie:
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

    anio_inicio: int = 0

    def GetAnioInicio(self) -> int:
        return self.anio_inicio
    def SetAnioInicio(self, value: int) -> None:
        self.anio_inicio = value

    anio_fin: int = 0

    def GetAnioFin(self) -> int:
        return self.anio_fin
    def SetAnioFin(self, value: int) -> None:
        self.anio_fin = value
