function buy(issue){	
	url = '/cbtracker/issue/' + issue + '/own'
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
	row.style.setProperty("text-decoration", "line-through");
	buttonID = 'bought' + issue;
	button = document.getElementById(buttonID);
    button.disabled = true;
}

$('input[type = checkbox]').change(function () {
    $('.far-out').toggle(self.checked);
});