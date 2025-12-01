# 🧬 BIO-INSPIRED MICRO-MOBILITY: Autonomous Pod
### High-Speed Adaptive Navigation & Affective HRI on Edge Platforms

![Python](https://img.shields.io/badge/Python-3.9%7C3.10-blue)
![Framework](https://img.shields.io/badge/Framework-DonkeyCar_v5-green)
![RL Algorithm](https://img.shields.io/badge/RL-PPO_%2F_MobileNet-orange)
![Sim-to-Real](https://img.shields.io/badge/Sim--to--Real-Ready-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> **Research Project:** Development of a resource-constrained autonomous navigation system combining F1-style control, social robotics (WALL-E style), and generative design.

---

## 📖 Abstract

This project addresses the trade-off between **speed** and **passenger comfort** in modern service robots. We propose **"Mini Cyber-Rickshaw"**, a micro-scale (1:28) autonomous architecture that leverages **End-to-End Deep Reinforcement Learning** to achieve high-speed navigation while maintaining social compliance. The system is designed to operate on low-cost edge devices (Raspberry Pi Zero 2 W) using a Sim-to-Real transfer pipeline.

**Key Research Question:** *Can we deploy F1-grade racing algorithms on a $15 computer to serve smart city tourism?*

## 🌟 Key Features

### 1. 🏎️ F1-Inspired Navigation (The Brain)
* **Algorithm:** Proximal Policy Optimization (PPO) with MobileNetV3 backbone.
* **Behavior:** Optimized for **Apex Clipping** (cutting corners) and dynamic velocity control based on track curvature.
* **Reward Function:** Custom multi-objective function balancing *Velocity*, *Cross-Track Error*, and *Jerk* (smoothness).

### 2. 🤖 Active Perception & HRI (The Soul)
* **Active Vision:** Pan-Tilt camera mechanism (2-DOF) simulating saccadic eye movements to expand Field of View (FoV) at intersections.
* **Affective Locomotion:** State-machine based behaviors expressing internal states (e.g., *Curiosity* at landmarks, *Fear* at obstacles).

### 3. 🦴 Generative Bio-Chassis (The Body)
* **Design:** Voronoi lattice structure generated via Topology Optimization (Fusion 360).
* **Performance:** 40% weight reduction compared to stock chassis, maintaining structural integrity for high-speed impacts.

---

## 🛠️ System Architecture

| Component | Specification |
| :--- | :--- |
| **Platform** | WLToys K989 (1:28 Scale RC Car) |
| **Compute** | Raspberry Pi Zero 2 W (Quad-core ARM Cortex-A53) |
| **Sensors** | Pi Camera V2 (160° FoV) |
| **Actuation** | PCA9685 PWM Driver + SG90 Servos (Head) |
| **Simulation** | Unity 3D / Donkey Car Simulator |

---

## 🚀 Installation & Setup

### 1. Prerequisites
* Anaconda or Miniconda
* Python 3.9+
* NVIDIA GPU (Recommended for training)

### 2. Environment Setup
```bash
# Clone the repository
git clone [https://github.com/YourUsername/mini-cyber-rickshaw.git](https://github.com/YourUsername/mini-cyber-rickshaw.git)
cd mini-cyber-rickshaw

# Create Conda environment
conda create -n donkey python=3.9 -y
conda activate donkey

# Install dependencies
pip install -e .[pc]
pip install -r requirements.txt
```

### 3\. Launch Simulator (Sim Mode)

Ensure `myconfig.py` is configured with `DONKEY_GYM = True`.

```bash
python manage.py drive
```

Access the web controller at: `http://localhost:8887`

-----

## 🧠 Training Pipeline (Sim-to-Real)

We utilize a **Behavioral Cloning** approach augmented with **DRL**:

1.  **Data Collection:** Drive manually in the Simulator to generate \~10,000 samples.
2.  **Training:**
    ```bash
    donkey train --tub ./data --model ./models/mypilot.h5
    ```
3.  **Deploy:** Transfer the `.h5` model to Raspberry Pi Zero.
4.  **Inference:**
    ```bash
    python manage.py drive --model ./models/mypilot.h5
    ```

-----

## 📂 Project Structure

```text
mini-cyber-rickshaw/
├── data/               # Raw training data (Git ignored)
├── docs/               # Research papers and diagrams
├── models/             # Trained Neural Networks
├── src/                # Custom source code (RL agents, Vision)
├── manage.py           # Main entry point
└── myconfig.py         # Configuration file
```

-----

## 📊 Preliminary Results

*(Placeholders - Update with your real charts)*

  * **Lap Time:** Reduced by 15% compared to PID controller.
  * **Inference Speed:** 22 FPS on Raspberry Pi Zero 2 W.
  * **Smoothness:** Jerk metric reduced by 30% using the proposed Reward Function.

-----

## 👨‍💻 Author

  * **NGUYEN MINH QUANG**
  * Researcher
  * University of Science - VNU
  * Email: minhquang04072005@gmail.com

## 🤝 Acknowledgments

Special thanks to the **Donkey Car Community** and **Stable Baselines3** team for the open-source tools.

