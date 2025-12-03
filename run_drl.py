import os
import gym
import gym_donkeycar
from stable_baselines3 import PPO
import numpy as np

        
MODEL_PATH = "./models/ppo/ppo_f1_racer_final.zip"

TEST_MAP = "donkey-generated-track-v0"


CONF = { 
    "exe_path": "D:/CODE/PythonProject/donkeycar/DonkeySimWin/donkey_sim.exe", 
    "port": 9091,
    "body_style": "donkey",
    "body_rgb": [255, 0, 0], 
    "car_name": "F1_Champion",
    "font_size": 100
}

# ====================================================
# MAIN RUN LOOP
# ====================================================
if __name__ == "__main__":
    
    if not os.path.exists(MODEL_PATH):
            print("ERROR: NOT FOUND MODEL PATH.")
            exit()  
    print(f"FOUNDED MODEL AT {MODEL_PATH}")
    print(f"LOADING MODEL...")
    
    model = PPO.load(MODEL_PATH, device="cuda")
    print("LOADING SUCCCESFULLY!!!")

    print(f"CONNECTING WITH ENV: {TEST_MAP}...")
    env = gym.make(TEST_MAP, conf=CONF)
    
    obs = env.reset()
    print("CAR IS START DRIVING")

    try:
        while True:
            action, _states = model.predict(obs, deterministic=True)
            
            obs, reward, done, info = env.step(action)
            
            print(f"Steer: {action[0]:.2f} | Throttle: {action[1]:.2f} | Speed: {info.get('speed', 0):.2f}")

            if done:
                print("OVERTIME OR CRASH! Resetting...")
                obs = env.reset()

    except KeyboardInterrupt:
        print("\n IT IS STOPPED.")
    finally:
        env.close()