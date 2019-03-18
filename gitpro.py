#############################################
# 1) using installed git command
# 2) user friendly tool
# 3) ui will be good for user 
#    or scheduler run in background 
#    need to consider both
#    (success or fail sending email to admin)
# 
# main function > push / commit (to repository)
#                 project make (considering about extension)
#                 pull (from repository)
#
# (main function will be worke in website)
#
# * git install is the first way
# git config --global http.sslVerify false
#
# https://pypi.org/project/python-git/#history
# pip install python-git > python -m pygit
#############################################

import os
import sys
import shutil
import logging
from subprocess import Popen, PIPE, STDOUT


def logging_job():
    mylogger = logging.getLogger("jin2")
    mylogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    mylogger.addHandler(stream_handler)

    file_handler = logging.FileHandler("jin2.log")
    mylogger.addHandler(file_handler)

    mylogger.info("server start!")
    return mylogger


def check_version():
    proc = Popen(['git','--version'], shell=True, stdout=PIPE,)
    msg, _ = proc.communicate()
    msg = msg.decode('utf-8')

    print(msg)

def commit_code():
    proc = Popen(['git','--version'], shell=True, stdout=PIPE,)
    msg, _ = proc.communicate()
    msg = msg.decode('utf-8')

    print(msg)

    
    
if __name__ == '__main__':
    logging.error("something wrong!")
    logging_job()