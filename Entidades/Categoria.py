class Categoria:

    id_categoria: int = 0;
 
    def GetId_categoria(self) -> int:

        return self.id_categoria;

    def SetId_categoria(self, value: int) -> None:

        self.id_categoria = value;
 
    nombre_categoria: str = None;
 
    def GetNombre_categoria(self) -> str:

        return self.nombre_categoria;

    def SetNombre_categoria(self, value: str) -> None:

        self.nombre_categoria = value;

 