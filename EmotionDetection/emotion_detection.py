import requests
import json

def emotion_detector(text_to_analyse):
    """
    Watson NLP istifadə edərək verilmiş mətnin emosiyasını analiz edir
    və nəticəni tələb olunan formatda qaytarır.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Əgər status kodu 400 olarsa (boş mətn daxil edilibsə)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # API-dən gələn cavabı JSON formatına çeviririk
    formatted_response = json.loads(response.text)
    
    # Emosiyaları çıxarırıq
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Ən dominant (ən yüksək xalı olan) emosiyanı tapırıq
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Tələb olunan formatda lüğət (dictionary) qaytarırıq
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result
