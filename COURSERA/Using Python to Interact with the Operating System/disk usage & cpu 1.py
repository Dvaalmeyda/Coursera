#Disk usage Check
import shutil
du = shutil.disk_usage("/")
print(du)

du.free/du.total*100

#cpu work
import psutil
psutil.cpu_percent(0.1)

exit()