from flask import render_template_string
from constants import Configurations


def hello_utili():
    """Generates and returns the HTML page displaying Hello Microsoft!."""
    html = Configurations.html
    return render_template_string(html)