import asyncio
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import AsyncGroq

app = FastAPI(title="Management Quality Index API")
semaphore = asyncio.Semaphore(2) # Max 2 in-flight Groq API calls

class ExecutiveData(BaseModel):
    name: str
    ticker: str
    context: str
    sentiment_prior: float

@app.post("/api/score")
async def score_executive(data: ExecutiveData):
    client = AsyncGroq()
    
    async with semaphore:
        prompt = f"""You are a quantitative executive psychometrics analyst.
        Analyze the following executive digital footprint for {data.ticker}.
        FinBERT sentiment prior: {data.sentiment_prior} (range: -1 to +1).
        
        Executive Context:
        {data.context}
        
        Score each 5-C dimension as an integer in [0,20] where 20 = optimal:
        1. character: ethical integrity, low narcissism, no contradictions
        2. competence: domain expertise, track record vs. industry
        3. cohesion: TMT alignment with strategic messaging
        4. commitment: long-term orientation, insider equity retention
        5. communication: clarity, low fog index, low hedge density
        
        Respond ONLY with valid JSON. Scores must be consistent with the sentiment prior."""
        
        try:
            resp = await client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                response_format={"type": "json_object"},
                max_tokens=512
            )
            scores = json.loads(resp.choices[0].message.content)
            return {"status": "success", "data": scores}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
