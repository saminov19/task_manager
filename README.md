# Task Manager API

This app allows to manage users, roles, and tasks through API.

## Table of Contents
- [Authentication](#authentication)
- [Roles](#roles)
  - [List Roles](#list-roles)
  - [Create Role](#create-role)
  - [Read Role](#read-role)
  - [Update Role](#update-role)
  - [Partial Update Role](#partial-update-role)
  - [Delete Role](#delete-role)
  - [Delete Role by ID](#delete-role-by-id)
  - [Update Role by ID](#update-role-by-id)
- [Tasks](#tasks)
  - [List Tasks](#list-tasks)
  - [Create Task](#create-task)
  - [List Tasks](#list-tasks)
  - [Read Task](#read-task)
  - [Update Task](#update-task)
  - [Partial Update Task](#partial-update-task)
  - [Delete Task](#delete-task)
  - [Delete Task by ID](#delete-task-by-id)
  - [Update Task by ID](#update-task-by-id)
- [Users](#users)
  - [List Users](#list-users)
  - [Create User](#create-user)
  - [Read User](#read-user)
  - [Update User](#update-user)
  - [Partial Update User](#partial-update-user)
  - [Delete User](#delete-user)
  - [Delete User by ID](#delete-user-by-id)
  - [Update User by ID](#update-user-by-id)

## Authentication

- **Authorization Header:** `Authorization`

## Roles

### List Roles

- **URL:** `/tasks/roles/`
- **Method:** GET
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `[{ "id": 1, "name": "RoleName", "description": "RoleDescription" }]`

### Create Role

- **URL:** `/tasks/roles/`
- **Method:** POST
- **Parameters:** `data` (Body, Required, [Role](#role))
- **Responses:**
  - Success (HTTP 201)
    - Sample Response: `{"id": 1, "name": "RoleName", "description": "RoleDescription"}`

### Read Role

- **URL:** `/tasks/roles/{id}/`
- **Method:** GET
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "name": "RoleName", "description": "RoleDescription"}`

### Update Role

- **URL:** `/tasks/roles/{id}/`
- **Method:** PUT
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [Role](#role))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "name": "UpdatedRoleName", "description": "UpdatedRoleDescription"}`

### Partial Update Role

- **URL:** `/tasks/roles/{id}/`
- **Method:** PATCH
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [Role](#role))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "name": "UpdatedRoleName", "description": "UpdatedRoleDescription"}`

### Delete Role

- **URL:** `/tasks/roles/{id}/`
- **Method:** DELETE
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 204)

### Delete Role by ID

- **URL:** `/tasks/roles/{id}/delete_role/`
- **Method:** DELETE
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 204)

### Update Role by ID

- **URL:** `/tasks/roles/{id}/update_role/`
- **Method:** PUT
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [Role](#role))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "name": "UpdatedRoleName", "description": "UpdatedRoleDescription"}`

## Tasks

### List Tasks

- **URL:** `/tasks/tasks/`
- **Method:** GET
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `[{ "id": 1, "title": "TaskTitle", "description": "TaskDescription", "created_by": 1, "assigned_to": 2 }]`

### Create Task

- **URL:** `/tasks/tasks/`
- **Method:** POST
- **Parameters:** `data` (Body, Required, [Task](#task))
- **Responses:**
  - Success (HTTP 201)
    - Sample Response: `{"id": 1, "title": "TaskTitle", "description": "TaskDescription", "created_by": 1, "assigned_to": 2}`

### Read Task

- **URL:** `/tasks/tasks/{id}/`
- **Method:** GET
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "title": "TaskTitle", "description": "TaskDescription", "created_by": 1, "assigned_to": 2}`

### Update Task

- **URL:** `/tasks/tasks/{id}/`
- **Method:** PUT
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [Task](#task))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "title": "UpdatedTaskTitle", "description": "UpdatedTaskDescription", "created_by": 1, "assigned_to": 2}`

### Partial Update Task

- **URL:** `/tasks/tasks/{id}/`
- **Method:** PATCH
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [Task](#task))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "title": "UpdatedTaskTitle", "description": "UpdatedTaskDescription", "created_by": 1, "assigned_to": 2}`

### Delete Task

- **URL:** `/tasks/tasks/{id}/`
- **Method:** DELETE
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 204)

### Delete Task by ID

- **URL:** `/tasks/tasks/{id}/delete_task/`
- **Method:** DELETE
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 204)

### Update Task by ID

- **URL:** `/tasks/tasks/{id}/update_task/`
- **Method:** PUT
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [Task](#task))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "title": "UpdatedTaskTitle", "description": "UpdatedTaskDescription", "created_by": 1, "assigned_to": 2}`

## Users

### List Users

- **URL:** `/tasks/users/`
- **Method:** GET
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `[{ "id": 1, "username": "Username", "email": "user@example.com", "first_name": "FirstName", "last_name": "LastName", "password": "Password", "last_login": "2023-08-01T12:00:00Z", "is_active": true, "is_staff": false, "is_superuser": false, "date_joined": "2023-08-01T12:00:00Z", "groups": [1], "user_permissions": [1] }]`

### Create User

- **URL:** `/tasks/users/`
- **Method:** POST
- **Parameters:** `data` (Body, Required, [User](#user))
- **Responses:**
  - Success (HTTP 201)
    - Sample Response: `{"id": 1, "username": "Username", "email": "user@example.com", "first_name": "FirstName", "last_name": "LastName", "password": "Password", "last_login": "2023-08-01T12:00:00Z", "is_active": true, "is_staff": false, "is_superuser": false, "date_joined": "2023-08-01T12:00:00Z", "groups": [1], "user_permissions": [1]}`

### Read User

- **URL:** `/tasks/users/{id}/`
- **Method:** GET
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "username": "Username", "email": "user@example.com", "first_name": "FirstName", "last_name": "LastName", "password": "Password", "last_login": "2023-08-01T12:00:00Z", "is_active": true, "is_staff": false, "is_superuser": false, "date_joined": "2023-08-01T12:00:00Z", "groups": [1], "user_permissions": [1]}`

### Update User

- **URL:** `/tasks/users/{id}/`
- **Method:** PUT
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [User](#user))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "username": "UpdatedUsername", "email": "user@example.com", "first_name": "UpdatedFirstName", "last_name": "UpdatedLastName", "password": "Password", "last_login": "2023-08-01T12:00:00Z", "is_active": true, "is_staff": false, "is_superuser": false, "date_joined": "2023-08-01T12:00:00Z", "groups": [1], "user_permissions": [1]}`

### Partial Update User

- **URL:** `/tasks/users/{id}/`
- **Method:** PATCH
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [User](#user))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "username": "UpdatedUsername", "email": "user@example.com", "first_name": "UpdatedFirstName", "last_name": "UpdatedLastName", "password": "Password", "last_login": "2023-08-01T12:00:00Z", "is_active": true, "is_staff": false, "is_superuser": false, "date_joined": "2023-08-01T12:00:00Z", "groups": [1], "user_permissions": [1]}`

### Delete User

- **URL:** `/tasks/users/{id}/`
- **Method:** DELETE
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 204)

### Delete User by ID

- **URL:** `/tasks/users/{id}/delete_user/`
- **Method:** DELETE
- **Parameters:** `id` (Path, Required, Integer)
- **Responses:**
  - Success (HTTP 204)

### Update User by ID

- **URL:** `/tasks/users/{id}/update_user/`
- **Method:** PUT
- **Parameters:** `id` (Path, Required, Integer), `data` (Body, Required, [User](#user))
- **Responses:**
  - Success (HTTP 200)
    - Sample Response: `{"id": 1, "username": "UpdatedUsername", "email": "user@example.com", "first_name": "UpdatedFirstName", "last_name": "UpdatedLastName", "password": "Password", "last_login": "2023-08-01T12:00:00Z", "is_active": true, "is_staff": false, "is_superuser": false, "date_joined": "2023-08-01T12:00:00Z", "groups": [1], "user_permissions": [1]}`

## Definitions

### Role

- **Required Fields:** `name`, `description`
- **Properties:**
  - `id` (Integer, Read-Only)
  - `name` (String, Max Length: 255, Min Length: 1)
  - `description` (String, Min Length: 1)

### Task

- **Required Fields:** `title`, `description`, `created_by`, `assigned_to`
- **Properties:**
  - `id` (Integer, Read-Only)
  - `title` (String, Max Length: 255, Min Length: 1)
  - `description` (String, Min Length: 1)
  - `created_by` (Integer)
  - `assigned_to` (Integer)

### User

- **Required Fields:** `password`, `email`, `first_name`, `last_name`
- **Properties:**
  - `id` (Integer, Read-Only)
  - `password` (String, Max Length: 128, Min Length: 1)
  - `last_login` (Date-Time, Nullable)
  - `email` (String, Format: Email, Max Length: 254, Min Length: 1)
  - `username` (String, Max Length: 150, Min Length: 1)
  - `first_name` (String, Max Length: 255, Min Length: 1)
  - `last_name` (String, Max Length: 255, Min Length: 1)
  - `is_active` (Boolean)
  - `is_staff` (Boolean)
  - `is_superuser` (Boolean)
  - `date_joined` (Date-Time)
  - `groups` (Array of Integers, Unique Items)
  - `user_permissions` (Array of Integers, Unique Items)
