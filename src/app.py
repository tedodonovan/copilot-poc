"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Basketball": {
        "description": "Join the basketball team and compete in local tournaments",
        "type": "Sports",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Soccer": {
        "description": "Play soccer and improve your teamwork skills",
        "type": "Sports",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Tennis": {
        "description": "Learn and play tennis with peers",
        "type": "Sports",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 8,
        "participants": []
    },
    "Swimming": {
        "description": "Swim and train for competitions",
        "type": "Sports",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 10,
        "participants": []
    },
    "Painting": {
        "description": "Express your creativity through painting",
        "type": "Artistic",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    },
    "Drama Club": {
        "description": "Act, direct, and participate in school plays",
        "type": "Artistic",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Photography": {
        "description": "Learn photography techniques and build a portfolio",
        "type": "Artistic",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Choir": {
        "description": "Sing in the school choir and perform at events",
        "type": "Artistic",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": []
    },
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "type": "Intellectual",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Mathletes": {
        "description": "Compete in math competitions and improve problem-solving skills",
        "type": "Intellectual",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "type": "Intellectual",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Science Olympiad": {
        "description": "Participate in science competitions and experiments",
        "type": "Intellectual",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "type": "Intellectual",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "type": "Sports",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up")
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
