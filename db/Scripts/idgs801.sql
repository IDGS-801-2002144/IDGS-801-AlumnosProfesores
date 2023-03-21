
DROP DATABASE IF EXISTS idgs800;
CREATE DATABASE IF NOT EXISTS idgs800;
use idgs800;
/*Alumnos----------------------------------------------*/

CREATE TABLE `students` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `created_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_student`(IN `name` VARCHAR(50), IN `surname` VARCHAR(50), IN `email` VARCHAR(50), IN `created_date` DATE)
     NO SQL
INSERT INTO students (name, surname, email, created_date) VALUES (name, surname, email, created_date);

CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_student`(IN `id_` INT(50))
     NO SQL
DELETE FROM students WHERE id = id_;

CREATE DEFINER=`root`@`localhost` PROCEDURE `search_all_students`()
     NO SQL
SELECT * FROM students;

CREATE DEFINER=`root`@`localhost` PROCEDURE `search_student`(IN `id_` INT(30))
     NO SQL
SELECT * FROM students WHERE id = id_;

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_student`(IN `id_` INT(50), IN `name` VARCHAR(50), IN `surname` VARCHAR(50), IN `email` VARCHAR(50))
     NO SQL
UPDATE students
SET name = name,
     surname = surname,
     email = email,
     created_date = created_date
WHERE id = id_;
/*-------------------------------------------------------------*/


/*----Profesores-----------------------------------------------*/

CREATE TABLE `teachers` (
   `id` int(11) NOT NULL AUTO_INCREMENT,
   `name` varchar(50) NOT NULL,
   `surname` varchar(50) NOT NULL,
   `email` varchar(50) NOT NULL,
   `created_date` date NOT NULL,
   PRIMARY KEY (`id`)
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_teacher`(IN `name` VARCHAR(50), IN `surname` VARCHAR(50), IN `email` VARCHAR(50), IN `created_date` DATE)
     NO SQL
INSERT INTO teachers (name, surname, email, created_date) VALUES (name, surname, email, created_date);

CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_teacher`(IN `id_` INT(50))
     NO SQL
DELETE FROM teachers WHERE id = id_;

CREATE DEFINER=`root`@`localhost` PROCEDURE `search_all_teachers`()
     NO SQL
SELECT * FROM teachers;

CREATE DEFINER=`root`@`localhost` PROCEDURE `search_teacher`(IN `id_` INT(30))
     NO SQL
SELECT * FROM teachers WHERE id = id_;

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_teacher`(IN `id_` INT(50), IN `name` VARCHAR(50), IN `surname` VARCHAR(50), IN `email` VARCHAR(50))
     NO SQL
UPDATE teachers
SET name = name,
     surname = surname,
     email = email,
     created_date = created_date
WHERE id =id_;


/*-------------------------------------------------------------*/