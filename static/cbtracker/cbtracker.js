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
	strikeoutRow('r' + issue);
	strikeoutRow('rg' + issue + ' collapsable-row');
	disableButton('bought' + issue);
	disableButton('boughtG' + issue);
}

function strikeoutRow(rowID) {
	row = document.getElementById(rowID);
	if (row != null) {
		row.style.setProperty("text-decoration", "line-through");
	}
}

function disableButton(buttonID) {
	button = document.getElementById(buttonID);
	if (button != null) {
	    button.disabled = true;
	}
}


function toggleSeries(series) {
	$('.r' + series).toggle();
}

$('#showFarOut').change(function () {
    $('.far-out').toggle();
});

$('.collapser').click(function () {
    $('.row-' + this.id).toggle();
});

$('#show-series-year').change(function () {
    $('.series-name').toggle();
});

$('#show-target-price').change(function () {
    $('.target-price').toggle();
});

$('#group-by-series').change(function () {
    $('.back-issue-table').toggle();
});


