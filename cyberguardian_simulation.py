import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1100, 700
WHITE, BLACK, BLUE, GRAY, GREEN, RED, ORANGE = (
    (255,255,255), (0,0,0), (65,110,215), (240,240,240), (0,200,80), (210,0,40), (255, 165, 0))
FONT = pygame.font.SysFont('arial', 32)
BIG_FONT = pygame.font.SysFont('arial', 60, bold=True)
MED_FONT = pygame.font.SysFont('arial', 40, bold=True)
SMALL_FONT = pygame.font.SysFont('arial', 22)
HEAD_FONT = pygame.font.SysFont('arial', 42, bold=True)

# Load sound files
try:
    SND_CORRECT = pygame.mixer.play("correct.wav")
except:
    SND_CORRECT = None

try:
    SND_WRONG = pygame.mixer.play("wrong.wav")
except:
    SND_WRONG = None

try:
    pygame.mixer.music.load("bg_music.mp3")
except:
    pass

# Explanations for risky answers by scenario id and option index
SECURITY_EXPLANATIONS = {
    # Home WiFi
    (0, 0): "Open WiFi lets anyone connect, putting your network at risk for hacking or misuse.",
    (0, 2): "WEP is outdated and easily cracked. Always use modern security like WPA2.",
    (0, 3): "Sharing passwords reduces security—only trusted people in your home should have access.",
    # Office Computer
    (1, 0): "Delaying updates leaves security holes open for attackers to exploit.",
    (1, 2): "Ignoring updates makes your computer more vulnerable to new viruses.",
    (1, 3): "Only update using official sources. Fake sites may offer malware.",
    # USB Station
    (2, 0): "Unknown USB devices can hide malware that infects your PC instantly.",
    (2, 2): "Plugging unknown devices in any computer spreads the risk!",
    (2, 3): "Leaving a USB could endanger others; always alert IT/security.",
    # Inbox
    (3, 0): "Phishing tries to steal your data. Never click or log in from suspicious emails.",
    (3, 2): "Forwarding phishing emails spreads attacks to others.",
    (3, 3): "Replying can confirm your address to attackers.",
    # Server Room
    (4, 0): "Always notify security as well as checking for ID.",
    (4, 1): "Ignoring a stranger in secure areas is dangerous—always report to security.",
    (4, 3): "Never give computer access to strangers; it risks sensitive data.",
    # Phone Call
    (5, 0): "Never give passwords by phone. Real IT staff never ask this way.",
    (5, 2): "Attackers may keep trying; always report suspicious calls.",
    (5, 3): "Ignoring is not enough. Reporting helps prevent future attacks.",
    # Browser
    (6, 0): "Popups offering urgent downloads are a common malware trick.",
    (6, 2): "Restarting won't remove malware. Always use antivirus.",
    (6, 3): "Scam popups may list fake support numbers. Never call them.",
    # Work Desk
    (7, 0): "Never share your password, even to help a colleague.",
    (7, 2): "Written passwords can be stolen or photographed.",
    (7, 3): "Only IT should assist with access issues securely.",
    # Mobile App
    (8, 1): "Downloading APKs outside official app stores can infect your device.",
    (8, 2): "Delaying updates leaves your device open to attacks.",
    (8, 3): "Uninstall if not needed, but updating is safer and more secure.",
    # Café WiFi
    (9, 0): "Open public WiFi exposes your logins—use a VPN for safety.",
    (9, 2): "Never share your credentials. This can lead to data breaches.",
    (9, 3): "2FA (two-factor authentication) adds a critical layer of protection.",
}

