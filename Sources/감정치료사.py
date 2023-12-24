from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import os
import load_diary as ld 
import emotion_graph as eg
import emotion_score as ec
import wirte_diary as wd
import user_Info as ui
import emotion_solution as es
import pygame
import sys

#노래 자동 재생
pygame.init()
music_file = "배경음악.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

# 각 날짜별 일기를 담을 리스트
diaries = []

#사용자 정보 입력 받기
IP_user = ui.userInfo()
IP_user.name = input("사용자님의 이름을 입력해주세요: ")
IP_user.filename = input("사용자님의 결과를 출력할 파일 이름을 입력해주세요.(txt): ")
IP_user.day = input("날짜를 입력해주세요(ex.2000년 1월 첫째주): ")


while(1) :
    print("★ 감정 치료사 ★")
    print(f"1. {IP_user.name}님의 일기를 작성해드릴께요\n")
    print(f"2. {IP_user.name}님의 일기를 분석해드릴께요!\n")
    print("3. 음악을 꺼드릴께요!\n")
    print("4. 프로그램을 종료해드릴께요!\n")
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
            day_diary_words = ld.read_diary_word(day_diary)
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

        print(f"\n\n{IP_user.name}님의 이번주 감정 랭킹이에요")
        print(ranked_emotions)
        print()

        #감정 솔루션 함수 호출
        es.provide_solution(IP_user.name, IP_user.filename, ranked_emotions, IP_user.day)
        
        
    if (choice == 3):
        pygame.mixer.music.stop()
        print("음악을 꺼드렸어요!\n")
        continue

    if (choice == 4):
        break

    
    
