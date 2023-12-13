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
