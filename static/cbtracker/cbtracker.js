function buy(issue){	
	url = '/comics/issue/' + issue + '/own'
	var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false );
    xmlHttp.send( null );
    response = xmlHttp.responseText;
    
    if (response == 'bought' + issue) {
    	disableRow(issue)
    }
}

function disableRow(issue) {
	rowID = 'r' + issue;
	row = document.getElementById(rowID);
	//row.style.backgroundColor = '#FFFFCC';
	row.style.setProperty("text-decoration", "line-through");
	buttonID = 'bought' + issue;
	button = document.getElementById(buttonID);
    button.disabled = true;
}

/*	
function buyIssue(issueID) {
	var deferred = $.Deferred();
	url = '/comics/issue/' + issue + '/own'
	XMLHttpRequest xhr = new XMLHttpRequest();
	xhr.open("GET",url,true);
	
	xhr.addEventListener('load',function(){
    	if(xhr.status === 200){
    		disableRow(issueID);
		    deferred.resolve(xhr.response);
    	}
    },false)
    
    xhr.send();
    return deferred.promise();	
}
*/
