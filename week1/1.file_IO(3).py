# sys 파이썬 터미널로 실행 시 입력인수 전달
# 실습 3

'''
import sys

args = sys.argv[1:]
src_name = args[0]
dst_name = args[1]

src_file = open(src_name, 'r')
dst_name = open(dst_name, 'w')

for i in src_file:
    dst_name.write(i)

src_file.close()
dst_name.close()

print("copy done")
'''

#TA 코드

import sys

src_file = sys.argv[1]
dst_file = sys.argv[2]

f_s = open(src_file, 'r')
f_d = open(dst_file, 'w')

data = f_s.read()
f_d.write(data)

f_s.close()
f_d.close()