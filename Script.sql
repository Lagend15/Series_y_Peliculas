
CREATE DATABASE db_series_peliculas;
USE db_series_peliculas;

-- ============================================================
-- TABLAS MAESTRAS
-- ============================================================

CREATE TABLE estados (
  id_estado INT AUTO_INCREMENT PRIMARY KEY,
  nombre_estado VARCHAR(50) NOT NULL
);

CREATE TABLE categorias (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nombre_categoria VARCHAR(100) NOT NULL
);

CREATE TABLE paises (
  id_pais INT AUTO_INCREMENT PRIMARY KEY,
  nombre_pais VARCHAR(100) NOT NULL
);

CREATE TABLE directores (
  id_director INT AUTO_INCREMENT PRIMARY KEY,
  nombre_director VARCHAR(100) NOT NULL,
  nacionalidad VARCHAR(50)
);

CREATE TABLE actores (
  id_actor INT AUTO_INCREMENT PRIMARY KEY,
  nombre_actor VARCHAR(100) NOT NULL,
  nacionalidad VARCHAR(50)
);

CREATE TABLE productoras (
  id_productora INT AUTO_INCREMENT PRIMARY KEY,
  nombre_productora VARCHAR(100) NOT NULL,
  id_pais INT,
  FOREIGN KEY (id_pais) REFERENCES paises(id_pais)
);

CREATE TABLE usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre_usuario VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL UNIQUE,
  contrasena VARCHAR(100) NOT NULL,
  fecha_registro DATE
);

-- ============================================================
-- TABLAS DE CONTENIDO
-- ============================================================

CREATE TABLE peliculas (
  id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100) NOT NULL,
  id_categoria INT,
  id_estado INT,
  id_director INT,
  duracion INT,
  anio_estreno INT,
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
  FOREIGN KEY (id_estado) REFERENCES estados(id_estado),
  FOREIGN KEY (id_director) REFERENCES directores(id_director)
);

CREATE TABLE series (
  id_serie INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100) NOT NULL,
  id_categoria INT,
  id_estado INT,
  id_director INT,
  anio_inicio INT,
  anio_fin INT,
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
  FOREIGN KEY (id_estado) REFERENCES estados(id_estado),
  FOREIGN KEY (id_director) REFERENCES directores(id_director)
);

-- ============================================================
-- RELACIONES N:N
-- ============================================================

CREATE TABLE peliculas_actores (
  id_pelicula INT,
  id_actor INT,
  PRIMARY KEY (id_pelicula, id_actor),
  FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula),
  FOREIGN KEY (id_actor) REFERENCES actores(id_actor)
);

CREATE TABLE series_actores (
  id_serie INT,
  id_actor INT,
  PRIMARY KEY (id_serie, id_actor),
  FOREIGN KEY (id_serie) REFERENCES series(id_serie),
  FOREIGN KEY (id_actor) REFERENCES actores(id_actor)
);

CREATE TABLE peliculas_productoras (
  id_pelicula INT,
  id_productora INT,
  PRIMARY KEY (id_pelicula, id_productora),
  FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula),
  FOREIGN KEY (id_productora) REFERENCES productoras(id_productora)
);

CREATE TABLE series_productoras (
  id_serie INT,
  id_productora INT,
  PRIMARY KEY (id_serie, id_productora),
  FOREIGN KEY (id_serie) REFERENCES series(id_serie),
  FOREIGN KEY (id_productora) REFERENCES productoras(id_productora)
);

-- ============================================================
-- TABLAS DE USUARIO Y CONTENIDO PERSONALIZADO
-- ============================================================

