# 1) time.process_time()

import prime
from time import process_time

start = process_time()
prime.prime(2 ** 8)
end = process_time()
print(end - start)

print()

# 2) sys.path.append()
import sys
sys.path.append('C:\HelloPython\ch04')
import prime2
from time import process_time
start = process_time()
prime.prime(2 ** 8)
end = process_time()
print(end - start)

print()

# 3) importlib.import_module()
import os
import importlib
from glob import glob

N = 2 ** 12 # 4096

# 현재 dir은 ch09이지만 prime.py파일은 ch04에 있으므로 패키지 경로를 추가하고 작업 디렉토리도 변경
sys.path.append('C:\HelloPython\ch04')
os.chdir('C:\HelloPython\ch04')

for pth in glob('prime*'): # prime으로 시작하는 파일명 각각에 대해 접근
    name = os.path.splitext(pth)[0] # 모듈명(파일명에서 확장자 앞 까지 구함)
    print(f'\nRunning {pth} ...')
    mod = importlib.import_module(name) # 해당 모듈 import

    # 실행 시간 측정
    start = process_time()
    mod.prime(N)
    end = process_time()
    print('elapsed:', end - start)
