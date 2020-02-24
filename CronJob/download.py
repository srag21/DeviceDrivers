import os
import sys
import subprocess
import time

def main():
	start_time = time.time()
	mycmd = subprocess.getoutput("time curl -o /dev/null https://www.apple.com/")
	#time_taken = time.time() - start_time
	#print(time_taken)
	#print(mycmd)

if __name__ == '__main__':
	main()