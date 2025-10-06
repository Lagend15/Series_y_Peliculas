class Usuario:

    id_usuario: int = 0;
 
    def GetId_usuario(self) -> int:

        return self.id_usuario;

    def SetId_usuario(self, value: int) -> None:

        self.id_usuario = value;
 
    nombre_usuario: str = None;
 
    def GetNombre_usuario(self) -> str:

        return self.nombre_usuario;

    def SetNombre_usuario(self, value: str) -> None:

        self.nombre_usuario = value;
 
    correo: str = None;
 
    def GetCorreo(self) -> str:

        return self.correo;

    def SetCorreo(self, value: str) -> None:

        self.correo = value;
 
    contrasena: str = None;
 
    def GetContrasena(self) -> str:

        return self.contrasena;

    def SetContrasena(self, value: str) -> None:

        self.contrasena = value;
 
    fecha_registro: str = None;
 
    def GetFecha_registro(self) -> str:

        return self.fecha_registro;

    def SetFecha_registro(self, value: str) -> None:

        self.fecha_registro = value;

 
 