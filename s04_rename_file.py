# (카카오로 사진 파일을 하나 받아보자)
# 김대리는 이번에 업무를 위해 박람회에 참가하였습니다.
# 함께 참가한 이과장님이 폰으로 사진을 찍고 카톡으로 전달하였습니다.
# 카톡으로 전달받은 파일의 명은 KakaoTalk_20210714_114434023.jpg 이런 식으로 되어있어서
# 업무 폴더에 저장하기 위해서 지저분한 파일이름을 하나씩 장인정신으로 바꾸기 시작합니다.
# 옆에서 보고 있던 파이썬을 배운 신입 장그래가 김대리님 "그거 한 번에 가능합니다"라고 말합니다
# 5초 후 모든 파일명이 이런 형식(KakaoTalk_20210714_114434023.jpg -> 박람회_20210714_114434023.jpg)
# 으로 바뀌었습니다. 어떻게 장그래는 해결했을까요?

import os
path = os.getcwd()+'\\rename'
#Mac은 '\\rename' 대신에 '/rename'
files = os.listdir('./rename')

user_input = input(
    "바꾸고 싶은 이름을 입력하시오\t from:to형식으로 적어주세요\n ex)KakaoTalk:박람회\n>>>")
user_input_split = user_input.split(':')


for file in files:
    change_name = file.replace(user_input_split[0], user_input_split[1])
    os.rename(os.path.join(path, file), os.path.join(path, change_name))

print("\n바뀐 이름은 아래와 같습니다\n", os.listdir('./rename'))
