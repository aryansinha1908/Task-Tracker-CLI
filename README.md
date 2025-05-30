*Task Tracker* :- App to make to-do lists and manage them using command line interface.

# Functions for the app:-
1) Create multiple to-do lists
2) Add, delete and update tasks in the to-do lists.
3) Update tasks as done, in-progress and late.
4) List all tasks of the to-do list.
5) List tasks with tags; done/pending/not started.

# Commands List:-
1) Adding a new task
task-cli add "Buy groceries"

2) Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

3) Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

4) Listing all tasks
task-cli list

5) Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
