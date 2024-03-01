$(document).ready(function() {
    // Initialize DataTable
    var table = $('#example').DataTable({
        "ajax": {
            "url": "http://127.0.0.1:8000/api/products",
            "type": "GET",
            "dataSrc": ""
        },
        "columns": [
            { "data": "name" },
            { "data": "price" },
            {
                "data": null,
                "defaultContent": '<button class="btn btn-primary btn-sm edit-btn">Edit</button>'
            }
        ]
    });

    // Handle inline editing
    $('#example tbody').on('click', '.edit-btn', function () {
        var data = table.row($(this).parents('tr')).data();
        var newData = {}; // New data to be updated

        // Example: Prompt for name and price updates
        newData.name = prompt('Enter new name:', data.name);
        newData.price = prompt('Enter new price:', data.price);

        if (newData.name && newData.price) {
            // Perform PUT request to update the data
            $.ajax({
                url: 'http://127.0.0.1:8000/api/products/' + data.id,
                type: 'PUT',
                contentType: 'application/json',
                data: JSON.stringify(newData),
                success: function (response) {
                    // Assuming your server returns the updated data
                    table.ajax.reload(null, false);
                },
                error: function (xhr, status, error) {
                    console.error('Error updating data:', error);
                }
            });
        }
    });
});