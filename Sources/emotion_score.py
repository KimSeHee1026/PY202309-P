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

def provide_solution(overall_emotion, threshold=0):
    # 전체 감정 스코어를 기반으로 솔루션을 제공하는 함수
    negative_emotion_score = overall_emotion.get('neg', 0)
    
    if negative_emotion_score > threshold:
        # 부정적인 감정이 특정 기준 이상인 경우 부정적인 솔루션 제공
        return provide_negative_solution()
    else:
        # 그 외의 경우 일반적인 긍정적인 솔루션 제공
        return "이번 주는 특별한 어려움이 없었나봐요. 좋은 소식을 기대하고 있어요."

def provide_negative_solution():
    # 부정적인 감정에 대한 솔루션을 제공하는 함수
    solutions = {
        'pos': '이번 주는 특히 긍정적이었군요! 자세한 내용을 기대하고 있어요.',
        'neu': '이번 주는 차분한 주간이었군요. 더 나은 다음 주를 기대해봐요.',
        'neg': '이번 주는 어려움이 있었던 것 같아요. 힘들었던 일을 얘기해보는 것도 좋겠어요.',
        'compound': '이번 주의 종합 감정은 상당히 강렬한 것으로 보여요. 자세한 이야기를 들려주세요.'
    }

    top_emotion = 'neg'  # 부정적인 감정이 높은 경우
    solution = solutions.get(top_emotion, "이번 주 감정을 더 자세히 들려주세요.")
    return solution
