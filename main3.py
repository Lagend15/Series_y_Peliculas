from Repositorios.Conexion import Conexion

def main():
    conexion = Conexion()
    print("✅ Conexión a base de datos db_series_peliculas exitosa\n")

    # ==============================
    # ESTADOS
    # ==============================
    print("📄 Estados actuales:")
    estados = conexion.CargarEstados()
    for e in estados:
        print(f"{e.GetId()}, {e.GetNombre()}")

    # ==============================
    # ACTORES
    # ==============================
    print("\n📄 Actores actuales:")
    actores = conexion.CargarActores()
    for a in actores:
        print(f"{a.GetId()}, {a.GetNombre()}, {a.GetNacionalidad()}")

    # ==============================
    # PELÍCULAS
    # ==============================
    print("\n📄 Películas actuales:")
    peliculas = conexion.CargarPeliculas()
    for p in peliculas:
        print(f"{p.GetId()}, {p.GetTitulo()}, Cat:{p.GetCategoria()}, Estado:{p.GetEstado()}, Dir:{p.GetDirector()}, Dur:{p.GetDuracion()}, Año:{p.GetAnioEstreno()}")

    # ==============================
    # SERIES
    # ==============================
    print("\n📄 Series actuales:")
    series = conexion.CargarSeries()
    for s in series:
        print(f"{s.GetId()}, {s.GetTitulo()}, Cat:{s.GetCategoria()}, Estado:{s.GetEstado()}, Dir:{s.GetDirector()}, Inicio:{s.GetAnioInicio()}, Fin:{s.GetAnioFin()}")

    # ==============================
    # EJEMPLOS DE CRUD
    # ==============================

    # ------------------------------
    # ESTADOS
    # ------------------------------
    # conexion.InsertarEstado("Prueba Estado")
    # conexion.ActualizarEstado(1, "Disponible")
    # conexion.EliminarEstado(8)

    # ------------------------------
    # ACTORES
    # ------------------------------
    # conexion.InsertarActor("Actor Prueba", "Pais Prueba")
    # conexion.ActualizarActor(1, "Actor Actualizado", "Pais Actualizado")
    # conexion.EliminarActor(1)

    # ------------------------------
    # PELÍCULAS
    # ------------------------------
    # conexion.InsertarPelicula("Película Prueba", 1, 1, 1, 120, 2025)
    # conexion.ActualizarPelicula(1, "Película Actualizada", 1, 1, 1, 150, 2024)
    # conexion.EliminarPelicula(1)

    # ------------------------------
    # SERIES
    # ------------------------------
    # conexion.InsertarSerie("Serie Prueba", 1, 1, 1, 2025, 2026)
    # conexion.ActualizarSerie(1, "Serie Actualizada", 1, 1, 1, 2020, 2022)
    # conexion.EliminarSerie(1)

if __name__ == "__main__":
    main()
