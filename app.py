from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Russia, Moscow',
    'salary': 'Rub. 20,000'
  },
  {
    'id': 2,
    'title': 'Data Composer',
    'location': 'Russia, Ufa',
    'salary': 'Rub. 30,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'India',
    'salary': 'Rub. 24,000'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS, 
                         company_name='Kote')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)