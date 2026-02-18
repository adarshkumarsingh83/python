# Python REST Client (FastAPI proxy)

This repository implements a small Python client application that exposes a FastAPI-based local REST API and forwards requests to a remote backend according to entries defined in a YAML configuration file.

**Purpose**
- Provide a local API surface for CRUD operations on `Employee` resources.
- Forward each request to a configured remote API endpoint (the "backend") using an integration layer.

**Quick summary**
- Start point: [main.py](main.py#L1-L14) — builds configuration, wires services and controller, then runs the FastAPI app.
- Local API: `127.0.0.1:8090` by default (see [main.py](main.py#L1-L14)).
- Remote API config: `resources/application.yml` — defines base URLs, paths and HTTP methods used by the `IntegrationService`.

Table of important files
- [main.py](main.py#L1-L14): application entry point, starts uvicorn.
- [resources/application.yml](resources/application.yml#L1-L20): API mapping configuration loaded at startup.
- [src/bean/Employee.py](src/bean/Employee.py#L1-L20): `Employee` Pydantic model.
- [src/config/YmlReader.py](src/config/YmlReader.py#L1-L80): loads YAML into `ConfigBean` and `ApiConfigBean` objects.
- [src/config/bean/ConfigBean.py](src/config/bean/ConfigBean.py#L1-L40): dataclasses for API config entries.
- [src/config/ApplicationConfig.py](src/config/ApplicationConfig.py#L1-L120): wiring: locate YAML, instantiate `IntegrationService`, `EmployeeService`, and `ApplicationController`.
- [src/service/IntegrationService.py](src/service/IntegrationService.py#L1-L400): performs HTTP requests to the remote service using `requests`.
- [src/service/EmployeeService.py](src/service/EmployeeService.py#L1-L200): business/service layer converting integration results to `Employee` models and returning friendly messages.
- [src/web/ApplicationController.py](src/web/ApplicationController.py#L1-L120): FastAPI controller that exposes endpoints and uses `Depends` to access `EmployeeService`.

Architecture and flow
1. `main.py` creates an `ApplicationConfig` instance.
2. `ApplicationConfig` locates `resources/application.yml`, uses `YmlReader` to parse it into dataclasses, and builds an `apiConfigStore` mapping names to `ApiConfigBean`.
3. `IntegrationService` is created with `apiConfigStore`; it looks up the correct mapping by the integration method name and performs HTTP calls (`GET`, `POST`, `PUT`, `DELETE`).
4. `EmployeeService` calls `IntegrationService` and maps returned JSON into `Employee` objects (`Employee(**emp_data)`).
5. `ApplicationController` registers FastAPI routes and delegates to `EmployeeService` methods.

Configuration details (application.yml)
- The code expects a list of API definitions with fields: `name`, `baseUrl`, `url`, and `httpMethod`.
- Example (recommended top-level format):

```yaml
apis:
  - name: "createEmployee"
    baseUrl: "http://localhost:8000"
    url: "/api/v1/employee"
    httpMethod: "POST"
  - name: "getEmployee"
    baseUrl: "http://localhost:8000"
    url: "/api/v1/employee/{id}"
    httpMethod: "GET"
  - name: "getAllEmployees"
    baseUrl: "http://localhost:8000"
    url: "/api/v1/employee"
    httpMethod: "GET"
  - name: "updateEmployee"
    baseUrl: "http://localhost:8000"
    url: "/api/v1/employee/{id}"
    httpMethod: "PUT"
  - name: "deleteEmployee"
    baseUrl: "http://localhost:8000"
    url: "/api/v1/employee/{id}"
    httpMethod: "DELETE"
```

Note: The repository's supplied `resources/application.yml` uses a nested namespace (`com.chase.espark.apis`) which will not be found by the current `YmlReader` implementation. Either change the file to the top-level `apis` format above, or modify `YmlReader` to extract the nested path.

Step-by-step setup and run (Windows)
1. Ensure Python 3.9+ is installed.
2. Create and activate a virtual environment (optional but recommended):

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install fastapi uvicorn pydantic requests PyYAML
```

4. (Optional) Create `requirements.txt` to pin versions:

```powershell
pip freeze > requirements.txt
```

5. Ensure `resources/application.yml` is in the expected place (`resources/` adjacent to `src/`) and is in the expected format (see above).

6. Run the app:

```powershell
python main.py
```

The app will start a FastAPI server on `127.0.0.1:8090` by default. Open `http://127.0.0.1:8090/docs` for the Swagger UI.

Example requests (curl)
- Get all employees:

```bash
curl -X GET http://127.0.0.1:8090/api/employees
```

- Get an employee by id:

```bash
curl -X GET http://127.0.0.1:8090/api/employees/1
```

- Create an employee:

```bash
curl -X POST http://127.0.0.1:8090/api/employees -H "Content-Type: application/json" -d '{"employeeId": 10, "name": "Alice"}'
```

- Update an employee:

```bash
curl -X PUT http://127.0.0.1:8090/api/employees/10 -H "Content-Type: application/json" -d '{"employeeId": 10, "name": "Alice Updated"}'
```

- Delete an employee:

```bash
curl -X DELETE http://127.0.0.1:8090/api/employees/10
```

What to expect from responses
- `IntegrationService` forwards remote responses and tries to parse JSON. On failures it prints an error and returns an empty list / None / False depending on the method.
- `EmployeeService` wraps integration responses into `Employee` objects for GET endpoints, and returns simple success messages for write operations.

Common troubleshooting
- YAML path: If you get `FileNotFoundError` from `ApplicationConfig.loadConfig`, check `resources/application.yml` path and ensure the file exists.
- YAML structure: If `YmlReader` reads no APIs (returns `None` or an empty list), either change the YAML to top-level `apis` or update `YmlReader` to read the nested keys.
- Remote backend: The code expects the remote backend to be available at the `baseUrl` configured in the YAML (example `http://localhost:8000`). Start or point to the actual backend before issuing proxied requests.
- Logging: The project prints simple debug messages to stdout. Check the console output for `Executing method:` and `Making <METHOD> request to URL:` messages from `IntegrationService`.

Suggested improvements (next steps)
- Add `requirements.txt` or `pyproject.toml` and commit it.
- Improve `YmlReader` to support nested configuration keys and/or environment-specific overrides.
- Add proper logging instead of `print()` statements.
- Add unit tests for `IntegrationService` using mocked `requests` responses.
- Add health check endpoints for the local API and remote backend connectivity checks.

If you want, I can:
- create a `requirements.txt` with pinned versions,
- update `src/config/YmlReader.py` to read the nested `com.chase.espark.apis` structure in the provided YAML,
- or add simple tests and example curl scripts.
