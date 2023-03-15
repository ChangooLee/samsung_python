# pip install qrcode
# pip install pillow
import qrcode
# url 변수에 변수값으로 주소를 입력하세요
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'

# url = 'https://debank.com/profile/0x84d34f4f83a87596cd3fb6887cff8f17bf5a7b83?chain='
qr_img = qrcode.make(url)
qr_img.save('my QRcode.png')

print("QR code가 생성되었습니다.")
