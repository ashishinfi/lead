$(document).ready(function() {
    // Make a GET request to your API endpoint
    $.ajax({
        url: 'http://127.0.0.1:8000/api/sales',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // Handle the successful response here
            console.log('Data received:', data);

            // Clear existing table rows
            $('#salesTable tbody').empty();

            // Populate the table with the received data
            for (var i = 0; i < data.length; i++) {
                $('#salesTable tbody').append('<tr>' +
                    '<td>' + data[i].id + '</td>' +
                    '<td>' + data[i].quantity + '</td>' +
                    '<td>' + data[i].total_amount + '</td>' +
                    '<td>' + data[i].sale_date + '</td>' +
                    '<td>' + data[i].customer + '</td>' +
                    '<td>' + data[i].product + '</td>' +
                    '</tr>');
            }
        },
        error: function(error) {
            // Handle any errors that occurred during the request
            console.error('Error:', error);
        }
    });
});
