def write_diary():
    diary_content = ""
    print("일기를 작성해주세요. 작성이 끝났다면 '일기 끝' 을 입력하세요.")
    #일기 작성
    while True:
        line = input()
        if line.lower() == '일기 끝':
            break
        diary_content += line + '\n'

     
    while True:
        day_of_week = input("현재 요일을 입력하세요(ex.월요일): \n")

        if(day_of_week == "월요일"):
            file_name = f"monday_diary.txt"
            with open(file_name, 'w') as file:
                file.write(diary_content)
            print(f"일기가 {file_name} 파일에 저장되었습니다.")
            break
        elif(day_of_week == "화요일"):
            file_name = f"tuesday_diary.txt"
            with open(file_name, 'w') as file:
                file.write(diary_content)
            print(f"일기가 {file_name} 파일에 저장되었습니다.")
            break
        elif(day_of_week == "수요일"):
            file_name = f"wensday_diary.txt"
            with open(file_name, 'w') as file:
                file.write(diary_content)
            print(f"일기가 {file_name} 파일에 저장되었습니다.")
            break
        elif(day_of_week == "목요일"):
            file_name = f"thursday_diary.txt"
            with open(file_name, 'w') as file:
                file.write(diary_content)
            print(f"일기가 {file_name} 파일에 저장되었습니다.")
            break
        elif(day_of_week == "금요일"):
            file_name = f"friday_diary.txt"
            with open(file_name, 'w') as file:
                file.write(diary_content)
            print(f"일기가 {file_name} 파일에 저장되었습니다.")
            break
        elif(day_of_week == "토요일"):
            file_name = f"saturday_diary.txt"
            with open(file_name, 'w') as file:
                file.write(diary_content)
            print(f"일기가 {file_name} 파일에 저장되었습니다.")
            break
        elif(day_of_week == "일요일"):
            file_name = f"sunday_diary.txt"
            with open(file_name, 'w') as file:
                file.write(diary_content)
            print(f"일기가 {file_name} 파일에 저장되었습니다.")
            break
        else:
            print("잘못입력하셨습니다 다시 입력해주세요")
            continue


