class Task:
    def __init__(self, task_description, task_completed=False):
        # Python __ prefix = private field
        self.__task_description = task_description
        self.__task_completed = task_completed

    def get_description(self):
        return self.__task_description

    def is_completed(self):
        return self.__task_completed