CREATE TABLE listas (
  id_lista INT AUTO_INCREMENT PRIMARY KEY,
  nombre_lista VARCHAR(100) NOT NULL,
  id_usuario INT,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

CREATE TABLE listas_contenido (
  id_lista INT,
  tipo_contenido ENUM('Serie','Pelicula') NOT NULL,
  id_contenido INT NOT NULL,
  PRIMARY KEY (id_lista, tipo_contenido, id_contenido),
  FOREIGN KEY (id_lista) REFERENCES listas(id_lista)
);

CREATE TABLE reseñas (
  id_reseña INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT,
  tipo_contenido ENUM('Serie','Pelicula') NOT NULL,
  id_contenido INT NOT NULL,
  comentario TEXT,
  calificacion INT CHECK (calificacion BETWEEN 1 AND 5),
  fecha DATE,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-- ============================================================
-- PROCEDIMIENTOS ALMACENADOS
-- ============================================================

-- para la tabla estados


-- Seleccionar todos los estados
DELIMITER $$
CREATE PROCEDURE proc_select_estados()
BEGIN
    SELECT id_estado, nombre_estado FROM estados;
END$$
DELIMITER ;


DELIMITER $$

-- Insertar estado
CREATE PROCEDURE proc_insert_estado(
    IN p_nombre_estado VARCHAR(50)
)
BEGIN
    INSERT INTO estados(nombre_estado)
    VALUES (p_nombre_estado);
END$$

-- Actualizar estado
CREATE PROCEDURE proc_update_estado(
    IN p_id_estado INT,
    IN p_nombre_estado VARCHAR(50)
)
BEGIN
    UPDATE estados
    SET nombre_estado = p_nombre_estado
    WHERE id_estado = p_id_estado;
END$$

-- Eliminar estado
CREATE PROCEDURE proc_delete_estado(
    IN p_id_estado INT
)
BEGIN
    DELETE FROM estados
    WHERE id_estado = p_id_estado;
END$$

DELIMITER ;


-- para la tabla peliculas 
DELIMITER $$

-- Insertar película
CREATE PROCEDURE proc_insert_pelicula(
    IN p_titulo VARCHAR(100),
    IN p_id_categoria INT,
    IN p_id_estado INT,
    IN p_id_director INT,
    IN p_duracion INT,
    IN p_anio_estreno INT
)
BEGIN
    INSERT INTO peliculas(titulo, id_categoria, id_estado, id_director, duracion, anio_estreno)
    VALUES (p_titulo, p_id_categoria, p_id_estado, p_id_director, p_duracion, p_anio_estreno);
END$$

-- Actualizar película
CREATE PROCEDURE proc_update_pelicula(
    IN p_id_pelicula INT,
    IN p_titulo VARCHAR(100),
    IN p_id_categoria INT,
    IN p_id_estado INT,
    IN p_id_director INT,
    IN p_duracion INT,
    IN p_anio_estreno INT
)
BEGIN
    UPDATE peliculas
    SET titulo = p_titulo,
        id_categoria = p_id_categoria,
        id_estado = p_id_estado,
        id_director = p_id_director,
        duracion = p_duracion,
        anio_estreno = p_anio_estreno
    WHERE id_pelicula = p_id_pelicula;
END$$

-- Eliminar película
CREATE PROCEDURE proc_delete_pelicula(
    IN p_id_pelicula INT
)
BEGIN
    DELETE FROM peliculas
    WHERE id_pelicula = p_id_pelicula;
END$$

-- Consultar todas las películas
CREATE PROCEDURE proc_select_peliculas()
BEGIN
    SELECT * FROM peliculas;
END$$

-- Consultar película por ID
CREATE PROCEDURE proc_select_pelicula_por_id(
    IN p_id_pelicula INT
)
BEGIN
    SELECT * FROM peliculas
    WHERE id_pelicula = p_id_pelicula;
END$$

DELIMITER ;

-- para la tabla series
DELIMITER $$

-- Insertar serie
CREATE PROCEDURE proc_insert_serie(
    IN p_titulo VARCHAR(100),
    IN p_id_categoria INT,
    IN p_id_estado INT,
    IN p_id_director INT,
    IN p_anio_inicio INT,
    IN p_anio_fin INT
)
BEGIN
    INSERT INTO series(titulo, id_categoria, id_estado, id_director, anio_inicio, anio_fin)
    VALUES (p_titulo, p_id_categoria, p_id_estado, p_id_director, p_anio_inicio, p_anio_fin);
END$$

-- Actualizar serie
CREATE PROCEDURE proc_update_serie(
    IN p_id_serie INT,
    IN p_titulo VARCHAR(100),
    IN p_id_categoria INT,
    IN p_id_estado INT,
    IN p_id_director INT,
    IN p_anio_inicio INT,
    IN p_anio_fin INT
)
BEGIN
    UPDATE series
    SET titulo = p_titulo,
        id_categoria = p_id_categoria,
        id_estado = p_id_estado,
        id_director = p_id_director,
        anio_inicio = p_anio_inicio,
        anio_fin = p_anio_fin
    WHERE id_serie = p_id_serie;
END$$

-- Eliminar serie
CREATE PROCEDURE proc_delete_serie(
    IN p_id_serie INT
)
BEGIN
    DELETE FROM series
    WHERE id_serie = p_id_serie;
END$$

-- Consultar todas las series
CREATE PROCEDURE proc_select_series()
BEGIN
    SELECT * FROM series;
END$$

-- Consultar serie por ID
CREATE PROCEDURE proc_select_serie_por_id(
    IN p_id_serie INT
)
BEGIN
    SELECT * FROM series
    WHERE id_serie = p_id_serie;
END$$

DELIMITER ;

-- para la tabla actores

DELIMITER $$

-- Insertar actor
CREATE PROCEDURE proc_insert_actor(
    IN p_nombre_actor VARCHAR(100),
    IN p_nacionalidad VARCHAR(50)
)
BEGIN
    INSERT INTO actores(nombre_actor, nacionalidad)
    VALUES (p_nombre_actor, p_nacionalidad);
END$$

-- Actualizar actor
CREATE PROCEDURE proc_update_actor(
    IN p_id_actor INT,
    IN p_nombre_actor VARCHAR(100),
    IN p_nacionalidad VARCHAR(50)
)
BEGIN
    UPDATE actores
    SET nombre_actor = p_nombre_actor,
        nacionalidad = p_nacionalidad
    WHERE id_actor = p_id_actor;
END$$

-- Eliminar actor
CREATE PROCEDURE proc_delete_actor(
    IN p_id_actor INT
)
BEGIN
    DELETE FROM actores
    WHERE id_actor = p_id_actor;
END$$

-- Consultar todos los actores
CREATE PROCEDURE proc_select_actores()
BEGIN
    SELECT * FROM actores;
END$$

-- Consultar actor por ID
CREATE PROCEDURE proc_select_actor_por_id(
    IN p_id_actor INT
)
BEGIN
    SELECT * FROM actores
    WHERE id_actor = p_id_actor;
END$$

DELIMITER ;



-- ============================================================
-- DATOS DE EJEMPLO OPCIONALES
-- ============================================================

INSERT INTO estados (nombre_estado) VALUES 
('Disponible'), ('No disponible');

INSERT INTO categorias (nombre_categoria) VALUES 
('Acción'), ('Comedia'), ('Drama'), ('Terror');

INSERT INTO paises (nombre_pais) VALUES 
('Estados Unidos'), ('México'), ('España'), ('Colombia');

-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================
