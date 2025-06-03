# Technical Design Document – CyberGuardian

## 1. Features

- Multiple-choice scenario engine
- Feedback and explanations
- Score tracking & leaderboard
- Admin login & management
- Persistent score storage
- Responsive/resizable UI

## 2. Game Engine & Tech Stack

- Python 3
- Pygame (for GUI)
- Simple text file for score persistence

## 3. Architecture Diagram
   
-attached in the pdf.

**Modules:**
- main.py: Game flow
- scenarios: List of dicts, logic
- admin: Score viewing/resetting
- utils: Drawing functions

## 4. 3D Objects/Terrain/Scenes

- Not applicable; 2D interface with icons

## 5. Physics

- Not applicable

## 6. AI/Logic

- No enemy AI; decision logic checks answers, gives feedback

## 7. Audio/Visual

- No sound, but supports color feedback and icons for clarity

## 8. Networking

- Not used; local only

## 9. Platform Requirements

- Windows, Mac, Linux
- Python 3, Pygame installed

## Delivery

- .py files, user_scores.txt
- Documentation (this and others)


