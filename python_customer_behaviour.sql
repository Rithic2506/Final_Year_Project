-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 08, 2022 at 03:42 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_customer_behaviour`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee_details`
--

CREATE TABLE `employee_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee_details`
--

INSERT INTO `employee_details` (`id`, `name`, `contact`, `email`, `address`, `username`, `password`, `status`, `report`) VALUES
(1, 'sham', '9876543210', 'sham@gmail.com', 'trichy', 'sham', '123', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `manager_details`
--

CREATE TABLE `manager_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `manager_details`
--

INSERT INTO `manager_details` (`id`, `name`, `contact`, `email`, `address`, `username`, `password`, `status`, `report`) VALUES
(1, 'arun', '9875643120', 'arun@gmail.com', 'trichy', 'arun', '123', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `sales_details`
--

CREATE TABLE `sales_details` (
  `id` int(100) NOT NULL,
  `employee` varchar(100) NOT NULL,
  `invoice_no` varchar(100) NOT NULL,
  `customer_id` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales_details`
--

INSERT INTO `sales_details` (`id`, `employee`, `invoice_no`, `customer_id`, `contact`, `product`, `price`, `quantity`, `total`, `status`, `report`) VALUES
(1, 'sham', '1', '343', '9786453212', 'pen', '25', '2', '50', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `search_details`
--

CREATE TABLE `search_details` (
  `Member_number` varchar(100) NOT NULL,
  `itemDescription` varchar(100) NOT NULL,
  `Quantity` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `search_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `search_result`
--

CREATE TABLE `search_result` (
  `product` varchar(100) NOT NULL,
  `count` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `search_result`
--

INSERT INTO `search_result` (`product`, `count`) VALUES
('tropical fruit', 0),
('whole milk', 0),
('pip fruit', 0),
('other vegetables', 0),
('rolls/buns', 0),
('pot plants', 0),
('citrus fruit', 0),
('beef', 0),
('frankfurter', 0),
('chicken', 0),
('butter', 0),
('fruit/vegetable juice', 0),
('packaged fruit/vegetables', 0),
('chocolate', 0),
('specialty bar', 0),
('butter milk', 0),
('bottled water', 0),
('yogurt', 0),
('sausage', 0),
('brown bread', 0),
('hamburger meat', 0),
('root vegetables', 0),
('pork', 0),
('pastry', 0),
('canned beer', 0);

-- --------------------------------------------------------

--
-- Table structure for table `search_result1`
--

CREATE TABLE `search_result1` (
  `Member_number` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `search_result1`
--

INSERT INTO `search_result1` (`Member_number`, `product`) VALUES
('1808', 'tropical fruit,rolls/buns,'),
('2552', 'whole milk,canned beer,'),
('2300', 'pip fruit,canned beer,'),
('1187', 'other vegetables,frankfurter,'),
('3037', 'whole milk,other vegetables,'),
('4941', 'rolls/buns,whole milk,'),
('4501', 'other vegetables,whole milk,'),
('3803', 'pot plants,citrus fruit,'),
('2762', 'whole milk,frankfurter,decalcifier,'),
('4119', 'tropical fruit,frankfurter,'),
('1340', 'citrus fruit,butter milk,'),
('2193', 'beef,hamburger meat,root vegetables,'),
('1997', 'frankfurter,pasta,'),
('4546', 'chicken,other vegetables,'),
('4736', 'butter,sausage,'),
('1959', 'fruit/vegetable juice,rolls/buns,citrus fruit,'),
('1974', 'packaged fruit/vegetables,grapes,'),
('2421', 'chocolate,root vegetables,'),
('1513', 'specialty bar,'),
('1905', 'other vegetables,fruit/vegetable juice,sugar,'),
('2810', 'butter milk,frankfurter,sausage,'),
('2867', 'whole milk,chicken,'),
('3962', 'tropical fruit,sausage,'),
('1088', 'tropical fruit,'),
('4976', 'bottled water,'),
('4056', 'yogurt,'),
('3611', 'sausage,'),
('1420', 'other vegetables,'),
('4286', 'brown bread,'),
('4918', 'yogurt,'),
('4783', 'hamburger meat,'),
('3709', 'root vegetables,'),
('4289', 'pork,'),
('1559', 'beef,'),
('2900', 'pastry,'),
('3527', 'canned beer,'),
('1495', 'root vegetables,'),
('3558', 'citrus fruit,'),
('3128', 'sausage,'),
('1863', 'tropical fruit,'),
('3841', 'berries,frankfurter,'),
('3903', 'canned beer,'),
('2658', 'butter milk,'),
('4272', 'coffee,'),
('1120', 'pastry,meat,'),
('2676', 'rolls/buns,'),
('1697', 'misc. beverages,'),
('2507', 'root vegetables,canned beer,'),
('4620', 'sausage,'),
('3365', 'canned beer,'),
('2978', 'ham,');
