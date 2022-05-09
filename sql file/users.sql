-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2022 at 06:53 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `educative`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Id` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Dept` varchar(20) NOT NULL,
  `Age` int(11) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Role` int(11) NOT NULL,
  `account_status` int(11) NOT NULL,
  `State` varchar(200) NOT NULL,
  `Country` varchar(20) NOT NULL,
  `Zipcode` varchar(20) NOT NULL,
  `Class` int(11) NOT NULL,
  `RegisterNum` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Id`, `Name`, `Dept`, `Age`, `Password`, `email`, `phone`, `Address`, `Role`, `account_status`, `State`, `Country`, `Zipcode`, `Class`, `RegisterNum`) VALUES
(1, 'Alan Mathew', 'BCA', 18, 'Alan123', 'Alan@gmail.com', '1234567890', '', 2, 2, '', '', '', 1, '19UBC129'),
(5, 'Amal Eapan', 'BCA', 20, '123456789', 'Eapan123@gmail.com', '+919656247861', 'Thakadiyel house, Palampra P.O', 1, 1, 'Kerala', 'India', '686518', 1, '19UBC104'),
(6, 'Admin', '', 30, 'Admin123', 'Admin@educative.in', '1234567890', '', 0, 2, '', '', '', 0, '0'),
(7, 'Alan Dileep', 'BCA', 21, 'Alan123', 'Alan123', '', 'Edward\'s snow den', 2, 2, 'Kerala', 'India', '686518', 1, '19UBC102'),
(9, 'Indrajith Vinod Nair', 'BCA', 18, '123', 'indrajithvinod16@gmail.com', '+919656247861', 'Thakadiyel house, Palampra P.O', 2, 0, 'Kerala', 'India', '686518', 1, '19UBC105'),
(10, 'Aleena Paul', 'BCA', 0, 'Aleena123', 'indrajithvinod16@gmail.com', '+919656247861', 'Valooran House', 2, 0, 'Kerala', 'India', '686518', 1, '19UBC103'),
(11, 'Akhil Mathew', 'BCA', 0, 'Akhil123', 'Akhilmathew@gmail.com', '+919656247861', 'Padakootil house, Palampra P.O', 1, 2, 'Kerala', 'India', '686518', 1, 'MCK104'),
(15, 'Akhil Soman', 'BCA', 20, 'AkhilSoman', 'AkhilSoman@gmail.com', '3473294739473', 'Kerala', 2, 2, 'Kerala', 'India', '123232', 1, '19UBC108'),
(16, 'Indrajith V Nair', 'BCA', 20, 'Indrajith123', 'indrajithvinod16@gmail.com', '+919656247861', 'Thakadiyel house, Palampra P.O', 2, 2, 'Kerala', 'India', '686518', 1, '19UBC126');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
