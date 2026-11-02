from groq import Groq

from app.core.config import settings


class CareerAIService:
    def __init__(self):
        if not settings.groq_api_key:
            raise RuntimeError(
                "GROQ_API_KEY is not configured. Add it to backend/.env."
            )
        self.client = Groq(api_key=settings.groq_api_key)

    def analyze_candidate(self, candidate) -> str:
        profile = {
            "name": candidate.full_name,
            "education": candidate.education,
            "experience_years": candidate.experience_years,
            "career_goal": candidate.career_goal,
            "location": candidate.location,
            "skills": candidate.skills or [],
            "interests": candidate.interests or [],
        }

        response = self.client.chat.completions.create(
            model=settings.groq_model,
            temperature=0.4,
            max_tokens=900,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are CareerPilot AI, a practical and supportive career "
                        "coach. Give realistic, actionable advice. Do not invent "
                        "qualifications or guarantee employment. Structure the "
                        "answer with: Profile summary, Strengths, Skill gaps, "
                        "Recommended next steps, and a 30-day action plan. "
                        "If information is missing, state your assumptions."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Analyze this candidate profile:\n{profile}",
                },
            ],
        )
        return response.choices[0].message.content or "No analysis was returned."
