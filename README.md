# AI Mock Interview Platform 🎯

An AI-powered interview preparation platform that generates technical interview questions based on user skills and provides performance analysis.

## Features
- Generate interview questions using Google Gemini AI
- Skill-based question generation
- Upload and analyze resumes
- Performance evaluation and scoring
- Detailed interview reports
- Simple and interactive Streamlit interface

## Tech Stack
- Python
- Streamlit
- Google Gemini API
- Pandas
- SQLite
- NLP

## Project Structure
ai-mock-interview-platform/ │── app.py │── auth.py │── dashboard.py │── database.py │── evaluation.py │── parser.py │── questions.py │── report.py │── requirements.txt │── uploads/ │── reports/

## Installation

1. Clone the repository
bash git clone https://github.com/bishtujjwal128-tech/ai-mock-interview-platform.git cd ai-mock-interview-platform 

2. Install dependencies
bash pip install -r requirements.txt 

3. Add your Gemini API key in a .env file:
env GOOGLE_API_KEY=your_api_key_here 

4. Run the application
bash streamlit run app.py 

## Future Enhancements
- Voice-based mock interviews
- HR interview simulation
- Resume feedback system
- Interview analytics dashboard

## Author
Ujjwal Bisht  
B.Tech Artificial Intelligence & Machine Learning  
Delhi Technical Campus, GGSIPU
