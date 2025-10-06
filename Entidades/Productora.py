class Productora:

    id_productora: int = 0;
 
    def GetId_productora(self) -> int:

        return self.id_productora;

    def SetId_productora(self, value: int) -> None:

        self.id_productora = value;
 
    nombre_productora: str = None;
 
    def GetNombre_productora(self) -> str:

        return self.nombre_productora;

    def SetNombre_productora(self, value: str) -> None:

        self.nombre_productora = value;
 
    id_pais: int = 0;
 
    def GetId_pais(self) -> int:

        return self.id_pais;

    def SetId_pais(self, value: int) -> None:

        self.id_pais = value;

 