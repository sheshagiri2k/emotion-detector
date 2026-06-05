from .emotion_detection import emotion_detector
EmotionDetector/ (Root folder)
│
├── EmotionDetection/       # Package folder
│   ├── __init__.py         # <--- Save this file here
│   └── emotion_detection.py
│
└── server.py
# Instead of: from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection import emotion_detector
