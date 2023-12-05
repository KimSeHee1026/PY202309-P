import 사용자일기정리 
import 사용자감정랭킹화 
import 솔루션 
import 감정리스트

#사용자 일기 정리
filename = input("전체를 전부 입력하세요 (txt포함)") #사용자의 일기를 단어로 분리하는 함수
diary_list = 사용자일기정리.load_diary_from_file(filename) #사용자 일기를 불러옴
diary_word = 사용자일기정리.read_diary_word(diary_list) # 사용자 일기를 단어별로 나누는 함수

emotion_rank = 사용자감정랭킹화.word_ranking(diary_word)
solution_emotion = 솔루션.solution(emotion_rank)

    
