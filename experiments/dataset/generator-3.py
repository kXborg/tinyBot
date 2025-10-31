import csv
import random

rooms = ["living_room", "bedroom", "bathroom", "kitchen", "balcony", "garage", "office"]
times = ["morning", "afternoon", "evening", "night"]

devices = [
    "fan", "light", "curtain", "door", "window", "refrigerator", "geyser",
    "ac", "heater", "humidifier", "dehumidifier", "air_purifier",
    "tv", "music_system", "cctv_camera", "aquarium_pump",
    "coffee_maker", "water_motor", "desk_lamp", "phone_charger"
]

voice_templates = [
    "turn on the {}", "turn off the {}", "switch on the {}", "switch off the {}",
    "activate the {}", "deactivate the {}", "start the {}", "stop the {}",
    "is the {} on", "is the {} off", "open the {}", "close the {}",
    "how’s the {}", "check the {}", "status of the {}", "what’s up with the {}"
]

def generate_sample():
    temp = round(random.uniform(15, 40), 2)
    humidity = round(random.uniform(20, 90), 2)
    light_intensity = round(random.uniform(5, 100), 2)
    noise = round(random.uniform(10, 80), 2)
    pir_motion = random.choice([0, 1])
    person_count = random.choice([0, 1, 2, 3])
    door_state = random.choice(["open", "closed"])
    window_state = random.choice(["open", "closed"])
    co2 = round(random.uniform(400, 2000), 2)
    gas_leak = random.choice([0, 1])
    smoke_detected = random.choice([0, 1])
    rain_detected = random.choice([0, 1])
    room = random.choice(rooms)
    time = random.choice(times)
    device = random.choice(devices)
    command = random.choice(voice_templates).format(device)

    # State logic
    if any(word in command for word in ["off", "deactivate", "stop", "close"]):
        state = "OFF"
    else:
        state = "ON"

    return [
        temp, humidity, light_intensity, noise, pir_motion, person_count,
        door_state, window_state, co2, gas_leak, smoke_detected, rain_detected,
        command, room, time, device, state
    ]

# Generate dataset
rows = [generate_sample() for _ in range(5000)]

with open("smart_home_dataset_v3.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "temperature","humidity","light_intensity","noise_level",
        "pir_motion","person_count","door_state","window_state",
        "co2_level","gas_leak","smoke_detected","rain_detected",
        "voice_command","room_type","time_of_day","device","state"
    ])
    writer.writerows(rows)

print("smart_home_dataset.csv generated successfully with", len(rows), "samples.")
