(function(){
	var start = '20160104173643'; 
	var end = '20160521101256';	

	calculateTimeDifference(start, end); 

	function buildTimeDiffOutput(diff) {
		var days, hours, minutes, seconds, milliseconds, output;
		diff=(diff-(milliseconds=diff%1000))/1000;
		diff=(diff-(seconds=diff%60))/60;
		diff=(diff-(minutes=diff%60))/60;
		days=(diff-(hours=diff%24))/24;

		output = days + ' Days ' + hours + ' Hours ' + minutes + ' Minutes ' + seconds + ' Seconds';
		console.log(output);
	    return output
	}

	function formateDateTimeString(str){
	  var pattern = /(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})/i;
	  output = pattern.exec(str);
	  return new Date(output[1], output[2], output[3], output[4], output[5], output[6]);
	}	

	function calculateTimeDifference(start, end) {
		var diff =  formateDateTimeString(end) - formateDateTimeString(start);
	 	return buildTimeDiffOutput(diff)
	}

})();
