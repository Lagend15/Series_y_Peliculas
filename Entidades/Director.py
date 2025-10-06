class Director:

    id_director: int = 0;
 
    def GetId_director(self) -> int:

        return self.id_director;

    def SetId_director(self, value: int) -> None:

        self.id_director = value;
 
    nombre_director: str = None;
 
    def GetNombre_director(self) -> str:

        return self.nombre_director;

    def SetNombre_director(self, value: str) -> None:

        self.nombre_director = value;
 
    nacionalidad: str = None;
 
    def GetNacionalidad(self) -> str:

        return self.nacionalidad;

    def SetNacionalidad(self, value: str) -> None:

        self.nacionalidad = value;

 