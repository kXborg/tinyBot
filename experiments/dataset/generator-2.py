import random
import pandas as pd

# Possible categorical values
voice_commands = [
    "I am home", "I am leaving", "good night", "good morning",
    "turn on the light", "turn off the fan", "it's hot",
    "open the window", "close the door", "start the geyser", "turn off everything"
]
rooms = ["bedroom", "living_room", "kitchen", "bathroom"]
times = ["morning", "afternoon", "evening", "night"]
devices = ["light", "fan", "ac", "geyser", "door", "window", "camera"]
states = ["ON", "OFF", "STANDBY", "LOCKED", "UNLOCKED"]

def generate_sample():
    # --- Sensor inputs ---
    temp = random.uniform(16, 40)
    humidity = random.uniform(20, 90)
    light_intensity = random.uniform(0, 100)
    noise = random.uniform(10, 90)
    pir = random.choice([0, 1])
    ultrasonic = random.uniform(10, 300)  # cm
    person_count = random.randint(0, 3)
    door = random.choice(["open", "closed"])
    window = random.choice(["open", "closed"])
    co2 = random.uniform(300, 2000)       # ppm
    gas_leak = random.choice([0, 1])
    smoke_detected = random.choice([0, 1])
    rain_detected = random.choice([0, 1])
    energy_usage = random.uniform(0, 2000)  # watts
    voice = random.choice(voice_commands)
    room = random.choice(rooms)
    time = random.choice(times)

    # --- Intelligent rule-based logic for outputs ---
    device, state = None, None

    # Safety and emergencies have highest priority
    if gas_leak or smoke_detected:
        device, state = "fan", "ON"  # ventilation
    elif rain_detected and window == "open":
        device, state = "window", "CLOSE"
    elif co2 > 1200 and room != "kitchen":
        device, state = "window", "OPEN"
    # Environmental comfort
    elif temp > 30 or "hot" in voice:
        device, state = "ac", "ON"
    elif temp < 20 and "bedroom" in room:
        device, state = "geyser", "ON"
    # Lighting and presence
    elif "good night" in voice or time == "night":
        device, state = "light", "OFF"
    elif "good morning" in voice or (light_intensity < 30 and pir):
        device, state = "light", "ON"
    # Presence / absence logic
    elif "leaving" in voice or person_count == 0:
        device, state = "light", "OFF"
    elif "home" in voice or pir:
        device, state = "light", "ON"
    # Energy optimization
    elif energy_usage > 1500 and not pir:
        device, state = "fan", "OFF"
    else:
        device, state = random.choice(devices), random.choice(states)

    return {
        "temperature": round(temp, 2),
        "humidity": round(humidity, 2),
        "light_intensity": round(light_intensity, 2),
        "noise_level": round(noise, 2),
        "pir_motion": pir,
        "ultrasonic_distance": round(ultrasonic, 2),
        "person_count": person_count,
        "door_state": door,
        "window_state": window,
        "co2_level": round(co2, 2),
        "gas_leak": gas_leak,
        "smoke_detected": smoke_detected,
        "rain_detected": rain_detected,
        "energy_usage": round(energy_usage, 2),
        "voice_command": voice,
        "room_type": room,
        "time_of_day": time,
        "device": device,
        "state": state
    }

def generate_dataset(n=5000):
    data = [generate_sample() for _ in range(n)]
    df = pd.DataFrame(data)
    df.to_csv("smart_home_dataset_v2.csv", index=False)
    print(f"Generated {n} samples and saved as smart_home_dataset_v2.csv")

if __name__ == "__main__":
    generate_dataset(1000)
