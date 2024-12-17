import os

# ฟังก์ชันสำหรับการตรวจสอบลายเซ็นต์ในไฟล์
def scan_file(file_path, virus_signatures):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        for signature in virus_signatures:
            if signature.encode() in file_data:
                return True
    return False

# ฟังก์ชันสำหรับการโหลดลายเซ็นต์ของไวรัสจากไฟล์
def load_virus_signatures():
    signatures = []
    with open('virus_signatures.txt', 'r') as sig_file:
        for line in sig_file:
            signatures.append(line.strip())
    return signatures

# ฟังก์ชันสำหรับการสแกนโฟลเดอร์
def scan_directory(directory, virus_signatures):
    infected_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file(file_path, virus_signatures):
                infected_files.append(file_path)
    return infected_files

# โปรแกรมหลัก
def main():
    directory_to_scan = input("Enter the directory to scan: ")
    
    # โหลดลายเซ็นต์จากไฟล์
    virus_signatures = load_virus_signatures()
    
    # เริ่มการสแกน
    infected_files = scan_directory(directory_to_scan, virus_signatures)
    
    if infected_files:
        print("Infected files found:")
        for infected_file in infected_files:
            print(infected_file)
    else:
        print("No infected files found.")

if __name__ == "__main__":
    main()