# SmartCampus Project - Automated Planning Management System (APMS)

## Architectural Overview

The Automated Planning Management (APMS) project is organized in a modular architecture composed of three main layers: a Docker container for planner execution, a backend service for business logic and integrations, and a frontend web application.

This structure follows the principles of separation of concerns, facilitating development, maintenance, and scalability.

- **smartcampus-container**: Responsible for the isolated execution of planning algorithms using PDDL. Works as an independent service in a Docker container.
- **smartcampus-service**: Backend that orchestrates the generation of PDDL files (Planning Domain Definition Language), planner execution, and exposure of REST APIs for the frontend.
- **smartcampus-web**: Web interface that consumes the backend APIs to display data and allow interactions with IoT devices in a university campus.

Communication between layers occurs via REST APIs and Docker container execution for process isolation.

## Technologies Used

### smartcampus-container

- **Docker**: For containerization and execution environment isolation.
- **PDDL**: Language for defining planning domains and problems.
- **POPF-TIF**: Planner used to solve PDDL problems based on the domain, obtaining an action plan to solve the problems.

### smartcampus-service

- **Python**: Language used for the backend.
- **FastAPI**: Framework for creating asynchronous REST APIs.
- **APScheduler**: For scheduling tasks (plan actions).
- **Docker SDK**: For integration and execution of the planner container.
- **Pydantic**: For data validation and DTOs (Data Transfer Objects).

### smartcampus-web

- **Vue.js**: JavaScript framework for building the user interface.
- **TypeScript**: For static typing in the frontend.
- **Vite**: Fast build tool and development server.
- **SCSS**: For CSS styles.
- **Axios**: For HTTP requests to the backend APIs.

## Step-by-Step Guide to Run Each Project

### General Prerequisites

- Docker installed and running.
- Python 3.8+ installed.
- Node.js 16+ and npm installed.
- Git to clone the repository (if necessary).

### 1. smartcampus-container

This module is a Docker container that runs the PDDL planner.

1. Navigate to the `smartcampus-container` folder:

   ```
   cd smartcampus-container
   ```

2. Build the Docker image:

   ```
   docker build -t smartcampus-planner .
   ```

3. Run the container (optional, for isolated testing):

   ```
   docker run --rm -v $(pwd)/data:/data smartcampus-planner
   ```

   - Input files (domain.pddl, problem.pddl) should be in `data/`.
   - The generated plan will be saved in `data/output/plan.txt`.

### 2. smartcampus-service

This is the Python backend that integrates everything.

1. Navigate to the `smartcampus-service` folder:

   ```
   cd smartcampus-service
   ```

2. Install Python dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:

   ```
   python -m uvicorn app.main:app --reload
   ```

   - The server will be available at `http://localhost:8000`.
   - API documentation at `http://localhost:8000/docs` (Swagger UI).

4. (Optional) To run tests:
   ```
   pytest
   ```

### 3. smartcampus-web

This is the Vue.js frontend.

1. Navigate to the `smartcampus-web` folder:

   ```
   cd smartcampus-web
   ```

2. Install npm dependencies:

   ```
   npm install
   ```

3. Run the development server:

   ```
   npm run dev
   ```

   - The application will be available at `http://localhost:5173` (Vite default port).

4. (Optional) For production build:
   ```
   npm run build
   ```

## Additional Notes

- Make sure the backend (smartcampus-service) is running before starting the frontend, as it consumes the APIs.
- The planner container is executed by the backend via Docker SDK, not manually in production.
- For full development, run all three modules simultaneously in separate terminals.
