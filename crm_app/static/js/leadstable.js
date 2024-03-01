$(document).ready(function() {
    // Make a GET request to your API endpoint
    $.ajax({
        url: 'http://127.0.0.1:8000/api/leads',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // Handle the successful response here
            console.log('Data received:', data);

            // Clear existing table rows
            $('#leadsTable tbody').empty();

            // Populate the table with the received data
            for (var i = 0; i < data.length; i++) {
                $('#leadsTable tbody').append('<tr>' +
                    '<td>' + data[i].id + '</td>' +
                    '<td>' + data[i].first_name + '</td>' +
                    '<td>' + data[i].last_name + '</td>' +
                    '<td>' + data[i].email + '</td>' +
                    '<td>' + data[i].phone + '</td>' +
                    '<td>' + data[i].status + '</td>' +
                    '</tr>');
            }
        },
        error: function(error) {
            // Handle any errors that occurred during the request
            console.error('Error:', error);
        }
    });
});
