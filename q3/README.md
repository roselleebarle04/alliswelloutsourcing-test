# Questions 3:
 
Please create a simple REST API using each of the following language: :  Python 3.5,  PHP 5.3.
 
List of methods is displayed below:
 
URL                           HTTP Method  Operation
/api/orders                  GET      	Returns an array of orders
/api/orders/:id             GET      	Returns the order with id of :id
/api/orders                 POST     	Adds a new order and return it with an id attribute added
/api/orders/:id             PUT      	Updates the order with id of :id
 
Detail about DB:
 
Table Name: tbOrders
DB Name:  OMDB
DB Engine:  MySQL 5.0
DB Username :   OMADMIN
DB Password: test
 
 
Table structure:
 
CREATE TABLE tbOrders (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
OrderRef VARCHAR(30) NOT NULL,
CustomerCode VARCHAR(30) NOT NULL,
OrderDate TIMESTAMP,
OrderType SMALLINT
)