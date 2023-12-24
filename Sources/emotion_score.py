from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    # 입력된 텍스트에 대한 감정 분석을 수행하는 함수
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

def rank_emotions(emotion_scores):
    # 감정 스코어를 랭킹화하여 딕셔너리로 반환하는 함수
    ranked_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
    return dict(ranked_emotions)


