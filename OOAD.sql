-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: TEST1
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
-- Table structure for table `Lichhen`
--

DROP TABLE IF EXISTS `Lichhen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Lichhen` (
  `Doctor` varchar(45) DEFAULT NULL,
  `Patient` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Lichhen`
--

LOCK TABLES `Lichhen` WRITE;
/*!40000 ALTER TABLE `Lichhen` DISABLE KEYS */;
INSERT INTO `Lichhen` VALUES ('Nguyễn Minh Quân','pa','NCF','2024-01-07','12:00:00'),('Minh Hải','Đoàn Quang Lưu','CF','2024-01-07','12:00:00'),('Nguyễn Minh Quân','pa','NCF','2024-01-01','00:00:00'),('Nguyễn Minh Quân','pa','CF','2024-01-07','00:00:00'),('Nguyễn Minh Quân','pa','NCF','2024-01-07','06:07:00'),('Minh Hải','pa','NCF','2024-01-14','07:10:00'),('Nguyễn Minh Quân','pa','CF','2024-01-07','00:00:00'),('Nguyễn Minh Quân','pa','NCF','2024-01-01','00:00:00'),('Nguyễn Minh Quân','pa','CF','2024-01-25','00:00:00'),('Nguyễn Minh Quân','pa','NCF','2024-01-06','00:00:00'),('Nguyễn Minh Quân','Đoàn Quang Lưu','CF','2024-01-02','14:00:00'),('Nguyễn Minh Quân','Đoàn Quang Lưu','CF','2024-01-06','14:28:00');
/*!40000 ALTER TABLE `Lichhen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `Name` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `Usercol` varchar(45) NOT NULL,
  `Id` varchar(45) DEFAULT NULL,
  `Firstname` varchar(45) DEFAULT NULL,
  `Lastname` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `DoB` varchar(45) DEFAULT NULL,
  `Age` varchar(45) DEFAULT NULL,
  `Sex` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('Nguyễn Minh Quân','abc','Doctor','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Đoàn Quang Lưu','def','Patient','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Lê Quang Huy','bcd','Doctor','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('pa','pa','Patient','4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('do','do','Doctor','5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dichVu`
--

DROP TABLE IF EXISTS `dichVu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dichVu` (
  `Ten` varchar(45) DEFAULT NULL,
  `Gia` int DEFAULT NULL,
  `moTa` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dichVu`
--

LOCK TABLES `dichVu` WRITE;
/*!40000 ALTER TABLE `dichVu` DISABLE KEYS */;
INSERT INTO `dichVu` VALUES ('Nho rang',100,'Nho rang rat dau'),('Trong rang',200,'Trong rang rat suong');
/*!40000 ALTER TABLE `dichVu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-01 21:31:22
