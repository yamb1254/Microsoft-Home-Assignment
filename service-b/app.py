from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello Microsoft!</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="jumbotron text-center">
                        <h1 class="display-4">Hello Microsoft!</h1>
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
    return render_template_string(html)

# Health check endpoint
@app.route('/healthz', methods=['GET'])
def health_check():
    return "OK", 200

# Readiness check endpoint
@app.route('/readyz', methods=['GET'])
def readiness_check():
    return "Ready", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
