from os import O_NDELAY, O_RDONLY
from flask import Flask, json, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Walkabout Creek',
    'salary': '$50,000'
}, {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Wolfe Creek',
    'salary': '$4,000,000'
}, {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Dunedoo',
    'salary': '$45,000'
}, {
    'id': 4,
    'title': 'Business Analyst',
    'location': 'Timbuktu ',
    'salary': '$90,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Bodacious')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
