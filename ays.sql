-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-12-2022 a las 00:34:26
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ays`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aulas`
--

CREATE TABLE `aulas` (
  `codigo` int(11) NOT NULL,
  `numero` int(3) NOT NULL,
  `bloque` varchar(1) NOT NULL,
  `descripcion` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `aulas`
--

INSERT INTO `aulas` (`codigo`, `numero`, `bloque`, `descripcion`) VALUES
(1, 205, 'M', 'Laboratorio de Física'),
(2, 405, 'K', 'Sala de computadores'),
(3, 211, 'N', 'Aula de clase');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventos`
--

CREATE TABLE `eventos` (
  `codigo` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `duracion` int(2) NOT NULL,
  `objetivo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `eventos`
--

INSERT INTO `eventos` (`codigo`, `fecha`, `duracion`, `objetivo`) VALUES
(1, '2022-11-17', 2, 'Competencia de matemáticas básicas'),
(2, '2023-01-18', 4, 'Exposición de proyectos de mecatrónica'),
(3, '2023-04-11', 3, 'Bootcamp de programación orientada a dispositivos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupos`
--

CREATE TABLE `grupos` (
  `codigo` int(11) NOT NULL,
  `numero_grupo` int(3) NOT NULL,
  `cantidad_estudiantes` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `grupos`
--

INSERT INTO `grupos` (`codigo`, `numero_grupo`, `cantidad_estudiantes`) VALUES
(1, 25, 32),
(2, 42, 26),
(3, 102, 39);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horarios`
--

CREATE TABLE `horarios` (
  `codigo` int(11) NOT NULL,
  `codigo_aula` int(3) NOT NULL,
  `codigo_materia` int(11) NOT NULL,
  `cedula_maestro` int(11) NOT NULL,
  `codigo_grupo` int(11) NOT NULL,
  `dias` varchar(255) NOT NULL,
  `hora` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `horarios`
--

INSERT INTO `horarios` (`codigo`, `codigo_aula`, `codigo_materia`, `cedula_maestro`, `codigo_grupo`, `dias`, `hora`) VALUES
(1, 2, 1, 1000632525, 1, 'Lunes, Miercoles y Viernes', '10:00'),
(2, 2, 2, 1000589632, 2, 'Martes y Jueves', '16:00'),
(3, 3, 3, 1000698754, 3, 'Miercoles y Viernes', '08:00'),
(10, 1, 3, 1000698754, 1, 'Lunes y Miercoles', '06:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripciones`
--

CREATE TABLE `inscripciones` (
  `codigo` int(11) NOT NULL,
  `codigo_grupo` int(11) NOT NULL,
  `codigo_evento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `inscripciones`
--

INSERT INTO `inscripciones` (`codigo`, `codigo_grupo`, `codigo_evento`) VALUES
(1, 3, 2),
(2, 2, 3),
(3, 1, 1),
(7, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maestros`
--

CREATE TABLE `maestros` (
  `cedula` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `telefono` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `maestros`
--

INSERT INTO `maestros` (`cedula`, `nombre`, `apellido`, `correo`, `telefono`) VALUES
(1000589632, 'Naomi', 'Montoya', 'naomi.montoya@yopmail.com', '3114859865'),
(1000632525, 'Sara', 'Zapata', 'sara.zapata@yopmail.com', '3124589658'),
(1000698754, 'Jose', 'Martinez', 'jose.martinez@yopmail.com', '3186957470');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `duracion` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`codigo`, `nombre`, `duracion`) VALUES
(1, 'Lógica de Programación', 6),
(2, 'Estructuras de Datos', 4),
(3, 'Física de Campos', 4);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `aulas`
--
ALTER TABLE `aulas`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `eventos`
--
ALTER TABLE `eventos`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `cedula_maestro` (`cedula_maestro`),
  ADD KEY `codigo_aula` (`codigo_aula`),
  ADD KEY `codigo_grupo` (`codigo_grupo`),
  ADD KEY `codigo_materia` (`codigo_materia`);

--
-- Indices de la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `codigo_grupo` (`codigo_grupo`),
  ADD KEY `codigo_evento` (`codigo_evento`);

--
-- Indices de la tabla `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`cedula`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`codigo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `aulas`
--
ALTER TABLE `aulas`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `eventos`
--
ALTER TABLE `eventos`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `grupos`
--
ALTER TABLE `grupos`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `horarios`
--
ALTER TABLE `horarios`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD CONSTRAINT `horarios_ibfk_1` FOREIGN KEY (`cedula_maestro`) REFERENCES `maestros` (`cedula`),
  ADD CONSTRAINT `horarios_ibfk_2` FOREIGN KEY (`codigo_aula`) REFERENCES `aulas` (`codigo`),
  ADD CONSTRAINT `horarios_ibfk_3` FOREIGN KEY (`codigo_grupo`) REFERENCES `grupos` (`codigo`),
  ADD CONSTRAINT `horarios_ibfk_4` FOREIGN KEY (`codigo_materia`) REFERENCES `materias` (`codigo`);

--
-- Filtros para la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `inscripciones_ibfk_1` FOREIGN KEY (`codigo_grupo`) REFERENCES `grupos` (`codigo`),
  ADD CONSTRAINT `inscripciones_ibfk_2` FOREIGN KEY (`codigo_evento`) REFERENCES `eventos` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
