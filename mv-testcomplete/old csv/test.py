import subprocess

def test():
    proc = subprocess.call(['TestComplete.exe'], shell = True)
    #str = proc.decode('ascii')
    #print(str)
test()
