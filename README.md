# To-Do List API — (Beginner)

This is a simple To-Do List API built with Django REST Framework. It's designed as a warm-up project for beginners to practice model creation, viewsets, authentication, permissions, and basic testing.

---

##  Features

-  **Task Model** with fields: `id`, `title`, `completed`
-  **CRUD API** at `/tasks/` using `ModelViewSet`
-  **Token Authentication** with a custom `IsOwner` permission
-  **Filtering** support via `?completed=true/false`
-  **Pagination** using PageNumberPagination (10 per page)
-  **2 Unit Tests** for listing and creating tasks

---

## About Me

Hi, I'm Ashkan — a junior Django developer who recently transitioned from teaching English as a second language to learning backend development.  
I’m currently focused on improving my skills, building projects, and looking for opportunities to work as a backend developer.  
You can find more of my work here: [My GitHub](https://github.com/AsHkAn-Django)
[Linkdin](in/ashkan-ahrari-146080150)


## Permissions

A custom permission class (`AuthorOnly`) ensures that only the creator of a task can update or delete it. Any user can create and list tasks (based on queryset rules).

---

## Installation

1. Clone the repository
   `git clone https://github.com/your-username/todo-api-drf-tutorial.git`
2. Navigate into the folder  
   `cd your-project-name`
3. Create a virtual environment and activate it
   `python -m venv .venv`
   `source .venv/bin/activate  # Or .venv\Scripts\activate  on Windows`
4. Install the dependencies  
   `pip install -r requirements.txt`
5. Run the server
   `python manage.py migrate`
   `python manage.py createsuperuser`  
   `python manage.py runserver`


## Tutorial
COMING SOON
