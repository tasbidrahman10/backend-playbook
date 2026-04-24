"""Exercise 01: identity vs equality."""


class Task:
    """Simple entity model for identity/equality experiments."""

    def __init__(self, task_id: int, title: str, done: bool = False) -> None:
        self.task_id = task_id
        self.title = title
        self.done = done

    def __repr__(self) -> str:
        return (
            f"Task(task_id={self.task_id}, "
            f"title={self.title!r}, done={self.done})"
        )

    def __str__(self) -> str:
        status = "done" if self.done else "todo"
        return f"[{self.task_id}] {self.title} ({status})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return self.task_id == other.task_id


def build_demo_tasks() -> tuple[Task, Task, Task, Task]:
    task_a = Task(1, "Write equality lab")
    same_reference = task_a
    same_id_new_instance = Task(1, "Write equality lab")
    different_id = Task(2, "Read logs")
    return task_a, same_reference, same_id_new_instance, different_id


def main() -> None:
    task_a, same_reference, same_id_new_instance, different_id = build_demo_tasks()

    print("Identity checks (is):")
    print("task_a is same_reference ->", task_a is same_reference)
    print("task_a is same_id_new_instance ->", task_a is same_id_new_instance)

    print("\nEquality checks (==):")
    print("task_a == same_reference ->", task_a == same_reference)
    print("task_a == same_id_new_instance ->", task_a == same_id_new_instance)
    print("task_a == different_id ->", task_a == different_id)

    print("\nrepr(task_a):", repr(task_a))
    print("str(task_a):", str(task_a))


if __name__ == "__main__":
    main()
