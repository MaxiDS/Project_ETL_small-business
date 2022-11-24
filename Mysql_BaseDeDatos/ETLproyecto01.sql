#DROP DATABASE `ETL_proyecto1`;
CREATE DATABASE  IF NOT EXISTS `ETL_proyecto1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ETL_proyecto1`;

-- MAESTROS DE LOS ARCHIVOS CARGADOS

 -- Table structure for table `listaprecio`

DROP TABLE IF EXISTS producto;

CREATE TABLE producto (
	producto_id varchar(30) NOT NULL PRIMARY KEY,
	marca varchar(50) NOT NULL,
	nombre varchar(120) NOT NULL,
	presentacion varchar(20) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
 
 DROP TABLE IF EXISTS `sucursal`;

CREATE TABLE sucursal (
  sucursal_id varchar(15) NOT NULL PRIMARY KEY,
  comercioId varchar(5) NOT NULL,
  banderaId varchar(5) NOT NULL,
  banderaDescripcion varchar(60),
  comercioRazonSocial varchar(100),
  Provincia varchar(20) ,
  Localidad VARCHAR(40) ,
  Direccion VARCHAR(90) ,
  lat   VARCHAR(20) ,
  lng  VARCHAR(20) ,
  sucursalNombre  VARCHAR(80) ,
  sucursalTipo   VARCHAR(30) NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
 
 -- Table structure for table `listaprecio`
DROP TABLE IF EXISTS listaprecio;

CREATE TABLE listaprecio (
	precio decimal(20.5),
	producto_id varchar(30) NOT NULL,
	sucursal_id varchar(15) NOT NULL,
	date date NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- TABLAS ADICIONALES PARA VALIDACION
-- Deberiamos colocar tabla calendario


DROP TABLE IF EXISTS `auditoriacarga`;

CREATE TABLE auditoriacarga (
  UltFechaMod INT NOT NULL);
  

ALTER TABLE listaprecio ADD FOREIGN KEY (producto_id) REFERENCES producto(producto_id);
  

  
  
  
