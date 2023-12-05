#파일 불러오기
def load_diary_from_file(filename):
    diary_list = []
    read_fp = open(filename, 'r', encoding="utf8")
    lines = read_fp.readlines()
    for line in lines:
        diary_list.append(line.strip())
    return diary_list 

#단어로 정리하기
def read_diary_word(list):
    diary_sentence = ''
    for sentence in list:
        diary_sentence += sentence
    diary_word = diary_sentence.replace('.', '').split()
    return diary_word

