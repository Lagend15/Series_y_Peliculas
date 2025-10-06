class Pelicula:

    id_pelicula: int = 0;
 
    def GetId_pelicula(self) -> int:

        return self.id_pelicula;

    def SetId_pelicula(self, value: int) -> None:

        self.id_pelicula = value;
 
    titulo: str = None;
 
    def GetTitulo(self) -> str:

        return self.titulo;

    def SetTitulo(self, value: str) -> None:

        self.titulo = value;
 
    id_categoria: int = 0;
 
    def GetId_categoria(self) -> int:

        return self.id_categoria;

    def SetId_categoria(self, value: int) -> None:

        self.id_categoria = value;
 
    id_estado: int = 0;
 
    def GetId_estado(self) -> int:

        return self.id_estado;

    def SetId_estado(self, value: int) -> None:

        self.id_estado = value;
 
    id_director: int = 0;
 
    def GetId_director(self) -> int:

        return self.id_director;

    def SetId_director(self, value: int) -> None:

        self.id_director = value;
 
    duracion: int = 0;
 
    def GetDuracion(self) -> int:

        return self.duracion;

    def SetDuracion(self, value: int) -> None:

        self.duracion = value;
 
    anio_estreno: int = 0;
 
    def GetAnio_estreno(self) -> int:

        return self.anio_estreno;

    def SetAnio_estreno(self, value: int) -> None:

        self.anio_estreno = value;

 