scenarios = [
    {
        'id': 0,
        'place': 'Home WiFi',
        'icon': "",
        'situation': "You are setting up your home WiFi. Which security setting is best?",
        'options': [
            "Open, no password",
            "WPA2-PSK with strong password",
            "WEP with short password",
            "Share password with neighbor"
        ],
        'answer': 1,
        'feedback': [
            "Unsecured WiFi is risky!",
            "Excellent! This keeps your network safe.",
            "WEP is outdated and weak.",
            "Don’t share passwords outside your household."
        ],
        'mastery': "Understanding"
    },
    {
        'id': 1,
        'place': 'Office Computer',
        'icon': "",
        'situation': "Your PC says: Update now or remind later. What do you do?",
        'options': [
            "Click 'Remind me later'",
            "Update now and restart",
            "Ignore and keep working",
            "Search Google for 'updates'"
        ],
        'answer': 1,
        'feedback': [
            "Updates often fix security holes—don't delay.",
            "Correct! Timely updates stop hackers.",
            "Ignoring puts you at risk.",
            "Official updates only—avoid random sites."
        ],
        'mastery': "Applying"
    },
    {
        'id': 2,
        'place': 'USB Station',
        'icon': "",
        'situation': "You find a USB stick in the hallway. What's your move?",
        'options': [
            "Plug into your PC",
            "Hand to IT/security",
            "Plug into friend’s PC",
            "Leave it there"
        ],
        'answer': 1,
        'feedback': [
            "Malware risk! Don’t plug unknown devices.",
            "Correct. IT will check it safely.",
            "Spreads risk to others.",
            "Better to alert security, not just leave."
        ],
        'mastery': "Analyzing"
    },
    {
        'id': 3,
        'place': 'Inbox',
        'icon': "",
        'situation': "You receive: 'Your account locked! Click to unlock.' What do you do?",
        'options': [
            "Click and log in",
            "Check sender and report as phishing",
            "Forward to friends",
            "Reply asking for info"
        ],
        'answer': 1,
        'feedback': [
            "Phishing—never click suspicious links.",
            "Good! Always verify & report.",
            "Don’t spread phishing emails.",
            "Never reply to attackers."
        ],
        'mastery': "Evaluating"
    },
    {
        'id': 4,
        'place': 'Server Room',
        'icon': "",
        'situation': "You see a stranger in the server room. Next step?",
        'options': [
            "Ask for ID",
            "Ignore—they look busy",
            "Tell manager/security",
            "Give access to your computer"
        ],
        'answer': 2,
        'feedback': [
            "Good to check, but also notify security.",
            "Don’t assume—security comes first.",
            "Correct! Always report unauthorized people.",
            "Never give computer access to strangers."
        ],
        'mastery': "Creating"
    },
    {
        'id': 5,
        'place': 'Phone Call',
        'icon': "",
        'situation': "A caller claims to be 'IT' and asks for your password.",
        'options': [
            "Give password over phone",
            "Refuse and report the call",
            "Ask them to call back",
            "Ignore the call"
        ],
        'answer': 1,
        'feedback': [
            "Never share your password by phone.",
            "Excellent. Report social engineering.",
            "They may try to trick again.",
            "Report suspicious calls, don’t just ignore."
        ],
        'mastery': "Applying"
    },
    {
        'id': 6,
        'place': 'Browser',
        'icon': "",
        'situation': "You see a popup: 'PC Infected! Download this now!'",
        'options': [
            "Download software",
            "Ignore & run your antivirus",
            "Restart the PC",
            "Call number on popup"
        ],
        'answer': 1,
        'feedback': [
            "Popups often deliver malware!",
            "Good: Always trust your own tools.",
            "Restart is okay, but scan for threats.",
            "Don’t call scam numbers."
        ],
        'mastery': "Understanding"
    },
    {
        'id': 7,
        'place': 'Work Desk',
        'icon': "",
        'situation': "Colleague asks you to share your password for a 'quick fix.'",
        'options': [
            "Share password to help",
            "Refuse and report",
            "Write on sticky note for them",
            "Tell them to ask IT"
        ],
        'answer': 1,
        'feedback': [
            "Never share passwords, even with coworkers.",
            "Correct! Only IT should help.",
            "Written passwords can leak.",
            "Good, IT can help securely."
        ],
        'mastery': "Analyzing"
    },
    {
        'id': 8,
        'place': 'Mobile App',
        'icon': "",
        'situation': "Your bank app says: 'Update needed' in app store.",
        'options': [
            "Update via app store",
            "Download APK from Google",
            "Ignore for now",
            "Uninstall the app"
        ],
        'answer': 0,
        'feedback': [
            "Correct! Official store only.",
            "Don’t trust random downloads.",
            "Updates patch vulnerabilities.",
            "Uninstall if not needed, but updating is safer."
        ],
        'mastery': "Applying"
    },
    {
        'id': 9,
        'place': 'Café WiFi',
        'icon': "",
        'situation': "You're on public café WiFi. How do you log in to your email?",
        'options': [
            "Just use your email/password",
            "Use VPN, then log in",
            "Share credentials with a friend",
            "Skip 2FA to save time"
        ],
        'answer': 1,
        'feedback': [
            "Open WiFi is dangerous—use VPN.",
            "Correct! VPN encrypts your data.",
            "Never share credentials.",
            "Never skip 2FA!"
        ],
        'mastery': "Evaluating"
    }
]

