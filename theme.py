# Theme PC Tool
import os, sys
from time import sleep
#===============================================================
try:
	import requests
	from fake_useragent import UserAgent
except:
	os.system("pip install requests")
	os.system("pip install fake_useragent")

os.system("cls")
import requests
from fake_useragent import UserAgent
#===============================================================
# KIỂM TRA KẾT NỐI MẠNG
while True:
	try:
		r = requests.get(url = 'https://www.google.com/')
		print(">>> Đã kết nối mạng!")
		sleep(3)
		os.system("cls")
		break
	except:
		print(">>> Bạn đang Offline, vui lòng kiểm tra kết nối mạng...")
		sleep(3)
os.system("cls")
#===============================================================
version = requests.get('https://raw.githubusercontent.com/HaLTools/Server_Test/master/version.txt').text
#===============================================================
def menu_update():
	s = ['\033[1;31m[-', '\033[1;32m[\\', '\033[1;33m[|', '\033[1;36m[/']
	while True:
		for i in s:
			print(f' {i}] Menu chính đang được HaL bảo trì và Update nhé', end = '\r')
			sleep(0.2)

def notification():
	from time import sleep
	print('''>>> Các bạn chờ một lúc để trở chuyển hướng về Menu chính''')
	s = ['-', '\\', '|', '/']
	for j in range(10): # 10 * 4 * 0.2 giây
		for i in s:
			print(f' [{i}] Tools này đang được HaL bảo trì và Update nhé', end = '\r')
			sleep(0.2)
#===============================================================
# GỌI HÀM menu_update() ĐỂ ĐÓNG SERVER TOOLS

# notification()

#===============================================================
try:
	# Bắt đầu hiển thị theme
	print(f'''\033[1;32m

			 /$$   /$$           /$$
			| $$  | $$          | $$
			| $$  | $$  /$$$$$$ | $$
			| $$$$$$$$ |____  $$| $$
			| $$__  $$  /$$$$$$$| $$
			| $$  | $$ /$$__  $$| $$
			| $$  | $$|  $$$$$$$| $$$$$$$$
			|__/  |__/ \\_______/|________/

*******************************************************************************
				Version: {version}
-------------------------------------------------------------------------------
				CÁC CHẾ ĐỘ CHẠY CỦA HaL TOOLS
-------------------------------------------------------------------------------
	[1]: Tăng Views cho Website/Blog
	[2]: Tăng Votes Widget Pack cho Website/Blog
	[3]: Get mã 2fa Facebook
	[4]: Check camera bị hổng bảo mật
	[5]: Máy tính quy đổi tiền điện tử Online
	[6]: Tải Video trên YouTube
	[a]: About Us
*******************************************************************************
	''')

	list_regime = ['a','1','2','3','4','5','6']
	regime = input(">>> Chọn chế độ chạy [số nguyên]: ")

	while True:
		if regime not in list_regime:
			print(">>> Rất tiếc, không có chế độ nào như bạn đã nhập :(")
			regime = input(">>> Mời nhập lại [số nguyên]: ")
		else:
			break
	def regimes(hal):
		url = f"https://raw.githubusercontent.com/HaLTools/Server_Test/master/{hal}.py"
		r = requests.get(url)
		exec(r.text)
	#=============================================
	try:
		# Gọi hàm main
		regimes(regime)
	except Exception as e:
		menu_update()

except KeyboardInterrupt:
	os.system("cls")
