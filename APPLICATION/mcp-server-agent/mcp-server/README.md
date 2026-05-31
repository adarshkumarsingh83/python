
### To shout down process on 8000 port 
- kill -9 $(lsof -t -i:8000)


python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
