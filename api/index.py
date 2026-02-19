import subprocess
import sys

def handler(request):
    """Handler for Vercel serverless function - runs Streamlit app"""
    subprocess.Popen([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py",
        "--server.port=8501",
        "--server.address=0.0.0.0",
        "--server.headless=true"
    ])
    return "Streamlit app started"
