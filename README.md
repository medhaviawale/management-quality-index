# Management Quality Index (MQI) Platform 🚀

Hi! Welcome to my project. The Management Quality Index (MQI) is a full-stack AI platform that I built to predict stock market performance. 

Usually, people only look at financial numbers to guess how a stock will perform. I wanted to try something different: predicting stock movement by analyzing the actual behavior, ethics, and communication style of company leaders and CEOs. 

## 💻 How We Built It (Tech Stack)
* **Frontend:** Next.js 14 (for a clean, fast user interface)
* **Backend:** FastAPI with Python (for handling asynchronous data requests)
* **AI & Machine Learning:** LLaMA 3.3-70B (for scoring behavior) & FinBERT (for analyzing sentiment in financial texts)
* **Database:** MongoDB Atlas (for session tracking and managing state)

## ⚙️ What It Actually Does
* **Smart Data Extraction:** The system automatically scrapes public digital footprints of executives (like earnings calls, interviews, and PR statements).
* **The 5-C Behavioral Framework:** Instead of random AI guesses, the LLM strictly scores leaders on 5 metrics: Character, Competence, Cohesion, Commitment, and Communication. 
* **Harmonic Fusion Engine:** It takes the AI-generated "Management Score" and combines it with real-time quantitative data from Yahoo Finance to generate a simple Buy, Hold, or Sell signal.
* **Predictive Sandbox:** A cool feature I added where you can simulate "what-if" scenarios (like what happens to the stock if a CEO suddenly resigns).

Feel free to explore the code!
