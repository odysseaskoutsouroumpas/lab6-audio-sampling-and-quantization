# lab6-audio-sampling-and-quantization

This repository demonstrates **digital signal processing (DSP)** techniques applied to real audio. Specifically, it focuses on **sampling (downsampling)** and **quantization**, which are fundamental steps in converting analog signals (like sound) into digital form for computers.

It is part of a larger educational project about RADAR and LIDAR signal processing in Python.

---

## 🔍 What is this lab about?

In simple terms:

- **Sampling** is like taking snapshots of a sound at specific intervals (like taking 1 photo per second).
- **Downsampling** means taking fewer snapshots, which saves space but may lose quality.
- **Quantization** means rounding each snapshot to the nearest allowed value (like turning a detailed drawing into pixel art).

This lab includes real audio examples (`.wav` files) to help you understand how these processes affect the sound.

---

## 📁 Contents

This repository contains:

- Python scripts (`.py`) that perform sampling, downsampling, and quantization on real sound.
- Original `.wav` audio files.
- Modified `.wav` audio files (with reduced quality, lower resolution, etc.)
- Scripts to load, modify, and save audio.

---

## 📦 Requirements – What you need to run this

You need to have **Python 3.8 or later** installed.

Then, install the required Python libraries:

```bash
pip install numpy scipy matplotlib soundfile
