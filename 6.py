# Download Video YouTube
#===============================================================
# GỌI HÀM menu_update() ĐỂ ĐÓNG SERVER TOOLS

# notification()

#===============================================================

import os
try:
	from pytube import YouTube
except:
	os.system('pip install pytube')
	os.system("cls")

try:
	from pytube import YouTube
	print("\n        *******************************************************************************\n")
	urls = input('>>> Nhập những Url Video YouTube muốn tải: ')
	urls = " ".join(urls.split())
	urls = urls.split()

	def down(url):
		yt = YouTube(url)
		video = yt.streams.filter(progressive = True, file_extension = 'mp4').last().download()
		print(f'>>> Video đang ở {video}')

	for url in urls:
		try:
			down(url)
		except:
			print('>>> Download Fail!')

except KeyboardInterrupt:
    r = requests.get("https://raw.githubusercontent.com/HaLTools/PC_Tools/master/theme.py")
    exec(r.text)

