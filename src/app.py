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
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Shooting Club": {
        "description": "Learn and practice shooting in a safe and controlled environment",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Lacrosse Team": {
        "description": "Join the lacrosse team and compete in local tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Graphic Design Workshop": {
        "description": "Learn graphic design skills and create stunning visuals",
        "schedule": "Wednesdays, 3:00 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Woodworking Club": {
        "description": "Learn woodworking skills and create handmade projects",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["elijah@mergington.edu", "isabella@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and critical thinking skills through debates",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu", "charlotte@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and participate in math competitions",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["benjamin@mergington.edu", "lucas@mergington.edu"]
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

    # Get the specificy activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    
    
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
