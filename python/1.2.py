# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# import os
# print('process (%s) start' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('child process id is (%s), father process id is(%s)' %(os.getpid(), os.getppid()))
# else:
#     print('i (%s) just created a process (%s)' %(os.getpid(), pid))

#
# from multiprocessing import Process
# import os
#
#
# def run_pp(name):
#     print('run child process %s (%s)' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('parent process %s.' % os.getpid())
#     p = Process(target=run_pp, args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end')


# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('run task %s (%s)' %(name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('task %s runs %0.2f seconds' %(name, (end - start)))
#
# if __name__=='__main__':
#     print('parent process %s' %os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('waiting for all subprocesses done')
#     p.close()
#     p.join()
#     print('all processes done')
#
#
#

# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# =================================================================================================================================================
# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code', p.returncode)
# ============================================================================================================================================================


from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['a', 'b', 'c']:
        print('process %s put %s to queue' % (os.getpid(), value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('process %s Get %s from queue' % (os.getpid(), value))

#if __name__ == '__main__':
#    q = Queue()
#    pw = Process(target=write, args=(q,))
#    pr = Process(target=read, args=(q,))
#    pw.start()
#    pr.start()
#    pw.join()
#    pr.terminate()

import test
from test import f1
f1()
