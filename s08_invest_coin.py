#분할 적립식 매달 투자를 가정
bit_price = 1_000
eth_price = 5_00
print(f"""
"코인의 가격은 아래와 같습니다"
1. 비트코인 {bit_price}만원
2. 이더리움 {eth_price}만원
""")
money=int(input("얼마를 투자하시겠습니까? 단위:만원>>> "))
_ratio=input("투자비율은 어떻게 하시겠습니까?\n n:n형식으로 입력하세요>>> ")
_ratio_list=_ratio.split(':')
_ratio_list_int=list(map(int, _ratio_list))
_sum=sum(_ratio_list_int)

bit_n=(money*(_ratio_list_int[0]/_sum))/bit_price
eth_n=(money*(_ratio_list_int[1]/_sum))/eth_price
change = money - (bit_price*bit_n) - (eth_price*eth_n)
print(f"""\n###########################\n잔고 내역 알려드립니다
비트코인 {bit_n:.4f}개, 이더리움 {eth_n:.4f}개, 예수금 {change:.2f}만원 입니다.""")
#1:1, 3:1로 QA
