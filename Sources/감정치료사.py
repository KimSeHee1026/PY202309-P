from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import os
import load_diary as ld 
import emotion_graph as eg
import emotion_score as ec


# 각 날짜별 일기를 담을 리스트
diaries = []

# 요일별로 일기 파일 이름 입력 받기
days_of_week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
for day in days_of_week:
    while True:
        filename = input(f"{day}의 일기 파일 (txt 포함): ")
        diary = ld.load_diary_from_file(filename)
        if diary:
            diaries.append(diary)
            break

# 전체 주간 감정 분석 수행
weekly_emotions = []
for day_diary in diaries:
    day_diary_words = ld.read_diary_word(day_diary)
    day_diary_text = ' '.join(day_diary_words)
    day_emotion = ec.analyze_sentiment(day_diary_text)
    weekly_emotions.append(day_emotion)

# 주간 감정 스코어 선 그래프로 시각화 및 저장
save_path = "Weeks_emotion.png"
eg.plot_weekly_sentiment_scores(weekly_emotions, save_path)

# 감정 랭킹화
overall_emotion = {}
for day_emotion in weekly_emotions:
    for key, value in day_emotion.items():
        overall_emotion[key] = overall_emotion.get(key, 0) + value

ranked_emotions = ec.rank_emotions(overall_emotion)
print("\n감정 랭킹:")
print(ranked_emotions)

# 상위 감정에 대한 솔루션 제공 (부정적인 감정이 특정 기준 이상인 경우에만)
threshold_for_solution = 0.5 #부정적 솔루션 기준(50% 이상)
solution = ec.provide_solution(overall_emotion, threshold_for_solution)
print(f"\n상위 감정에 대한 솔루션:\n{solution}")


