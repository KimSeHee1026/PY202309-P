#감정 구별 리스트(알고리즘을 통해 더 추가해야하지 않을까?)
sad = ['슬프다', '슬픔', '우울', '슬픈']
happy = ['행복','좋았','기쁜','기쁘','좋던','좋아']
angry = ['화나','화난','화났','화가났']
die = ['죽고싶','죽다','죽은','죽었','죽음']

#사용자의 일기를 불러오는 함수
def load_diary_from_file(filename):
    diary_list = []
    read_fp = open(filename, 'r', encoding="utf8")
    lines = read_fp.readlines()
    for line in lines:
        diary_list.append(line.strip())
    return diary_list

#사용자에 일기를 한줄로 붙여주는 함수
def read_diary_word(list):
    diary_sentence = ''
    for sentence in list:
        diary_sentence += sentence
    diary_word = diary_sentence.replace('.', '').split()
    return diary_word

#사용자의 단어에서 감정을 순위별로 나열하는 함수
def word_calculate (words):
    sad_count = 0
    happy_count = 0
    angry_count = 0
    die_count = 0
    
    #사용자 단어에서 감정 리스트를 계산
    for word in words: #사용자 words에서 word를 반복
        for sameword in sad: #sad리스트에서 하나씩 꺼냄
            if sameword in word:
                sad_count += 1
                
        for sameword in happy:  # happy 리스트에서 하나씩 꺼냄
            if sameword in word:
                happy_count += 1

        for sameword in angry:  # angry 리스트에서 하나씩 꺼냄
            if sameword in word:
                angry_count += 1

        for sameword in die:  # die 리스트에서 하나씩 꺼냄
            if sameword in word:
                die_count += 1
                  
    # 감정 카운트를 딕셔너리에 저장
    emotions = [('Sad', sad_count), ('Happy', happy_count), ('Angry', angry_count), ('Die', die_count)]
    sorted_emotions = sorted(emotions, key=lambda x: x[1], reverse=True)

    return sorted_emotions #반환값 [('Sad', 3), ('Happy', 2), ('Angry', 0), ('Die', 0)]

    
#나열된 감정들 중 높은 순위의 해결법을 출력해주는 함수(사용자 결과.txt로 파일 출력)
def solution (word_calculate):
    sorted_emotions = sorted(word_calculate, key=lambda x: x[1], reverse =True)
    highest_emotion = sorted_emotions[0][0]
    print(f"제일 높은 감정은: {highest_emotion}이에요")
    
    


filename = input("전체를 전부 입력하세요 (txt포함)") #사용자의 일기를 단어로 분리하는 함수
diary_list = load_diary_from_file(filename) #사용자 일기를 불러옴
diary_word = read_diary_word(diary_list) # 사용자 일기를 단어별로 나누는 함수
word_calculate(diary_word)