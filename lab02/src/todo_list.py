class TodoList():

    def __init__(self, tasks):
        if not isinstance(tasks, list):
            raise TypeError

        for elem in tasks:
            if not isinstance(elem, str):
                raise ValueError

        self.tasks = tasks.copy()
        self.completed = set()
        self.active = set()

    def add_task(self, arg):
        if not isinstance(arg, str):
            raise ValueError

        self.tasks.append(arg)

    def __str__(self):
        return (f"All tasks:{self.tasks}, completed: {self.completed},"
                f" active: {self.active}.")

    def complete_task(self, index):
        if not isinstance(index, int) or 0 > index or index >= len(self.tasks):
            raise IndexError

        self.completed.add(index)


if __name__ == "__main__":
    t1 = TodoList([])
    print(t1)
    t1.add_task("Prepare project")
    print(t1)
    t1.complete_task(0)
    print(t1)