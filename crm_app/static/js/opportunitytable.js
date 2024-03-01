$(document).ready(function() {
    // Make a GET request to your API endpoint
    $.ajax({
        url: 'http://127.0.0.1:8000/api/opportunities',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // Handle the successful response here
            console.log('Data received:', data);

            // Clear existing table rows
            $('#opportunityTable tbody').empty();

            // Populate the table with the received data
            for (var i = 0; i < data.length; i++) {
                $('#opportunityTable tbody').append('<tr>' +
                    '<td>' + data[i].id + '</td>' +
                    '<td>' + data[i].amount + '</td>' +
                    '<td>' + data[i].stage + '</td>' +
                    '<td>' + data[i].close_date + '</td>' +
                    '<td>' + data[i].customer + '</td>' +
                    // '<td>' + data[i].product + '</td>' +
                    '</tr>');
            }
        },
        error: function(error) {
            // Handle any errors that occurred during the request
            console.error('Error:', error);
        }
    });
});
