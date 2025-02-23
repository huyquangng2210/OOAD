-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: OOAD
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `AppointmentId` int NOT NULL,
  `Date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `doctor` varchar(255) DEFAULT NULL,
  `patient` varchar(255) DEFAULT NULL,
  `BilldetailId` int DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `AppointmentId` (`AppointmentId`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`AppointmentId`) REFERENCES `appointment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (2,5,'2000-01-01','00:00:00','b','a',9,'NCF'),(3,5,'2000-01-01','00:00:00','b','a',9,'NCF'),(4,5,'2000-01-01','00:00:00','b','a',9,'NCF'),(5,5,'2024-12-16','00:00:00','b','a',9,'NCF'),(6,5,'2024-12-16','00:00:00','b','a',9,'NCF'),(8,5,'2000-01-01','00:00:00','b','a',6,NULL),(9,5,'2000-01-01','00:00:00','b','a',16,'NCF'),(10,5,'2000-01-01','00:00:00','b','a',17,'NCF'),(11,15,'2024-02-04','16:00:00','Nguyễn Minh Quân','pa',18,'NCF'),(18,24,'2000-02-02','17:00:00','Đoàn Quang Lưu','a',25,'NCF'),(19,24,'2024-02-02','06:00:00','Đoàn Quang Lưu','a',26,'NCF'),(20,28,'2024-02-02','19:00:00','Nguyễn Minh Quân','Nguyễn Bá Trung Hiếu',27,'NCF');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-02 21:26:38