random.shuffle(scenarios)
ADMIN_PASS = "admin123"
scores_file = "user_scores.txt"

def load_highscores():
    try:
        with open(scores_file, "r") as f:
            return [line.strip().split(',') for line in f.readlines()]
    except:
        return []

def save_highscore(name, score):
    with open(scores_file, "a") as f:
        f.write(f"{name},{score}\n")

def reset_scores():
    open(scores_file, "w").close()

def draw_text(text, x, y, surf, font=FONT, color=BLACK, center=False):
    t = font.render(text, True, color)
    rect = t.get_rect()
    if center: rect.center = (x, y)
    else: rect.topleft = (x, y)
    surf.blit(t, rect)
    return rect

def draw_button(text, x, y, w, h, surf, color=BLUE, active=True, icon=None):
    pygame.draw.rect(surf, color if active else GRAY, (x, y, w, h), border_radius=12)
    if icon:
        t = FONT.render(icon, True, WHITE)
        surf.blit(t, (x+12, y+h//2-t.get_height()//2))
        t2 = FONT.render(text, True, WHITE)
        surf.blit(t2, (x+54, y+h//2-t2.get_height()//2))
    else:
        t = FONT.render(text, True, WHITE)
        rect = t.get_rect(center=(x + w//2, y + h//2))
        surf.blit(t, rect)
    return pygame.Rect(x, y, w, h)

def scenario_scene(idx, user_score, name):
    s = scenarios[idx]
    running = True
    feedback = ""
    chosen = None
    explanation = ""
    while running:
        screen.fill((240, 249, 255))
        pygame.draw.rect(screen, BLUE, (0,0,WIDTH,80))
        draw_text(f"Scenario {idx+1}/{len(scenarios)}: {s['place']} {s['icon']}", WIDTH//2, 32, screen, font=HEAD_FONT, color=WHITE, center=True)
        draw_text(s['situation'], WIDTH//2, 120, screen, font=FONT, color=BLACK, center=True)
        draw_text(f"Mastery: {s['mastery']}", WIDTH//2, 165, screen, font=SMALL_FONT, color=ORANGE, center=True)
        option_rects = []
        for i, opt in enumerate(s['options']):
            rect = draw_button(f"{opt}", WIDTH//2-420, 220+i*70, 840, 58, screen, color=ORANGE if chosen==i else BLUE)
            option_rects.append(rect)
        if feedback:
            pygame.draw.rect(screen, WHITE, (WIDTH//2-340, HEIGHT-180, 680, 80), border_radius=10)
            draw_text(feedback, WIDTH//2, HEIGHT-140, screen, font=MED_FONT, color=GREEN if chosen==s['answer'] else RED, center=True)
            if explanation:
                pygame.draw.rect(screen, (235,255,210), (WIDTH//2-340, HEIGHT-90, 680, 54), border_radius=10)
                draw_text(explanation, WIDTH//2, HEIGHT-65, screen, font=SMALL_FONT, color=BLACK, center=True)
            cont_btn = draw_button("Continue", WIDTH-210, HEIGHT-90, 180, 60, screen, color=GREEN)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not feedback:
                    for i, rect in enumerate(option_rects):
                        if rect.collidepoint(event.pos):
                            feedback = s['feedback'][i]
                            chosen = i
                            if i == s['answer']:
                                user_score += 1
                                explanation = ""
                            else:
                                explanation = SECURITY_EXPLANATIONS.get((s['id'], i), "")
                elif feedback and cont_btn.collidepoint(event.pos):
                    running = False
        pygame.time.wait(18)
    return user_score

def admin_menu():
    pw = ""
    entry = True
    error_msg = ""
    while entry:
        screen.fill((225,235,245))
        draw_text("Admin Login", WIDTH//2, 120, screen, font=HEAD_FONT, color=BLUE, center=True)
        pygame.draw.rect(screen, WHITE, (WIDTH//2-180, 200, 360, 60), border_radius=12)
        draw_text("Password: " + "*"*len(pw), WIDTH//2-160, 215, screen)
        btn = draw_button("Login", WIDTH//2-80, 280, 160, 50, screen)
        if error_msg:
            draw_text(error_msg, WIDTH//2, 350, screen, font=SMALL_FONT, color=RED, center=True)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if pw == ADMIN_PASS: entry = False; error_msg=""
                    else: pw = ""; error_msg="Wrong password!"
                elif event.key == pygame.K_BACKSPACE: pw = pw[:-1]
                else:
                    if len(pw)<16 and event.unicode.isprintable(): pw+=event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN and btn.collidepoint(event.pos):
                if pw == ADMIN_PASS: entry = False; error_msg=""
                else: pw = ""; error_msg="Wrong password!"
        pygame.time.wait(20)
    admin_panel()

def admin_panel():
    show = "scores"
    running = True
    while running:
        screen.fill((240,245,255))
        draw_text("Admin Panel", WIDTH//2, 60, screen, font=HEAD_FONT, color=BLUE, center=True)
        btn_scores = draw_button("View Scores", 80, 140, 200, 54, screen, color=GREEN if show=="scores" else BLUE)
        btn_reset = draw_button("Reset Scores", 80, 210, 200, 54, screen, color=ORANGE)
        btn_quit = draw_button("Main Menu", 80, 280, 200, 54, screen, color=RED)
        if show == "scores":
            draw_text("User High Scores", WIDTH//2+100, 140, screen, font=FONT, color=BLACK)
            scores = load_highscores()
            for i, (name, sc) in enumerate(scores[:15]):
                draw_text(f"{i+1}. {name}: {sc}", WIDTH//2+100, 185 + i*32, screen, font=SMALL_FONT, color=BLACK)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_scores.collidepoint(event.pos): show = "scores"
                elif btn_reset.collidepoint(event.pos): reset_scores()
                elif btn_quit.collidepoint(event.pos): running = False
        pygame.time.wait(20)

def main_menu():
    name = ""
    menu = True
    focus_name = True
    while menu:
        screen.fill((218,238,255))
        draw_text("CyberGuardian: Security Simulation", WIDTH//2, 80, screen, font=BIG_FONT, color=BLUE, center=True)
        btn_obj = draw_button("Learning Objectives", 70, 180, 300, 55, screen, color=BLUE)
        btn_howto = draw_button("How To Play", 70, 255, 300, 55, screen, color=BLUE)

        box_w = 480
        box_h = 60
        box_x = 420
        box_y = 220
        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_w, box_h), border_radius=14)
        label = FONT.render("Enter your name:", True, BLACK)
        label_rect = label.get_rect(midleft=(box_x+24, box_y+box_h//2))
        screen.blit(label, label_rect)
        entry_w = 200
        pygame.draw.rect(screen, GRAY, (box_x+box_w-24-entry_w, box_y+10, entry_w, 40), border_radius=7)
        name_text = FONT.render(name + ("_" if focus_name else ""), True, BLUE)
        name_rect = name_text.get_rect(midleft=(box_x+box_w-24-entry_w+10, box_y+box_h//2))
        screen.blit(name_text, name_rect)

        btn_start = draw_button("Start Simulation", WIDTH//2-140, 320, 280, 54, screen, color=GREEN if len(name)>1 else GRAY)
        btn_admin = draw_button("Admin", WIDTH//2-140, 395, 280, 54, screen, color=ORANGE)
        btn_quit = draw_button("Quit", WIDTH//2-140, 470, 280, 54, screen, color=RED)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                focus_name = True
                if event.key == pygame.K_RETURN and len(name) > 1:
                    simulation(name)
                elif event.key == pygame.K_BACKSPACE: name = name[:-1]
                elif event.key == pygame.K_TAB: focus_name = False
                elif focus_name and len(name) < 18 and event.unicode.isprintable(): name += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.collidepoint(event.pos) and len(name)>1:
                    simulation(name)
                elif btn_admin.collidepoint(event.pos): admin_menu()
                elif btn_obj.collidepoint(event.pos): show_objectives()
                elif btn_howto.collidepoint(event.pos): show_howto()
                elif btn_quit.collidepoint(event.pos): pygame.quit(); sys.exit()
        pygame.time.wait(20)

def show_objectives():
    obj = [
        "Learning Objectives:",
        "- Recognize safe and unsafe digital practices.",
        "- Apply password and email safety in daily life.",
        "- Analyze suspicious situations and choose the safest response.",
        "- Evaluate security risks and act responsibly.",
        "- Create strong, cyber-safe habits!"
    ]
    running = True
    while running:
        screen.fill((210,235,255))
        draw_text("Learning Objectives", WIDTH//2, 80, screen, font=BIG_FONT, color=BLUE, center=True)
        for i, line in enumerate(obj):
            draw_text(line, WIDTH//2, 180+i*55, screen, font=MED_FONT if i==0 else FONT, color=BLACK, center=True)
        btn = draw_button("Back", WIDTH//2-70, HEIGHT-100, 140, 54, screen, color=GREEN)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and btn.collidepoint(event.pos):
                running = False

def show_howto():
    howto = [
        "How To Play:",
        "1. Enter your name and click 'Start Simulation'.",
        "2. Read each scenario, look for clues and icons.",
        "3. Click the safest action/option.",
        "4. Watch for colored feedback and badges.",
        "5. Your score and certificate appear at the end!",
        "6. Try Admin mode to review scores."
    ]
    running = True
    while running:
        screen.fill((240,255,250))
        draw_text("How To Play", WIDTH//2, 80, screen, font=BIG_FONT, color=BLUE, center=True)
        for i, line in enumerate(howto):
            draw_text(line, WIDTH//2, 180+i*48, screen, font=MED_FONT if i==0 else FONT, color=BLACK, center=True)
        btn = draw_button("Back", WIDTH//2-70, HEIGHT-100, 140, 54, screen, color=GREEN)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and btn.collidepoint(event.pos):
                running = False

def simulation(name):
    user_score = 0
    for idx in range(len(scenarios)):
        user_score = scenario_scene(idx, user_score, name)
    save_highscore(name, user_score)
    certificate_screen(name, user_score)

def certificate_screen(name, score):
    running = True
    while running:
        screen.fill((230,255,240))
        draw_text("Simulation Complete!", WIDTH//2, 90, screen, font=BIG_FONT, color=GREEN, center=True)
        draw_text(f"Congratulations, {name}!", WIDTH//2, 180, screen, font=MED_FONT, color=BLACK, center=True)
        draw_text(f"Final Score: {score} / {len(scenarios)}", WIDTH//2, 240, screen, font=FONT, color=BLACK, center=True)
        if score == len(scenarios):
            draw_text("🏆 CYBER GUARDIAN BADGE 🏆", WIDTH//2, 320, screen, font=HEAD_FONT, color=BLUE, center=True)
        elif score >= len(scenarios)*0.8:
            draw_text("🎖️ CYBER SAFE ACHIEVER 🎖️", WIDTH//2, 320, screen, font=MED_FONT, color=ORANGE, center=True)
        else:
            draw_text("Keep learning and try again!", WIDTH//2, 320, screen, font=FONT, color=RED, center=True)
        draw_text("Press [M] for Main Menu or [Q] to Quit", WIDTH//2, 430, screen, font=FONT, color=BLACK, center=True)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: pygame.quit(); sys.exit()
                if event.key == pygame.K_m: return
        pygame.time.wait(20)

if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("CyberGuardian: Security Simulation")
    main_menu()
