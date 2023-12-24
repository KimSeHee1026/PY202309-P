def diary_input():
    diaries = []
    days_of_week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    for day in days_of_week:
        while True:
            filename = input(f"{day}의 일기 파일 (txt 포함): ")
            diary = load_diary_from_file(filename)
            if diary:
                diaries.append(diary)
                break
    print(diaries)
    return diaries

def load_diary_from_file(filename):
    while True:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                diary = file.read()
            return diary
        except FileNotFoundError:
            print(f"Error: {filename}을(를) 찾을 수 없습니다. 다시 입력해주세요.")
            filename = input("새로운 파일명을 입력하세요: ")
        except Exception as e:
            print(f"Error: {e}")
            exit()

def read_diary_word(diary):
    # 일기 텍스트를 단어로 분리하여 리스트로 반환하는 함수
    words = diary.split()
    return words