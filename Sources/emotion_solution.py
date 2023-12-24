#{'neu': 4.793, 'pos': 1.4209999999999998, 'compound': 1.3794000000000002, 'neg': 0.784}

def provide_solution(username, filename, rank_emotion,day):
    rank = list(rank_emotion.keys())

    fp = open(filename, "a", encoding="utf8")
    fp.write(f"{day} {username}의 감정 치료사 정리")
    fp.write(f"{username}의 이번 주 감정 랭킹\n{rank_emotion}")
    fp.write("\n")

    if rank[0] == 'neu':
        data = f"""{username}님은 나쁘지 않은 한 주를 보내고 계시군요! \n좋아요! 더욱 좋은 한 주를 위해 책을 읽어보거나 조금 더 건강한 나를 위해 운동을 해보는건 어때요?"""
        print(data)
        fp.write(data)
        fp.close()
    elif rank[0] == 'pos':
        data = f"""{username}님은 한 주를 굉장히 멋지게 보내고 계시네요!\n좋아요! 이번 주 너무 고생 많으셨어요! 우리 함께 다음 주도 힘내봐요!"""
        print(data)
        fp.write(data)
        fp.close()
    elif rank[0] == 'compound':
        data = f"""{username}님은 이번 주 복잡한 하루를 보내셨군요\n하루하루가 굉장히 생각이 많고 착잡했겠어요.....\n복잡한 하루를 위해 결과 파일에 복잡함으로 가득한 하루를 해결하기 좋은 방안들을\n정리해서 올려드릴께요!"""
        print(data)
        fp.write(f"{username}님의 복잡한 하루를 정리해 줄 해결 List\n")
        fp.write("""1. 일기를 통해 나의 감정과 원인 찾기\n2. 좋아하는 음식을 먹어보며 기분 전환시키기\n3. 상황을 인식하며 내가 이런 감정을 느끼는 이유가 무엇인지 찾아보기\n4. 나를 복잡하게 만드는 상황에서 한 걸음 물러나 피해보기\n""")
        fp.close()
    elif rank[0] == 'neg':
        data = f"""{username}님은 이번 주 꽤 힘든 하루하루를 견디고 계시군요\n해결에 앞서 이번 한 주 너무 고생많았어요.힘들었던 하루를 조금이나마 더 행복하게 해드리기 위해 결과 파일에 좋은 방안들을 정리해서 올려드릴께요"""
        print(data)
        fp.write(f"{username}님의 조금 더 행복한 하루를 위한 행동 List\n")
        fp.write("""<자기 감정 적어보기> : 사용자님의 생각과 감정을 적을 수 있는 일기장을 사도록하세요!\n일기를 쓰면서 자기감정을 내보내게 되면 스스로와 '파장이 맞는 상태'로\n들어가게 됩니다. 이런 과정을 통해 자기 자신에 대해 길이 이해 할 수 있어요""",
        """<웃고 미소짓기> : 미소를 짓는 행위가 기분을 좋게 만들어 준다는 걸 아시나요?\n웃는 행위는 기분을 좋게 만드는 '엔돌핀'이라는 물질을 형섬함으로써\n우울감에서 조금이나마 벗어날 수 있을거에요!\n<마음껏 울기> : 우리는 어릴 때부터 우는것에 대한 기피감이 있어요.\n마음 놓고 우는 행동은 자연스럽게 기분이 나아지게 한다는\n사실을 아는가요? 우는 것은 스트레스를 해소시키고 \n기분을 좋게 만들어주며 '가슴 속에서' 슬픔을 내보내는 행동이에요!""")
        fp.close()
    else:
        print('파일 입력이 되지 않았습니다.')
        