# PHP Version

## Starting the API (Using built in web server)

````
php -S localhost:8888 index.php

# Now go to http://localhost:8888/orders to list all orders
````

## Prerequisites
1. Database - the database used in config is mysql, for easy setup, i have backed up the test database i made, which you can easily import in your phpmyadmin gui or mysql database (test.sql) In original OCDB-test.db file, there is no Orders table so i had to create them myself. :( 

2. You can use curl or postman clients to test update and delete :)

## Resources
(https://github.com/mevdschee/php-crud-api) A really lightweight php script that allows us to build a simple api. 
