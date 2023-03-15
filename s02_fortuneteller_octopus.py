import random
coin = random.randint(0,1)
user_input = int(input("""
점쟁이 문어에게 미래를 물어봅시다. 손을 모으시고~ 
2022년에 대박이 날 수 있을까요? 본인의 생각은?
'대박 날 수 있을 것이다': 1번을 입력
'대박은 안나지만 괜찮을 것이다:' 0번을 입력
>>>
"""))

if user_input == coin:
    print("오 맞췄습니다")
else:
    print("땡 틀렸습니다.")
