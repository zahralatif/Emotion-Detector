"""
Flask server for Emotion Detection application.
This module sets up the web server and defines the routing endpoints.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Bu funksiya '/emotionDetector' endpointi üçün müraciətləri qəbul edir.
    İstifadəçidən gələn mətni alır, emotion_detector funksiyasına ötürür və
    nəticəni formatlı şəkildə qaytarır.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    
    # Xəta (boş input) yoxlanışı
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Əsas səhifəni (index.html) render edir.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
