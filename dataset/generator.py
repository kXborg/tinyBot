import csv, random, itertools, os

# Output file
OUTPUT_FILE = "tiny_chat_dataset_large.csv"

# Core vocabulary
devices = [
    "fan", "light", "dim light", "curtain", "door sensor", "refrigerator",
    "phone charger", "aquarium filter", "hydroponic farm motor", "cctv camera"
]

actions_on = [
    "turn on", "switch on", "activate", "enable", "power on", "start"
]

actions_off = [
    "turn off", "switch off", "deactivate", "disable", "power down", "stop"
]

status_queries = [
    "is the {device} on", "what is the status of the {device}",
    "check the {device}", "how’s the {device}", "is {device} working"
]

greetings = [
    "hi", "hello", "hey", "good morning", "good evening",
    "what’s up", "how are you", "yo", "greetings", "hi tinybot"
]

farewells = [
    "bye", "see you", "talk later", "good night", "see you soon",
    "catch you later", "bye tinybot"
]

smalltalk = [
    ("what’s your name", "i’m tinybot, your smart home friend."),
    ("how are you", "doing great! just monitoring your devices."),
    ("tell me a joke", "why did the robot smile? because it rebooted!"),
    ("what can you do", "i can help you control your smart home devices."),
    ("who made you", "i was created to make your home smarter!"),
    ("what time is it", "it’s always time to automate something!"),
    ("you are smart", "thank you! i’m learning every day."),
    ("you are dumb", "i’m still learning, but thanks for the feedback!")
]

confirmations = [
    "okay", "sure", "done", "got it", "on it", "working on it",
    "your command has been executed", "as you wish"
]

acknowledgements = [
    "yes", "no", "maybe", "not sure", "let me check", "please repeat that"
]

# Utility: make random reply
def make_reply(action, device):
    if action in actions_on:
        return random.choice(["okay turning on the {device}.", "sure! activating the {device}.", "done, {device} is now on."]).format(device=device)
    elif action in actions_off:
        return random.choice(["turning off the {device}.", "done, {device} is off.", "okay, deactivating the {device}."]).format(device=device)
    else:
        return f"i’ll check the {device} status."

# Generate data
rows = []

# Generate control commands
for device, action in itertools.product(devices, actions_on + actions_off):
    for _ in range(random.randint(5, 15)):  # multiple paraphrases
        input_text = f"{action} the {device}"
        reply_text = make_reply(action, device)
        rows.append((input_text, reply_text))

# Generate status queries
for device in devices:
    for template in status_queries:
        input_text = template.format(device=device)
        reply_text = random.choice([
            f"the {device} is currently on.",
            f"the {device} is currently off.",
            f"checking {device} status...",
            f"it seems the {device} is working fine."
        ])
        rows.append((input_text, reply_text))

# Add greetings and farewells
for g in greetings:
    rows.append((g, random.choice([
        "hey there!", "hi!", "hello!", "hi, i’m tinybot!", "nice to see you!"
    ])))

for f in farewells:
    rows.append((f, random.choice([
        "bye!", "see you soon!", "take care!", "goodbye!", "talk later!"
    ])))

# Add smalltalk
rows.extend(smalltalk)

# Random confirmations
for _ in range(100):
    rows.append((
        random.choice(["thanks", "thank you", "appreciate it"]),
        random.choice(["you’re welcome!", "no problem!", "happy to help!", "anytime!"])
    ))

# Random filler lines to reach ~1 MB
while len(rows) < 18000:
    device = random.choice(devices)
    action = random.choice(actions_on + actions_off)
    rows.append((f"{action} the {device}", make_reply(action, device)))

# Shuffle
random.shuffle(rows)

# Write CSV
with open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["input_text", "reply_text"])
    writer.writerows(rows)

print(f"✅ Dataset generated: {OUTPUT_FILE} ({len(rows)} rows, approx {os.path.getsize(OUTPUT_FILE)/1024:.1f} KB)")
