# CareerPilot AI

An AI-powered career guidance starter project built with **Next.js + FastAPI + Groq-hosted Llama**.

CareerPilot AI is designed to help students, fresh graduates, and experienced professionals:
- Create a career profile
- Receive an AI-generated profile review
- Identify skills to improve
- Get practical next-step recommendations

> This is an MVP starter repository. Job discovery, learning-plan tracking, assessments, and mock interviews are planned modules, not yet fully implemented.

## Tech stack

- Frontend: Next.js, React, TypeScript
- Backend: Python, FastAPI, SQLAlchemy
- AI: Groq API using a Meta Llama model
- Database: SQLite for local development

## Project structure

```text
careerpilot-ai/
├── backend/
│   ├── app/
│   │   ├── api/routes/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── app/
│   ├── lib/
│   └── .env.local.example
├── .gitignore
└── README.md
```

## Requirements

- Python 3.11 or newer
- Node.js 20.9 or newer
- npm
- A Groq API key

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/careerpilot-ai.git
cd careerpilot-ai
```

## 2. Configure the backend

Open PowerShell in the project folder:

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Open `backend/.env` and add your own Groq API key. Never commit this file.

```env
GROQ_API_KEY=your_new_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

The model name is configurable. Check your Groq console/model catalogue for the models currently enabled for your account.

Run the backend:

```powershell
uvicorn app.main:app --reload --port 8000
```

Backend:
- API: http://localhost:8000
- Interactive API documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## 3. Configure the frontend

Open a second terminal at the project root:

```powershell
cd frontend
Copy-Item .env.local.example .env.local
npm install
npm run dev
```

Open http://localhost:3000.

## 4. Test the application

1. Open the frontend at http://localhost:3000.
2. Enter a name, email, education, career goal, and skills.
3. Submit the profile.
4. Select **Analyze my profile** to receive AI guidance.

You can also test the backend directly at http://localhost:8000/docs.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/api/candidates` | Create a candidate profile |
| GET | `/api/candidates/{id}` | Retrieve a candidate |
| POST | `/api/candidates/{id}/analyze` | Generate AI career feedback |

## Security notes

- Never upload `.env`, `.env.local`, API keys, passwords, or private user data to GitHub.
- If an API key is exposed, revoke it and create a new one.
- The included SQLite database is for local development only.
- Add authentication, rate limiting, validation, privacy controls, and production database configuration before public deployment.
- AI output can be inaccurate. Users should verify job requirements and career decisions independently.

## Upload to your GitHub account

Create an empty repository on GitHub named `careerpilot-ai`. Do not add a README or license there because this project already contains a README.

Then, from this project folder:

```bash
git init
git add .
git commit -m "Initial CareerPilot AI MVP"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/careerpilot-ai.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

Before pushing, check that no secret files are staged:

```bash
git status
```

The `.gitignore` excludes `.env` files, virtual environments, local databases, and build outputs.

## Roadmap

- [x] Candidate profile creation
- [x] AI-powered profile analysis
- [ ] Job discovery and job matching
- [ ] Skill-gap analysis against selected job descriptions
- [ ] Personalized learning plans
- [ ] Skill assessments and progress tracking
- [ ] AI mock interviews
- [ ] User authentication and secure deployment
