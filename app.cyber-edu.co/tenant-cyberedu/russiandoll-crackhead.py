#!/bin/python3
import os
from time import sleep

def remove_by_rule(file_list,rule):
    new_file_list=[]
    for file in file_list:
        if rule in file:
            continue
        new_file_list.append(file)
    return new_file_list

def remove_folders(file_list):
    # print("function")
    new_file_list=[]
    for file in file_list:
        # print(file, os.path.isdir(file))
        if os.path.isdir(file):
            continue
        new_file_list.append(file)
    return new_file_list

rules=['.py','.zip','.7z','.txt','.gz','.sh']


while True:
    files=os.popen("ls").read().split("\n")[:-1]
    # print(files)
    for rule in rules:
        files=remove_by_rule(files,rule)
    files=remove_folders(files)
    print(files)
    if (len(files)!=1):
        raise("To many files")
    file=files[0]
    file_type=os.popen(f"file {file}").read()
    print(file_type)
    if ": gzip" in file_type:
        os.popen(f"mv {file} {file}.gz").read()
        file+='.gz'
        os.popen(f"gzip -dv {file}").read()
    elif ": Zip" in file_type:
        os.popen(f"mv {file} {file}.zip").read()
        file+=".zip"
        os.popen(f"~/john/run/zip2john {file} > hash.txt").read()
        john_output=os.popen("~/john/run/john hash.txt").read()
        print(john_output)
        john_output=os.popen("~/john/run/john --show hash.txt").read()
        print(john_output)
        password=john_output.split(":")[1]
        print(password)
        os.popen(f"unzip -P {password} {file}").read()
        os.popen("mv ./archives/* .")
    elif ": 7-zip" in file_type:
        os.popen(f"mv {file} {file}.7z")
        file+=".7z"
        os.popen(f"~/john/run/7z2john.pl {file} > hash.txt").read()
        john_output=os.popen("~/john/run/john hash.txt").read()
        sleep(1)
        print(john_output)
        john_output=os.popen("~/john/run/john --show hash.txt").read()
        print(john_output)
        password=john_output.split(":")[1]
        print(password)
        os.popen(f"7z x {file} -p{password}").read()
    else:
        raise("unknown file type")
    # break