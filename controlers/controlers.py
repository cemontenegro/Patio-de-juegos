from __main__ import app
from email.policy import default
from flask import render_template


@app.route('/play', defaults={'numero': 3, 'color': '#9fc5f8'})
@app.route('/play/<int:numero>', defaults={'color': '#9fc5f8'})
@app.route('/play/<int:numero>/<color>')
def plantilla(numero=3, color="blue"):
	return render_template("index.html", num=numero, color=color)
