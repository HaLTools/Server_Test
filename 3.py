# Get mã 2fa Facebook
#===============================================================
# GỌI HÀM menu_update() ĐỂ ĐÓNG SERVER TOOLS

# notification()

#===============================================================
print("\n        *******************************************************************************\n")
import requests
def get_2fa(code):
	code = code.replace(' ', '')
	url = f"http://2fa.live/tok/{code}"
	r = requests.get(url = url)
	data = r.json()
	print(f'>>> Code 2fa của bạn là: {data["token"]}')

try:
	while True:
		code = input(">>> Nhập Code 2fa của các bạn vào đây: ")
		try:
			get_2fa(code)
			print('')
		except:
			print('>>> Error!')

except KeyboardInterrupt:
	r = requests.get("https://raw.githubusercontent.com/HaLTool/PC_Tools/master/theme.py")
	exec(r.text)
