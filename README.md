
# 🏆 Leaderboard & Game Analytics API

This is a **personal backend project** to learn and practice modern **Python backend development** 

---

## 🎯 Project Purpose

This project simulates a **real-world game backend** system used to track:

- User registration & authentication
- Score submission & updates
- Leaderboard with top scores and user ranks
- Daily & weekly active user analytics

The goal is to build a **modular, production-ready backend** with best practices in Python.

---

## 🧱 Tech Stack

| Tool         | Purpose                             |
|--------------|-------------------------------------|
| FastAPI      | API framework                       |
| PostgreSQL   | Primary database                    |
| SQLAlchemy   | ORM for Python ↔ DB interaction     |
| Alembic      | Database migrations                 |
| Docker       | Containerization                    |
| JWT (Jose)   | Authentication                      |
| Pytest       | Unit + integration testing          |

---

## 🧠 Key Learnings

- Project layout and modular structuring in FastAPI
- Working with relational DBs in real use cases (joins, ranking, aggregates)
- Using Redis (later) for rate limiting, matchmaking (optional)
- Deploying a full Python backend on Docker
- Writing professional documentation and APIs

---

## 🚀 Features

### 👤 Authentication
- `POST /register` – Create new user
- `POST /login` – Get JWT token
- Token-based auth for protected routes

### 🕹️ Score Submission
- `POST /submit_score` – Submit or update score for current user
- Stores best score per user per day

### 📈 Leaderboards
- `GET /leaderboard?top=10` – Top users sorted by score
- `GET /user_rank` – Get rank and current score of logged-in user

### 📊 Analytics
- `GET /stats/dau` – Daily Active Users
- `GET /stats/wau` – Weekly Active Users
- `GET /stats/score_distribution` – Score histogram (bucketed)

---

## 🔧 Installation & Running Locally

> Make sure you have **Docker + docker-compose** installed.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/leaderboard-api.git
cd leaderboard-api
```

### 2. Create `.env` File

```env
DATABASE_URL=postgresql://postgres:password@db:5432/leaderboard
JWT_SECRET_KEY=your_super_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Run the Services

```bash
docker-compose up --build
```

API should now be available at `http://localhost:8000`

### 4. API Docs

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger documentation.

---

## 🧪 Testing

```bash
docker exec -it leaderboard-api bash
pytest
```

Tests are located in the `/tests` folder and include auth, score submission, and leaderboard ranking logic.

---

## 📦 Project Structure

```
app/
│
├── main.py              # FastAPI app entrypoint
├── models.py            # SQLAlchemy DB models
├── schemas.py           # Pydantic request/response models
├── crud.py              # DB logic
├── auth.py              # JWT utilities & password hashing
├── db.py                # DB session and engine
└── routers/             # API routes for users, scores, stats

alembic/                 # DB migrations
tests/                   # Unit & integration tests
```

---

## 🌍 Deployment

The project can be deployed to platforms like:
- [Render](https://render.com)
- [Railway](https://railway.app)
- [Fly.io](https://fly.io)

> Instructions for deploying to Railway are included in [`/deployment/railway.md`](deployment/railway.md)

---

## 🧠 Why This Project Matters

While inspired by casual games, this project is **domain-agnostic** and focuses on **backend fundamentals**:

- Auth flows and access management
- Efficient relational data modeling
- Time-based analytics and aggregations
- Performance via pagination, indexes, and caching potential
- Dockerized services with test coverage

✅ It’s designed to reflect the kind of **modular, production-grade backend** you’d build for any SaaS, analytics, or game product.

---

## 📚 Learning Goals

- FastAPI + PostgreSQL best practices
- Writing clean, modular backend code
- Secure, authenticated APIs using JWT
- Deployable Dockerized services
- Building APIs that scale: analytics, stats, and leaderboards

---

## 🙋 About This Project

This is a personal project created by [Your Name] to:
- Deepen backend engineering experience with Python
- Transition toward high-ceiling backend/software roles
- Build a portfolio of deployable, real-world systems

Feel free to fork, modify, or contribute!

---

## 📬 Contact

- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- GitHub: [github.com/yourusername](https://github.com/yourusername)
