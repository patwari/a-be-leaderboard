## Initial Setup

1. Setup folder structure
    ```bash
    mkdir a-be-leaderboard && cd a-be-leaderboard
    mkdir app
    touch app/main.py requirements.txt Dockerfile docker-compose.yml
    ```

2. Create `requirements.txt`
   ```txt
    fastapi
    uvicorn[standard]
    psycopg2-binary
    sqlalchemy
    python-jose[cryptography]
    passlib[bcrypt]
    python-dotenv
   ```

3. Create `DockerFile`
4. Create `docker-compose.yml`
5. Create `app/main.py`
6. `docker-compose up --build`
7. Open browser, and open url `http://localhost:8000/hello`. You'll see the result.