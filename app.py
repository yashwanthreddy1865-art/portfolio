from flask import Flask, render_template
from data import projects, work_experiences

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", projects=projects, work_experiences=work_experiences)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project:
        return render_template("project_detail.html", project=project)
    else:
        return "Project not found", 404

if __name__ == '__main__':
    app.run(debug=True)
