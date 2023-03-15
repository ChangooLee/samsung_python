stocks = ['삼성전자','SK하이닉스']

def manageStocks():
    user_input=0
    while user_input!='4':
        print("""
            === 관심 주식 ===
            1. 관심 주식 보기
            2. 관심 주식 추가하기
            3. 관심 주식 삭제하기
            4. 종료하기
            """)
        user_input=input("기능을 선택하세요 >>> ")
        if user_input == '1':
            print("관심 주식은 아래와 같습니다.")
            print("===========================")
            print(', '.join(stocks))
            print("===========================")
        elif user_input == '2':
            add_coin = input("추가할 주식명을 쓰세요 >>> ")
            stocks.append(add_coin)
        elif user_input == '3':
            del_coin = input("삭제할 주식명을 쓰세요 >>> ")
            stocks.remove(del_coin)
        elif user_input == '4':
            print("프로그램이 종료 되었습니다.")
    return stocks

if __name__ == '__main__':
    manageStocks()