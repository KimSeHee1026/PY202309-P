import matplotlib.pyplot as plt
import os

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