class Pais:
    id_pais: int = 0;
 
    def GetId_pais(self) -> int:
        return self.id_pais;
    def SetId_pais(self, value: int) -> None:
        self.id_pais = value;
 
    nombre_pais: str = None;
 
    def GetNombre_pais(self) -> str:
        return self.nombre_pais;
    def SetNombre_pais(self, value: str) -> None:
        self.nombre_pais = value;