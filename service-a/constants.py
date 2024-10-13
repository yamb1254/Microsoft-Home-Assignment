
class Constants:
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bitcoin Price</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="card">
                        <div class="card-header text-center">
                            <h1>Bitcoin Price Tracker</h1>
                        </div>
                        <div class="card-body">
                            <h3 class="text-center">Current Bitcoin Price</h3>
                            <p class="text-center display-4">${{ current_price }}</p>
                            {% if avg_price %}
                                <h4 class="text-center">10-Minute Average Price</h4>
                                <p class="text-center display-4">${{ avg_price }}</p>
                            {% else %}
                                <p class="text-center">Not enough data for a 10-minute average yet.</p>
                            {% endif %}
                        </div>
                        <div class="card-footer text-center">
                            <small>Updated every minute</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """
    server_url="0.0.0.0"
    



Configurations = Constants()