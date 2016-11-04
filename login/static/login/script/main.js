// --- Set up CSRF token, which is needed for django form submissions. ---
var csrftoken = $.cookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

add_rows();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}


$('#addBtn').on('click', function(e){

    var content = $.find('#content')[0];

    var content_text = $(content).val();

    $(content).val("");

    $.post('add_citation/', {'content': content_text}, function(data){
        location.reload();
    });
});

function add_rows(){

    var table_body = $.find('#table_body')[0];

    $.each(citations, function(index, citation){

        var table_row = table_body.insertRow(-1);


        //ID Cell
        var table_cell = table_row.insertCell(-1);

        var table_cell_text = document.createTextNode(citation.id);

        table_cell.appendChild(table_cell_text);


        //Content Cell
        table_cell = table_row.insertCell(-1);

        table_cell_text = document.createTextNode(citation.content);

        table_cell.appendChild(table_cell_text);


        //Delete Button
        table_cell = table_row.insertCell(-1);

        var delete_button = document.createElement('button');

        delete_button.className += 'btn btn-danger'

        delete_button.innerHTML = 'Delete'

        $(delete_button).on('click', function(e){

            $.post('delete_citation/', {'id': citation.id, 'content': citation.content}, function(data){
                    location.reload();
                });
            });

        table_cell.appendChild(delete_button);
    });

}

