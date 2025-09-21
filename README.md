# Motion Detector

This project demonstrates a simple **motion detection** system using **OpenCV** and the **MOG2 background subtraction** algorithm. The script can process either a local video file or a live webcam feed.

## How It Works

The core of this program is the `BackgroundSubtractorMOG2` class from OpenCV. It works by creating a model of the static background of a scene. When a new frame arrives, the model compares it to the background. Any significant differences—which are typically caused by moving objects—are identified and appear as white pixels in a resulting **mask**. This mask visually represents the motion in the video.

The code attempts to open a video file first. If it can't, it automatically falls back to using the system's default camera.

## Prerequisites

- Python 3.x
- OpenCV (specifically the `opencv-python` or `opencv-contrib-python` package)

To install the required library, run the following command:

```bash
pip install opencv-contrib-python
