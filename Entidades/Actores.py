class Actores:
    id: int = 0
    nombre: str = None
    nacionalidad: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetNacionalidad(self) -> str:
        return self.nacionalidad
    def SetNacionalidad(self, value: str) -> None:
        self.nacionalidad = value
