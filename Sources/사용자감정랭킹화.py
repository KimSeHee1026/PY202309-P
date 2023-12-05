import 감정리스트

#사용자의 단어에서 감정을 순위별로 나열하는 함수
def word_ranking (words):
    sad_count = 0
    happy_count = 0
    angry_count = 0
    die_count = 0
    
    #사용자 단어에서 감정 리스트를 계산
    for word in words: #사용자 words에서 word를 반복
        for sameword in 감정리스트.sad: #sad리스트에서 하나씩 꺼냄
            if sameword in word:
                sad_count += 1
                
        for sameword in 감정리스트.happy:  # happy 리스트에서 하나씩 꺼냄
            if sameword in word:
                happy_count += 1

        for sameword in 감정리스트.angry:  # angry 리스트에서 하나씩 꺼냄
            if sameword in word:
                angry_count += 1

        for sameword in 감정리스트.die:  # die 리스트에서 하나씩 꺼냄
            if sameword in word:
                die_count += 1
                  
    # 감정 카운트를 딕셔너리에 저장
    emotions = {'Sad' : sad_count, 'Happy' : happy_count, 'Angry' : angry_count, 'Die' : die_count}
    sorted_emotions = sorted(emotions.items(),key=lambda x:x[0])

    return sorted_emotions #반환값 [('Sad', 3), ('Happy', 2), ('Angry', 0), ('Die', 0)]
