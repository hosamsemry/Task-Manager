# Task Manager API

Task Manager API is a Django project that provides APIs for managing projects, tasks, comments, and activity logs.

## Features

### 1. User Authentication: Users can register, log in, and manage their accounts.

### 2. Project Management: Create, retrieve, update, and delete projects.

### 3. Task Management: Create, retrieve, update, and delete tasks within projects.

### 4. Commenting System: Users can add comments on tasks.

### 5. Activity Logging: Records user actions on tasks, such as creation and updates.

## Installation
To install and run the Task Manager API on your local machine, follow these steps:

### Clone the Repository:
git clone https://github.com/hosamsemry/Task-Manager.git
### Navigate to the Project Directory
### Install Dependencies:
pip install -r requirements.txt

## Usage

After setting up the project, you can access the API endpoints using tools like curl, Postman, or any programming language's HTTP library.

## API Endpoints

### Projects
- GET /api/projects/: List all projects.
- POST /api/projects/: Create a new project.
- GET /api/projects/{project_id}/: Retrieve details of a specific project.
- PUT /api/projects/{project_id}/: Update a project.
- DELETE /api/projects/{project_id}/: Delete a project.
### Tasks
- GET /api/tasks/: List all tasks.
- POST /api/tasks/: Create a new task.
- GET /api/tasks/{task_id}/: Retrieve details of a specific task.
- PUT /api/tasks/{task_id}/: Update a task.
- DELETE /api/tasks/{task_id}/: Delete a task.
### Comments
- GET /api/comments/: List all comments.
- POST /api/comments/: Create a new comment.
- GET /api/comments/{comment_id}/: Retrieve details of a specific comment.
- PUT /api/comments/{comment_id}/: Update a comment.
- DELETE /api/comments/{comment_id}/: Delete a comment.
### Activity Logs
- GET /api/activity-logs/: List all activity logs.
- GET /api/activity-logs/{log_id}/: Retrieve details of a specific activity log.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.
