from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import os

def analyze_sentiment(text):
    # 입력된 텍스트에 대한 감정 분석을 수행하는 함수
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

def load_diary_from_file(filename):
    try:
        # 파일을 읽어와서 일기 텍스트를 반환하는 함수
        with open(filename, 'r', encoding='utf-8') as file:
            diary = file.read()
        return diary
    except FileNotFoundError:
        print(f"Error: {filename}을(를) 찾을 수 없습니다. 프로그램을 종료합니다.")
        exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()

def read_diary_word(diary):
    # 일기 텍스트를 단어로 분리하여 리스트로 반환하는 함수
    words = diary.split()
    return words

def plot_weekly_sentiment_scores(weekly_emotions, save_path=None):
    # 주간 감정 스코어를 그래프로 시각화하는 함수
    labels = list(weekly_emotions[0].keys())  # 모든 날이 동일한 감정 카테고리를 가진다고 가정
    x_labels = ['월', '화', '수', '목', '금', '토', '일']
    x = list(range(len(x_labels)))

    for label in labels:
        values = [day[label] for day in weekly_emotions]
        plt.plot(x, values, label=label)

    plt.title('주간 감정 변화')
    plt.xlabel('요일')
    plt.xticks(x, x_labels)  # x 레이블을 요일로 변경
    plt.ylabel('점수')
    plt.legend()

    if save_path:
        # 그래프를 이미지 파일로 저장하는 함수 호출
        save_graph(save_path)
    else:
        plt.show()

def save_graph(save_path):
    try:
        # 이미지 파일로 그래프 저장
        plt.savefig(save_path, format='png', bbox_inches='tight')
        print(f"그래프가 {save_path}에 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"Error: {e}")

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

# 각 날짜별 일기를 담을 리스트
diaries = []

# 요일별로 일기 파일 이름 입력 받기
days_of_week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
for day in days_of_week:
    while True:
        filename = input(f"{day}의 일기 파일 (txt 포함): ")
        diary = load_diary_from_file(filename)
        if diary:
            diaries.append(diary)
            break

# 전체 주간 감정 분석 수행
weekly_emotions = []
for day_diary in diaries:
    day_diary_words = read_diary_word(day_diary)
    day_diary_text = ' '.join(day_diary_words)
    day_emotion = analyze_sentiment(day_diary_text)
    weekly_emotions.append(day_emotion)

# 주간 감정 스코어 선 그래프로 시각화 및 저장
save_path = "Weeks_emotion.png"
plot_weekly_sentiment_scores(weekly_emotions, save_path)

# 감정 랭킹화
overall_emotion = {}
for day_emotion in weekly_emotions:
    for key, value in day_emotion.items():
        overall_emotion[key] = overall_emotion.get(key, 0) + value

ranked_emotions = rank_emotions(overall_emotion)
print("\n감정 랭킹:")
print(ranked_emotions)

# 상위 감정에 대한

#솔루션 제공 (부정적인 감정이 특정 기준 이상인 경우에만)
threshold_for_solution = 0.5  # 사용자가 설정할 수 있는 임계값 (반 이상)
solution = provide_solution(overall_emotion, threshold_for_solution)
print(f"\n상위 감정에 대한 솔루션:\n{solution}")


