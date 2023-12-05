import 감정리스트


#나열된 감정들 중 높은 순위의 해결법을 출력해주는 함수(사용자 결과.txt로 파일 출력)
def solution (word_calculate):
    sorted_emotions = sorted(word_calculate, key=lambda x: x[1], reverse =True)
    highest_emotion = sorted_emotions[0][0]
    second_highest_emotion = sorted_emotions[1][0]

    print(f"제일 높은 감정은: {highest_emotion}이에요")
    print(f"두번째로 높은 감정은: {second_highest_emotion}이에요")

    if (highest_emotion == 'Happy'):
        print("정말 행복한 하루를 보내고 계시네요!")
        

