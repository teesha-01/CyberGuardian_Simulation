# Game Design Document – CyberGuardian

## Game Overview

CyberGuardian is an educational simulation game designed to reinforce key information security concepts through real-life scenarios. The player must choose the safest action in each situation, with instant feedback and educational explanations.

## Game Mechanics

- **Scenario-Based:** Each round presents a unique, relatable cybersecurity situation.
- **Multiple Choice:** Player selects the best response from 4 options.
- **Instant Feedback:** After each choice, feedback and explanations help the player learn.
- **Scoring:** Players earn points for correct answers. Final score = total correct.
- **Badges:** Top performers earn virtual badges (e.g., "Cyber Guardian").
- **Admin Panel:** Allows viewing and resetting high scores.

## Game Flow

1. **Main Menu:**  
   - Start Simulation (requires entering player name)  
   - View Learning Objectives  
   - How to Play  
   - Admin Login

2. **Simulation:**  
   - Player goes through 10 scenarios.
   - Selects the safest option.
   - Receives feedback and (if incorrect) a short educational explanation.

3. **Certificate/Score:**  
   - Score shown at end.  
   - Badge awarded based on performance.  
   - Option to return to main menu or quit.

4. **Admin Panel:**  
   - View scores  
   - Reset scores

## Art & UI

- Clean, professional layout
- Readable fonts, clear buttons, minimal distractions
- Use of color for feedback (green = correct, red = wrong)
- Icons for scenarios (WiFi, Computer, USB, etc.)

## Scenarios (Examples)

- Setting up home WiFi securely
- Software update prompt
- Handling a suspicious USB stick
- Spotting phishing emails
- Not sharing passwords at work
- Recognizing scam popups
- Safe use of public WiFi

(Full scenario list in code; each maps to a learning outcome and mastery level.)

## Game Characters

- Player (user’s name)
- Admin (teacher or manager, for scorekeeping)

## Menus

- Main menu, scenario screens, certificate/score, admin

## Game View/Scenarios

- All on one main window (resizable)
- Each scenario presented with icon, title, and question
- Multiple-choice answer buttons

## Win/Loss

- No "game over", but performance is scored
- Perfect score = top badge

## Risks, Challenges, and Interaction

- Each scenario requires player analysis and decision-making
- Feedback fosters learning, not just right/wrong

## Future Enhancements

- More scenarios
- Team mode/multiplayer
- Timed challenge rounds
