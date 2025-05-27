-- Crear la base de datos
CREATE DATABASE estudiantes_db;

-- Conectarse a la base de datos (esto varía según la herramienta que uses)
-- En psql: \c estudiantes_db

-- Crear la tabla estudiantes
CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    apellido VARCHAR(100),
    nombre VARCHAR(100),
    edad INT,
    numero_carne VARCHAR(20),
    correo VARCHAR(100)
);

-- Insertar datos en la tabla
INSERT INTO estudiantes (apellido, nombre, edad, numero_carne, correo)
VALUES
('Meléndez Avilés', 'Yassir Mauricio', 20, 'MA243080', 'yassirmelendezaaviles14@gmail.com'),
('Chévez Zepeda', 'Cesar Daniel', 19, 'CZ230902', 'cesarchevez37@gmail.com'),
('Hernández Acevedo', 'Anderson Daniel', 20, 'HA240610', 'anderhdz06@gmail.com'),
('Rodríguez Sánchez', 'Justin Alfredo', 21, 'RS240130', 'justinalfredo0477@gmail.com');
