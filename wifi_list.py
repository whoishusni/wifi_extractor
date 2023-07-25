import subprocess
import re
import time

def main():
    print('#'.center(50,'#'))
    print('''
          Aplikasi Liat Wifi
          Yang Sudah Pernah Terkonek
          ''')
    print('#'.center(50,'#'))
    commands = subprocess.run(['netsh','wlan','show','profile'], capture_output=True).stdout.decode()
    all_profile = re.findall('All User Profile     : (.*)\r', commands)
    if len(all_profile) != 0:
        for name in all_profile:
            profile_info = subprocess.run(['netsh','wlan','show','profile',name], capture_output=True).stdout.decode()
            if re.search('Security key           : Absent', profile_info):
                continue
            else:
                clear_content = subprocess.run(['netsh','wlan','show','profile',name, 'key=clear'], capture_output=True).stdout.decode()
                for_pass = re.search('Key Content            : (.*)\r', clear_content)
            print('SSID : {}\nPASS : {}\n----------------------------------'.format(name,for_pass[1]))
            
            # write to txt file ---------->
            writer = open('wifi.txt', 'a')
            writer.write('SSID : {}\nPASS : {}\n\n'.format(name,for_pass[1]))
            writer.close
        
if __name__ == '__main__':
    main()
    #time.sleep(100)