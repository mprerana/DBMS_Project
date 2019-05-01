-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 03, 2019 at 10:28 PM
-- Server version: 5.7.24
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ewalletdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `bankdetails`
--

DROP TABLE IF EXISTS `bankdetails`;
CREATE TABLE IF NOT EXISTS `bankdetails` (
  `UserId` int(12) NOT NULL,
  `BankName` varchar(20) NOT NULL,
  `AccountNo` varchar(30) NOT NULL,
  `IFSC` varchar(10) NOT NULL,
  `BranchName` varchar(50) NOT NULL,
  KEY `UserId` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `kycinfo`
--

DROP TABLE IF EXISTS `kycinfo`;
CREATE TABLE IF NOT EXISTS `kycinfo` (
  `UserId` int(11) NOT NULL,
  `KYC_request_Date` date NOT NULL,
  `KYC_request_Time` time NOT NULL,
  `KYC_Status` varchar(10) NOT NULL DEFAULT 'Not Done',
  KEY `FKUserId` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `useraccountstatus`
--

DROP TABLE IF EXISTS `useraccountstatus`;
CREATE TABLE IF NOT EXISTS `useraccountstatus` (
  `UserId` int(12) NOT NULL,
  `AccountStatus` varchar(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

DROP TABLE IF EXISTS `userdetails`;
CREATE TABLE IF NOT EXISTS `userdetails` (
  `UserId` int(12) NOT NULL,
  `UserName` varchar(50) NOT NULL,
  `EmailId` varchar(50) NOT NULL,
  `PhoneNo` varchar(10) NOT NULL,
  `PrimaryAddress` longtext NOT NULL,
  `SecondaryAddress` longtext,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `UserName` (`UserName`),
  UNIQUE KEY `EmailId` (`EmailId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bankdetails`
--
ALTER TABLE `bankdetails`
  ADD CONSTRAINT `bankdetails_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `userdetails` (`UserId`);

--
-- Constraints for table `kycinfo`
--
ALTER TABLE `kycinfo`
  ADD CONSTRAINT `FKUserId` FOREIGN KEY (`UserId`) REFERENCES `userdetails` (`UserId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
