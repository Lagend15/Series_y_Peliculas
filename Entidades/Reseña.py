class Reseña:

    id_reseña: int = 0;
 
    def GetId_reseña(self) -> int:

        return self.id_reseña;

    def SetId_reseña(self, value: int) -> None:

        self.id_reseña = value;
 
    id_usuario: int = 0;
 
    def GetId_usuario(self) -> int:

        return self.id_usuario;

    def SetId_usuario(self, value: int) -> None:

        self.id_usuario = value;
 
    tipo_contenido: str = None;
 
    def GetTipo_contenido(self) -> str:

        return self.tipo_contenido;

    def SetTipo_contenido(self, value: str) -> None:

        self.tipo_contenido = value;
 
    id_contenido: int = 0;
 
    def GetId_contenido(self) -> int:

        return self.id_contenido;

    def SetId_contenido(self, value: int) -> None:

        self.id_contenido = value;
 
    comentario: str = None;
 
    def GetComentario(self) -> str:

        return self.comentario;

    def SetComentario(self, value: str) -> None:

        self.comentario = value;
 
    calificacion: int = 0;
 
    def GetCalificacion(self) -> int:

        return self.calificacion;

    def SetCalificacion(self, value: int) -> None:

        self.calificacion = value;
 
    fecha: str = None;
 
    def GetFecha(self) -> str:

        return self.fecha;

    def SetFecha(self, value: str) -> None:

        self.fecha = value;

 