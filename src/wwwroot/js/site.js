// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.


function buy(issue) {
    console.log('Buy ' + issue);
    var request = $.ajax({
        url: '/Issue/Buy?id=' + issue,
        type: "GET"
    });
    request.done(function (response, textStatus, jqXHR) {
        console.log('Buy ' + issue + ' response: ' + response);
        if (response == 'bought ' + issue) {
            disableRow(issue)
        }
    });

    request.fail(function (jqXHR, textStatus, errorThrown) {
        console.log('Buy ' + issue + ' error: ' + errorThrown);
    });    
}

function disableRow(issue) {
    strikeoutRow('r' + issue);
//    strikeoutRow('rg' + issue + ' collapsable-row');
    disableButton('bought' + issue);
//    disableButton('boughtG' + issue);
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

/*


function toggleSeries(series) {
    $('.r' + series).toggle();
}

$('#showFarOut').change(function () {
    $('.far-out').toggle();
});

$('#showPulled').change(function () {
    $('.pulled').toggle();
});

$('#showNonPulled').change(function () {
    $('.nonPulled').toggle();
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

$('#showUnreleased').change(function () {
    $('.unreleased').toggle();
});

$('#wantListOnly').change(function () {
    $('.owned').toggle();
});

*/