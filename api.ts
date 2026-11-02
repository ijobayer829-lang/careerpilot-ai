const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export type CandidateInput = {
  full_name: string;
  email: string;
  education: string;
  experience_years: number;
  career_goal: string;
  location: string;
  skills: string[];
  interests: string[];
};

export async function createCandidate(payload: CandidateInput) {
  const response = await fetch(`${API_URL}/api/candidates`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await response.json();
  if (!response.ok) throw new Error(data.detail || "Could not save your profile.");
  return data;
}

export async function analyzeCandidate(candidateId: number): Promise<string> {
  const response = await fetch(`${API_URL}/api/candidates/${candidateId}/analyze`, {
    method: "POST",
  });
  const data = await response.json();
  if (!response.ok) throw new Error(data.detail || "Could not analyze your profile.");
  return data.analysis;
}
