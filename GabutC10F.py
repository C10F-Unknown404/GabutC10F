import os
import subprocess
import time

# Color codes
MERAH = '\033[31m'
HIJAU = '\033[32m'
KUNING = '\033[33m'
BIRU = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
PUTIH = '\033[37m'
RESET = '\033[0m'

DIM = '\033[2m'

def clear_screen():
    os.system("clear")

def print_attack_logo():
    logo = f'''{MERAH} 
 
    ⠀⠀ ⠀⠀⣀⡤⠔⠒⠊⠉⠉⠉⠉⠙⠒⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠞⠁⠀⣀⠀⠀⠀⠀⢀⣀⡀⠀⢀⣀⠀⠀⠀⠀⢀⠀⠈⠱⣄⠀⠀⠀
⠀⠀⡴⠁⡠⣴⠟⠁⢀⠤⠂⡠⠊⡰⠁⠇⢃⠁⠊⠑⠠⡀⠀⢹⣶⢤⡈⢣⡀⠀
⠀⡼⢡⣾⢓⡵⠃⡐⠁⠀⡜⠀⠐⠃⣖⣲⡄⠀⠀⠱⠀⠈⠢⠈⢮⣃⣷⢄⢳⠀
⢰⠃⣿⡹⣫⠃⡌⠀⠄⠈⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠣⠀⠀⠱⠈⣯⡻⣼⠈⡇
⡞⢈⢿⡾⡃⠰⠀⠀⠀⠀⠀⠀⠀⠀⣘⣋⠀⠀⠀⠀⠀⠀⠀⠀⠇⢸⢿⣿⢠⢸
⡇⢸⡜⣴⠃⠀⠀⠀⠀⠀⣀⣀⣤⡎⠹⡏⢹⣦⣀⣀⠀⠀⠀⠀⢈⠘⣧⢣⡟⢸
⢧⢊⢳⡏⣤⠸⠀⠀⠀⢸⣿⣿⣿⡇⢰⡇⢠⣿⣿⣿⣷⠀⠀⠀⡆⢸⢹⡼⣱⢸
⢸⡘⢷⣅⣿⢂⢃⠐⠂⣿⣿⣿⣿⣿⣼⣇⣾⣿⣿⣿⣿⠁⠂⡰⡠⣿⢨⡾⠃⡇
⠀⢳⡱⣝⠻⡼⣆⡁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠐⣰⣇⠿⣋⠝⡼⠀
⠀⠀⢳⡈⢻⠶⣿⣞⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢣⣿⡶⠟⢉⡼⠁⠀
⠀⠀⠀⠙⢦⡑⠲⠶⠾⠿⢟⣿⣿⣿⣿⣿⣿⣿⣿⡛⠿⠷⠶⠶⠊⡡⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠦⣝⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⡛⠛⠛⣋⠴⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠦⠿⣿⣿⣿⣿⣿⣿⠿⠧⠒⠋⠁⠀⠀⠀⠀⠀
AUTHOR = C10F
SC GABUT


===================================
'''
    print(logo)
    print(f"{MERAH}SC INI HANYA BUAT SENENG SENENG SAJA{RESET}")

def print_menu():
    print(f"{DIM}SC GABUT BY C10F{RESET}")
    print(f"{MERAH}1. Hacker Prank{RESET}")
    print(f"{KUNING}<==========================>{RESET}")
    print(f"{MERAH}2. Bermain Moon Buggy{RESET}")
    print(f"{KUNING}<==========================>{RESET}")
    print(f"{MERAH}3. Animasi Kereta{RESET}")
    print(f"{KUNING}<==========================>{RESET}")
    print(f"{MERAH}4. Hack Bulan{RESET}")
    print(f"{KUNING}<==========================>{RESET}")
    print(f"{MERAH}5. Hack Data-data tentada Israel{RESET}")
    print(f"{KUNING}<==========================>{RESET}")
    print(f"{MERAH}6. Informasi tentang Perangkat Android anda{RESET}")
    print(f"{KUNING}<==========================>{RESET}")
    print(f"{MERAH}7. Kalender{RESET}")
    print(f"{KUNING}<==========================>{RESET}")
    print(f"{MERAH}8. Keluar{RESET}")
    print(f"{MERAH}================================{RESET}")

    choice = input(f"{BIRU}Silahkan pilih: {RESET}")

    if choice == "1":
        install_and_run("cmatrix")
    elif choice == "2":
        install_and_run("moon-buggy")
    elif choice == "3":
        install_and_run("sl")
    elif choice == "4":
        hack_moon()
    elif choice == "5":
        hack_israel_data()
    elif choice == "6":
        android_info()
    elif choice == "7":
        install_and_run("calcurse")
    elif choice == "8":
        print(f"{MERAH}TERIMAKASIH TELAH MENCOBA SC GABUT BY C10F{RESET}")
        exit()
    else:
        print(f"{MERAH}Pilihan tidak valid{RESET}")

def install_and_run(package):
    subprocess.run(["pkg", "install", package, "-y"])
    subprocess.run([package])

def hack_moon():
    os.system("figlet Hack bulan")
    daerah = input("Masukan nama daerah anda: ")
    print("Sedang hack bulan di daerah", daerah)
    print("Loading...")
    time.sleep(2)
    print(f"{MERAH}Bulan berhasil di hack!{RESET}")

def hack_israel_data():
    print("Sedang mencari data...")
    print("Loading...")
    time.sleep(2)
    print(f"{KUNING}Negara: Israel{RESET}")
    print(f"{KUNING}Tentara aktif AD, AL, AU DLL: 176.500{RESET}")
    print(f"{KUNING}Tentara cadangan: 445.000{RESET}")
    print(f"{KUNING}Paramiliter (karabiner, polisi militer, garda nasional, dll.): 7.650{RESET}")
    print(f"{MERAH}Total: 629.150{RESET}")
    print("SC akan diupdate nanti")

def android_info():
    print(f"Konfigurasi jaringan:")
    print(run_command("ifconfig"))
    time.sleep(2)
    print(f"Merek HP Anda:")
    brand = run_command("getprop ro.product.brand")
    model = run_command("getprop ro.product.model")
    print(f"Brand: {brand.strip()}")    
    print(f"Model: {model.strip()}")
    mem_total = int(run_command("grep MemTotal /proc/meminfo | awk '{print $2}'"))
    mem_available = int(run_command("grep MemAvailable /proc/meminfo | awk '{print $2}'"))
    mem_total_mb = mem_total // 1024
    mem_available_mb = mem_available // 1024
    print(f"Total Memori: {mem_total_mb} MB")
    print(f"Memori Tersedia: {mem_available_mb} MB")

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Run the functions
clear_screen()
print_attack_logo()
while True:
    print_menu()
    time.sleep(5)
    clear_screen()