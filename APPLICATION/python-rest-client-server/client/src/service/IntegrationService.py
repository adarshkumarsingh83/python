import requests
import inspect
from src.bean.Employee import Employee
from src.config.bean.ConfigBean import ConfigBean, ApiConfigBean


class IntegrationService:
    def __init__(self, apiConf: dict):
        self.apiConf = apiConf

    def getAllEmployees(self) -> list[dict]:
        currentMethod = inspect.currentframe().f_code.co_name
        print(f"Executing method: {currentMethod}")
        apiconfig: ApiConfigBean = self.apiConf.get(currentMethod)
        if not apiconfig:
            print(f"API config for method '{currentMethod}' not found.")
            return []
        url = apiconfig.baseUrl + apiconfig.url
        print(f"Making {apiconfig.httpMethod} request to URL: {url}")
        method: str = apiconfig.httpMethod.upper() 
        try:
            if method == 'GET':
                response = requests.get(url)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            response.raise_for_status()
            employees_data = response.json()
            print(f"Received data: {employees_data}")
            return employees_data
        except Exception as e:
            print(f"Error in {currentMethod}: {e}")
            return []
        
    def getEmployee(self, emp_id: int) -> dict:
        currentMethod = inspect.currentframe().f_code.co_name
        print(f"Executing method: {currentMethod} with emp_id: {emp_id}")
        apiconfig: ApiConfigBean = self.apiConf.get(currentMethod)
        if not apiconfig:
            print(f"API config for method '{currentMethod}' not found.")
            return None
        url = apiconfig.baseUrl + apiconfig.url.format(emp_id=emp_id)
        print(f"Making {apiconfig.httpMethod} request to URL: {url}")
        method: str = apiconfig.httpMethod.upper() 
        try:
            if method == 'GET':
                response = requests.get(url)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            response.raise_for_status()
            emp_data = response.json()
            print(f"Received data: {emp_data}")
            return emp_data
        except Exception as e:
            print(f"Error in {currentMethod}: {e}")
            return None 
        
        
    def createEmployee(self, employee: Employee) -> str:
        currentMethod = inspect.currentframe().f_code.co_name
        print(f"Executing method: {currentMethod} with employee: {employee}")
        apiconfig: ApiConfigBean = self.apiConf.get(currentMethod)
        if not apiconfig:
            print(f"API config for method '{currentMethod}' not found.")
            return None
        url = apiconfig.baseUrl + apiconfig.url
        print(f"Making {apiconfig.httpMethod} request to URL: {url} with data: {employee}")
        method: str = apiconfig.httpMethod.upper() 
        try:
            if method == 'POST':
                response = requests.post(url, json=employee.__dict__)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            response.raise_for_status()
            emp_data = response.json()
            response_text = response.text.strip('"')
            print(f"Received data: {emp_data} {response_text}")
            return emp_data
        except Exception as e:
            print(f"Error in {currentMethod}: {e}")
            return None
        
        
    def updateEmployee(self, emp_id: int, employee: Employee) -> str:
        currentMethod = inspect.currentframe().f_code.co_name
        print(f"Executing method: {currentMethod} with emp_id: {emp_id} and employee: {employee}")
        apiconfig: ApiConfigBean = self.apiConf.get(currentMethod)
        if not apiconfig:
            print(f"API config for method '{currentMethod}' not found.")
            return None
        url = apiconfig.baseUrl + apiconfig.url.format(emp_id=emp_id)
        print(f"Making {apiconfig.httpMethod} request to URL: {url} with data: {employee}")
        method: str = apiconfig.httpMethod.upper() 
        try:
            if method == 'PUT':
                response = requests.put(url, json=employee.__dict__)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            response.raise_for_status()
            emp_data = response.json()
            response_text = response.text.strip('"')
            print(f"Received data: {emp_data} {response_text}")
            return emp_data
        except Exception as e:
            print(f"Error in {currentMethod}: {e}")
            return None
        
    def deleteEmployee(self, emp_id: int) -> str:
        currentMethod = inspect.currentframe().f_code.co_name
        print(f"Executing method: {currentMethod} with emp_id: {emp_id}")
        apiconfig: ApiConfigBean = self.apiConf.get(currentMethod)
        if not apiconfig:
            print(f"API config for method '{currentMethod}' not found.")
            return False
        url = apiconfig.baseUrl + apiconfig.url.format(emp_id=emp_id)
        print(f"Making {apiconfig.httpMethod} request to URL: {url}")
        method: str = apiconfig.httpMethod.upper() 
        try:
            if method == 'DELETE':
                response = requests.delete(url)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            response.raise_for_status()
            response_data = response.json()
            response_text = response.text.strip('"')
            print(f"Received data: {response_data} {response_text}")
            return response_data
        except Exception as e:
            print(f"Error in {currentMethod}: {e}")
            return False