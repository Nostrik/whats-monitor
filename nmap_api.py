import subprocess
import shlex
import time
import os

cmd = 'nmap -sP 192.168.0.1/24'
args = shlex.split(cmd)

if __name__ == "__main__":
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p.wait()
    time.sleep(10)
