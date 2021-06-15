# Máy tính quy đổi tiền điện tử online
#===============================================================
# GỌI HÀM menu_update() ĐỂ ĐÓNG SERVER TOOLS

# notification()

#===============================================================

try:
	import json, requests

	while True:
		#==================================================
		print("\n        *******************************************************************************\n")
		from_ = input(">>> Từ: ").upper()
		to = input(">>> Sang: ").upper()
		amount = input(f'>>> Số lượng cần quy đổi từ "{from_}" sang "{to}": ')
		#==================================================

		#==================================================
		file_name = requests.get(url = 'https://raw.githubusercontent.com/HoangGenZ/app-quy-doi-tien-online/master/file.json')
		data = file_name.json()
		#==================================================
		id_from = data["coin"][from_]
		id_to = data["coin"][to]
		#==================================================

		#==================================================
		url = f"https://web-api.coinmarketcap.com/v1/tools/price-conversion?amount={amount}&convert_id={id_to}&id={id_from}"

		a = requests.get(url)

		b = a.json()

		c = b["data"]["quote"][str(id_to)]["price"]
		#==================================================

		print(f"""
	==================================================
	>>> Từ {amount} {from_} đổi được ~ {round(c, 3)} {to}
	==================================================
			""")

except KeyboardInterrupt:
	r = requests.get("https://raw.githubusercontent.com/HaLTools/PC_Tools/master/theme.py")
	exec(r.text)
