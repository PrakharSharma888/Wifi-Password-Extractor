import subprocess #to access cmd from python
wifis = []
passs=[]

data = subprocess.check_output(['netsh', 'wlan' ,'show' ,'profiles']).decode('utf-8').split('\n')
for line in data:
    if "    All User Profile" in line:
        wifis.append(line)
hell = [i.split(':')[1][1:-1] for i in wifis]
for ello in hell:
    data1 = subprocess.check_output(['netsh', 'wlan', 'show', 'profile',ello,'key=clear']).decode('utf-8').split('\n')
    for line in data1:
        if "    Key Content" in line:
            passs.append(line)
    dam = [i.split(':')[1][1:-1] for i in passs]
res = dict(zip(hell,dam))
print(res)