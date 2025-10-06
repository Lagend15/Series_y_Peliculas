class Estado:

    id_estado: int = 0;
 
    def GetId_estado(self) -> int:

        return self.id_estado;

    def SetId_estado(self, value: int) -> None:

        self.id_estado = value;
 
    nombre_estado: str = None;
 
    def GetNombre_estado(self) -> str:

        return self.nombre_estado;

    def SetNombre_estado(self, value: str) -> None:

        self.nombre_estado = value;

 