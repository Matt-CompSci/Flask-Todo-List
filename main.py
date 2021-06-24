import flask
from models.task_dataset import TaskDataset

# Create flask application with name "Flask API"
app = flask.Flask("Flask API", template_folder="views")


@app.route("/todo")
def todo():
    import models.task_dataset as task_dataset
    task_dataset = TaskDataset()
    tasks = task_dataset.get_tasks()
    return flask.render_template("todo.html", tasks=tasks)


@app.route("/add_task", methods=["post"])
def add_task():
    from models.task_dataset import TaskDataset
    description = flask.request.form.get("description")
    task_dataset = TaskDataset()
    task_dataset.add_task(description, False)
    return flask.redirect("todo")


# Launch application default Port 5000
app.run()
