class Actor:

    id_actor: int = 0;
 
    def GetId_actor(self) -> int:

        return self.id_actor;

    def SetId_actor(self, value: int) -> None:

        self.id_actor = value;
 
    nombre_actor: str = None;
 
    def GetNombre_actor(self) -> str:

        return self.nombre_actor;

    def SetNombre_actor(self, value: str) -> None:

        self.nombre_actor = value;
 
    nacionalidad: str = None;
 
    def GetNacionalidad(self) -> str:

        return self.nacionalidad;

    def SetNacionalidad(self, value: str) -> None:

        self.nacionalidad = value;

 
# Entidades/Categoria.py

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

 