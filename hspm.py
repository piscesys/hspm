from ctypes import cdll
import os


pip_mirror_list = ["https://pypi.tuna.tsinghua.edu.cn/simple", "https://repo.huaweicloud.com/repository/pypi/simple",
                   "https://mirror.sjtu.edu.cn/pypi/web/simple"]
pip_mirror_host = ["pypi.tuna.tsinghua.edu.cn", "repo.huaweicloud.com",
                   "mirror.sjtu.edu.cn"]

pip_mirror_time = {}


print("Please wait for test... 正在测速，请稍等...")

for i in range(len(pip_mirror_host)):
    output = os.popen(f'ping {pip_mirror_host[i]} -c4').read()
    pip_mirror_time[pip_mirror_host[i]] = output.split("0% packet loss, ")[-1].split("\n")[0].split(" ")[-1].split("ms")[0]


result_time = []
for i in pip_mirror_time:
    result_time.append(pip_mirror_time[i])
    print(i,pip_mirror_time[i])

result = pip_mirror_list[result_time.index(min(result_time))]
print(f"The result is {result} 选择结果为{result}")

os.system('mkdir $HOME/.pip')
os.system('touch $HOME/.pip/pip.conf')
os.system(f'echo -e "[global]\nindex-url = {result}" >> $HOME/.pip/pip.conf')

print("pip OK.")