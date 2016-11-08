<?php 
include 'api.php';

$api = new PHP_CRUD_API(array(
	'dbengine'=>'MySQL',
	'hostname'=>'localhost',
	'username'=>'test',
	'password'=>'',
	'database'=>'test',
	'charset'=>'utf8'
));

$api->executeCommand();
 ?>