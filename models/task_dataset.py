from models.database import Database
from models.task import Task


class TaskDataset:
    def __init__(self):
        self.database = Database(":memory:")
        self.database.query("CREATE TABLE IF NOT EXISTS tasks(description varchar(128), completed number(1))")

    def get_tasks(self):
        task_data = self.database.query("SELECT * FROM tasks")
        task_objects = []
        for task in task_data:
            task_objects.append(Task(task["description"], task["completed"]))
        return task_objects

    def add_task(self, description, completed):
        self.database.query("INSERT INTO tasks (description, completed) VALUES('" + description + "', " + str(completed and 1 or 0) + ")")