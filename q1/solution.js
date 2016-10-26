(function(){
	var start = '20160104173643'; 
	var end = '20160521101256';	

	calculateTimeDifference(start, end); 

	function buildTimeDiffOutput(diff) {
	  	total_ms = diff;
	    total_seconds = total_ms / 1000;
	    total_minutes = total_seconds / 60; 
	    total_hours = total_minutes / 60; 
	    total_days = total_hours / 24;
	    var output = total_days + ' Days ' + total_hours + ' Hours ' + total_minutes + ' Minutes ' + total_seconds; 
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
