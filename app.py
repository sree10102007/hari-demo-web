from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS=[
    {"job_id":1,
    "title":"Data Analyst",
    "location":"Bengaluru, India",
    "salary":"Rs.10,00,000"},
    {"job_id":2,
    "title":"Data Scientist",
    "location":"Delhi, India",
    "salary":"Rs.15,00,000"},
    {"job_id":3,
    "title":"frontend engineer",
    "location":"remote", 
    "salary":""},
    {"job_id":4,
    "title":"backend engineer",
    "location":"san francisco,usa", 
    "salary":"Rs.15,00,000"}
     
]

@app.route("/")
def hello_world():
    return render_template("index.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
