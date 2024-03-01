$(document).ready(function() {
    // Make a GET request to your API endpoint
    $.ajax({
        url: 'http://127.0.0.1:8000/api/contacts',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // Handle the successful response here
            console.log('Data received:', data);

            // Clear existing table rows
            $('#studentTable tbody').empty();

            // Populate the table with the received data
            for (var i = 0; i < data.length; i++) {
                $('#studentTable tbody').append('<tr>' +
                    '<td>' + data[i].id + '</td>' +
                    '<td>' + data[i].Email + '</td>' +
                    '<td>' + data[i].Mobile_Number + '</td>' +
                    '<td>' + data[i].Website_Url + '</td>' +
                    '<td>' + data[i].Page_Url + '</td>' +
                    '<td>' + data[i].Date + '</td>' +
                    '<td>' + data[i].Time + '</td>' +
                    '<td>' + data[i].Lead_ID + '</td>' +
                    '<td>' + data[i].Referral_information_field + '</td>' +
                    '<td>' + data[i].Visitor_came_from + '</td>' +
                    '<td>' + data[i].utm_source + '</td>' +
                    '<td>' + data[i].utm_medium + '</td>' +
                    '<td>' + data[i].utm_campaign + '</td>' +
                    '<td>' + data[i].Last_visited_pages + '</td>' +
                   
                    '</tr>');
            }
        },
        error: function(error) {
            // Handle any errors that occurred during the request
            console.error('Error:', error);
        }
    });
});
