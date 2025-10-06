import mysql.connector
from Entidades.Estados import Estados
from Entidades.Actores import Actores
from Entidades.Pelicula import Pelicula
from Entidades.Serie import Serie

class Conexion:
    
    def __init__(self):
        self.config = {
            "host": "localhost",
            "port": 3306,
            "user": "user_python",
            "password": "Clas3s1Nt2024_!",
            "database": "db_series_peliculas"
        }

    # ==============================
    # METODOS GENERALES
    # ==============================
    def _get_conexion(self):
        return mysql.connector.connect(**self.config)

    # ==============================
    # CRUD PARA ESTADOS
    # ==============================
    def CargarEstados(self) -> list:
        lista = []
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_select_estados")
            for result in cursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    entidad = Estados()
                    entidad.SetId(row[0])
                    entidad.SetNombre(row[1])
                    lista.append(entidad)
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al cargar estados:", e)
        return lista

    def InsertarEstado(self, nombre: str) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_insert_estado", [nombre])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al insertar estado:", e)

    def ActualizarEstado(self, id_estado: int, nombre: str) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_update_estado", [id_estado, nombre])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al actualizar estado:", e)

    def EliminarEstado(self, id_estado: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_delete_estado", [id_estado])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al eliminar estado:", e)

    # ==============================
    # CRUD PARA ACTORES
    # ==============================
    def CargarActores(self) -> list:
        lista = []
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_select_actores")
            for result in cursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    entidad = Actores()
                    entidad.SetId(row[0])
                    entidad.SetNombre(row[1])
                    entidad.SetNacionalidad(row[2])
                    lista.append(entidad)
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al cargar actores:", e)
        return lista

    def InsertarActor(self, nombre: str, nacionalidad: str) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_insert_actor", [nombre, nacionalidad])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al insertar actor:", e)

    def ActualizarActor(self, id_actor: int, nombre: str, nacionalidad: str) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_update_actor", [id_actor, nombre, nacionalidad])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al actualizar actor:", e)

    def EliminarActor(self, id_actor: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_delete_actor", [id_actor])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al eliminar actor:", e)

    # ==============================
    # CRUD PARA PELICULAS
    # ==============================
    def CargarPeliculas(self) -> list:
        lista = []
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_select_peliculas")
            for result in cursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    entidad = Pelicula()
                    entidad.SetId(row[0])
                    entidad.SetTitulo(row[1])
                    entidad.SetCategoria(row[2])
                    entidad.SetEstado(row[3])
                    entidad.SetDirector(row[4])
                    entidad.SetDuracion(row[5])
                    entidad.SetAnioEstreno(row[6])
                    lista.append(entidad)
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al cargar películas:", e)
        return lista

    def InsertarPelicula(self, titulo: str, id_categoria: int, id_estado: int, id_director: int, duracion: int, anio_estreno: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_insert_pelicula", [titulo, id_categoria, id_estado, id_director, duracion, anio_estreno])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al insertar película:", e)

    def ActualizarPelicula(self, id_pelicula: int, titulo: str, id_categoria: int, id_estado: int, id_director: int, duracion: int, anio_estreno: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_update_pelicula", [id_pelicula, titulo, id_categoria, id_estado, id_director, duracion, anio_estreno])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al actualizar película:", e)

    def EliminarPelicula(self, id_pelicula: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_delete_pelicula", [id_pelicula])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al eliminar película:", e)

    # ==============================
    # CRUD PARA SERIES
    # ==============================
    def CargarSeries(self) -> list:
        lista = []
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_select_series")
            for result in cursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    entidad = Serie()
                    entidad.SetId(row[0])
                    entidad.SetTitulo(row[1])
                    entidad.SetCategoria(row[2])
                    entidad.SetEstado(row[3])
                    entidad.SetDirector(row[4])
                    entidad.SetAnioInicio(row[5])
                    entidad.SetAnioFin(row[6])
                    lista.append(entidad)
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al cargar series:", e)
        return lista

    def InsertarSerie(self, titulo: str, id_categoria: int, id_estado: int, id_director: int, anio_inicio: int, anio_fin: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_insert_serie", [titulo, id_categoria, id_estado, id_director, anio_inicio, anio_fin])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al insertar serie:", e)

    def ActualizarSerie(self, id_serie: int, titulo: str, id_categoria: int, id_estado: int, id_director: int, anio_inicio: int, anio_fin: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_update_serie", [id_serie, titulo, id_categoria, id_estado, id_director, anio_inicio, anio_fin])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al actualizar serie:", e)

    def EliminarSerie(self, id_serie: int) -> None:
        try:
            conexion = self._get_conexion()
            cursor = conexion.cursor()
            cursor.callproc("proc_delete_serie", [id_serie])
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("❌ Error al eliminar serie:", e)

