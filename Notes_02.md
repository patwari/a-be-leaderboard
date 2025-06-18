## Stage 02: Set Up the PostgreSQL Database

1. Add `.env` file to hide credential to database.
   ```bash
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_NAME=postgres
    DB_HOST=db
    DB_PORT=5432
    DATABASE_URL=postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
   ```
2. Use this .env file in the `docker-compose.yml` and inside codes.
3. Create files
      ```
      app/
      ├── db/
      │   ├── base.py
      │   ├── models.py
      │   └── session.py
      ```
4. Connect SQLAlchemy to PostgreSQL in `session.py`
5. Create `base.py` for Models
6. Create `models.py` for the first model = user.
7. Run in docker > `docker compose up -w --remove-orphans`

## Test
1. Open http://127.0.0.1:8000/hello in chrome. You should get
 ```json
  {
      "message" : "Hello, world!"
  }
  ```

## For Future:
1. Add `Alembic` for DB migrations to `requirements.txt` (we didn’t add it before):
   - When we define the database schema in code, and change it later, we need to manually control the structure of database:
     - run `ALTER TABLE`
     - need to remember changes between versions. Which may introduce human errors.
   - So, we use `Alembic`:
     - It auto-generates migration scripts.
      - You can version control your database schema.
      - It applies migrations in the correct order automatically.
      - You avoid manually writing raw SQL.
