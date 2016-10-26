<?php

function buildDateTime($str){
	$year = substr($str, 0, 4);
	$month = substr($str, 4, 2);
	$day = substr($str, 6, 2);
	$hour = substr($str, 8, 2);
	$minute = substr($str, 10, 2);
	$second = substr($str, 12, 2);
	$output = mktime($hour, $minute, $second, $month, $day, $year);

	return new DateTime(date("Y-m-d H:i:s", $output));
}

function timeDiff($start,$end)
{
	$start=buildDateTime($start);
	$end=buildDateTime($end);
	$timeDiff=$start->diff($end);
	echo $timeDiff->format('%a Days %H Hours %I Minutes %S Seconds');
	return $timeDiff;
}

$difference = timeDiff("20160104173643","20160521101256");