# Kutchi-curriculum


Database schema:
```mysq
CREATE DATABASE user_auth;

USE user_auth;

CREATE TABLE credentials (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE user_info (
    user_id INT,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES credentials(user_id) ON DELETE CASCADE
);
```


Dependencies:
```python
pip install fastapi uvicorn jinja2 mysql-connector-python python-multipart
```


Run FastAPI:
```bash
uvicorn login-with-frontend:app --reload
```
