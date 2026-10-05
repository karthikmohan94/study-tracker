# Study Task Tracker

A Django web application for creating and managing study tasks. Users can add tasks, mark them as completed or pending, and delete them. Tasks are stored in a SQLite database, so they remain available after the page is refreshed.

## Features

- Add new study tasks
- View all saved tasks
- Mark tasks as completed or pending
- Delete tasks
- Display the current status of each task
- Validate task titles using a Django `ModelForm`
- Protect form submissions using Django’s CSRF protection
- Use POST requests for actions that change data

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS

## How the Application Works

The application follows Django’s Model-Template-View structure:

- **Model:** The `Task` model defines the title and completion status stored for each task.
- **Form:** `TaskForm` creates and validates the task-title input.
- **Views:** The views retrieve, create, update, and delete tasks.
- **Templates:** The HTML template displays the form and the saved tasks.
- **URLs:** URL patterns connect browser requests to the correct views.

A newly created task receives `False` as its default `completed` value. The toggle view reverses this value when the user marks a task as completed or pending.

## Project Structure

```text
study-task-tracker/
├── config/
│   ├── settings.py
│   └── urls.py
├── tasks/
│   ├── migrations/
│   ├── static/
│   │   └── tasks/
│   │       └── style.css
│   ├── templates/
│   │   └── tasks/
│   │       └── task_list.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
```

## Run the Project Locally

### 1. Clone the repository

Use the **Code** button at the top of this GitHub repository to copy its URL, then run:

```bash
git clone <copied-repository-url>
cd study-task-tracker


### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install Django

```bash
python -m pip install django
```

### 5. Apply the migrations

```bash
python manage.py migrate
```

This creates the required database tables.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the following address in a browser:

```text
http://127.0.0.1:8000/
```

## Main Model

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

Each task contains:

- `title`: The text describing the study task.
- `completed`: A Boolean value showing whether the task is finished.

A new task starts as pending because `completed` defaults to `False`.

## Main Operations

The application supports the four basic database operations:

| Operation | Application feature |
|---|---|
| Create | Add a new task |
| Read | Display saved tasks |
| Update | Mark a task completed or pending |
| Delete | Remove a task |

## What I Learned

While developing this project, I practised:

- Organising a Django project and app
- Designing a model and applying migrations
- Using Django’s ORM for database operations
- Creating and validating a `ModelForm`
- Connecting project URLs, app URLs, and views
- Passing data from a view to a template
- Using Django template tags and conditions
- Handling GET and POST requests
- Applying CSRF protection
- Restricting data-changing views to POST requests
- Styling a responsive interface with CSS

## Current Scope

This version is a local, single-user learning project. It currently does not include user accounts, private task lists, due dates, categories, or online deployment.

## Possible Future Improvements

- Add user registration and login
- Give each user a private task list
- Add task editing
- Add due dates and categories
- Add search and filtering
- Add automated tests
- Deploy the application online

## Author

**Karthik Mohan**

[LinkedIn](https://www.linkedin.com/in/karthik-mohan-311ab03bb/)
