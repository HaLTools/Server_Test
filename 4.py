# Check cam bị lộ bảo mật
#===============================================================
# GỌI HÀM menu_update() ĐỂ ĐÓNG SERVER TOOLS

# notification()

#===============================================================

try:
    import re, os, sys, requests
    from os import system
    from time import sleep
    print("\n        *******************************************************************************\n")
    print(">>> Chọn quốc gia bạn muốn check camera")
    print("""
01. Russian Federation
02. United States
03. Japan
04. Canada
05. New Zealand
06. Ukraine
07. Germany
08. Austria
09. Spain
10. Turkey
11. Hong Kong
12. Greece
13. Portugal
14. Singapure
15. Columbia
16. Vietnam
    """)
    num = int(input(">>> Chọn quốc gia bạn muốn check camera: "))
    if num == 1:
            print('')
            os.system(delet)
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,82):

                    url = ("https://www.insecam.org/en/bycountry/RU/?page="+str(page))

                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0

                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)

                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()

                         count += 1
            except:
                print ("") 
    if num == 2:
            print('')
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
                for page in range (0,720):

                    url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))

                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0

                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()

                         count += 1
            except:
                print (" ")
    if num == 3:
            print('')
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
                for page in range (0,232):

                    url = ("https://www.insecam.org/en/bycountry/JP/?page="+str(page))

                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0

                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()

                         count += 1
            except:
                print (" ")
    if num == 4:
            print('')
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
                for page in range (0,38):

                    url = ("https://www.insecam.org/en/bycountry/CA/?page="+str(page))

                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0

                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()

                         count += 1
            except:
                print (" ")
    if num == 5:
            print('')
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
                for page in range (0,5):
    			
                    url = ("https://www.insecam.org/en/bycountry/NZ/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ")             
    if num == 6:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,2):
    			
                    url = ("https://www.insecam.org/en/bycountry/UK/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ") 
    if num == 7:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,107):
    			
                    url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ")
    if num == 8:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,48):

                    url = ("https://www.insecam.org/en/bycountry/AT/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                         count += 1
            except:
                print (" ")           
    if num == 9:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,39):
    			
                    url = ("https://www.insecam.org/en/bycountry/ES/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ")  
    if num == 10:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,54):

                    url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ")             
    if num == 11:
            print('')
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,7):

                    url = ("https://www.insecam.org/en/bycountry/HK/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ")  
    if num == 12:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,8):

                    url = ("https://www.insecam.org/en/bycountry/GR/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ")           
    if num == 13:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,7):

                    url = ("https://www.insecam.org/en/bycountry/PT/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ")        
    if num == 14:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,7):

                    url = ("https://www.insecam.org/en/bycountry/SG/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()

                         count += 1
            except:
                print (" ")      
    if num == 15:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,6):

                    url = ("https://www.insecam.org/en/bycountry/CO/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ") 
    if num == 16:
            print('')		
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}       
                for page in range (0,6):

                    url = ("https://www.insecam.org/en/bycountry/VN/?page="+str(page))
                
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                    
                    for _ in findip:
                         hasil = findip[count]

                         print (hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                     
                         count += 1
            except:
                print (" ") 

    print("\n>>> Tất cả IP bị lộ đều được lưu tại file logs.txt")

except KeyboardInterrupt:
    r = requests.get("https://raw.githubusercontent.com/HaLTools/PC_Tools/master/theme.py")
    exec(r.text)
