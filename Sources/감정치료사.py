from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import os
import load_diary as ld 
import emotion_graph as eg
import emotion_score as ec
import wirte_diary as wd

# 각 날짜별 일기를 담을 리스트
diaries = []


while(1) :
    print("★감정 치료사★")
    print("1. 일기를 쓸래!\n")
    print("2. 내 일기를 분석해줘!\n")
    print("3. 음악을 꺼줘!\n")
    print("4. 프로그램을 종료해줘!\n")
    choice = int(input("사용 할 기능을 선택해주세요: "))

    if (choice == 1):
        wd.write_diary()
    if (choice == 2):
        print("일기를 입력해주세요!\n")
        diaries = ld.diary_input()

        print(" . . . 감정을 분석중입니다.\n")
        # 전체 주간 감정 분석 수행
        weekly_emotions = []
        for day_diary in diaries:
            day_diary_words = ec.read_diary_word(day_diary)
            day_diary_text = ' '.join(day_diary_words)
            day_emotion = ec.analyze_sentiment(day_diary_text)
            weekly_emotions.append(day_emotion)

        print(" . . . 그래프를 분석중입니다.\n")
        save_path = input("그래프 이미지를 출력할 파일 이름을 입력해주세요(.png포함): \n")
        eg.plot_weekly_sentiment_scores(weekly_emotions, save_path)
         

        # 감정 랭킹화
        overall_emotion = {}

        for day_emotion in weekly_emotions:
            for key, value in day_emotion.items():
                overall_emotion[key] = overall_emotion.get(key, 0) + value

        ranked_emotions = ec.rank_emotions(overall_emotion)

        print("\n사용자님의 이번주 감정 랭킹:")
        print(ranked_emotions)
        

        # 상위 감정에 대한 솔루션 제공 (부정적인 감정이 특정 기준 이상인 경우에만)
        threshold_for_solution = 0.5 #부정적 솔루션 기준(50% 이상)
        solution = ec.provide_solution(overall_emotion, threshold_for_solution)
        print(f"\n상위 감정에 대한 솔루션:\n{solution}")
    if (choice == 3):
        pass
    if (choice == 4):
        break

    
    
