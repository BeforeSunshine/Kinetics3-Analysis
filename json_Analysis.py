'''
json(JavaScript Object Notation):轻量级数据交换个格式，json在python 由list 和dict组成
两个模块：
json: 用于字符串和python数据类型间进行转换,四个功能（dumps、dump、loads、load）,可在不同语言之间交换数据
      只能序列化基本数据类型（列表、字典、字符串、数字），不可以序列化日期格式、类对象等
pickle: 用于python特有类型和基本数据类型间进行转换,四个功能（dumps、dump、loads、load），只可用于python，
        可以序列化所有数据类型以及类、函数等
dumps：数据类型转换成字符串
dump: 数据类型转换为字符串并存储在文件
loads:将字符串转换为数据类型
load：打开文件并从字符串转换为数据类型

'''
import json
import argparse
import os
from subprocess import call
from subprocess import Popen

parser = argparse.ArgumentParser()
parser.add_argument('--json_file', required=True, help='path to json file')
parser.add_argument('--ori_vedio_dir', default='./data/', help='path to store vedio has been downloaded')
parser.add_argument('--cut_vedio_dir', default='./cut/', help='path to store vedio has been cuted')
params = parser.parse_args()

def json_load(jsonfile):
    with open(jsonfile,'r') as fr:
        load_dict = json.load(fr,strict=False)
    return load_dict
 
def dict_info(input_dict):
    list1 =[]
    for key in input_dict.keys():
        templist = []
        dict2 = input_dict[key]
        templist.append(key)
        templist.append(dict2['url'])
        dict3 = dict2['annotations']
        templist.extend(dict3['segment'])
        templist.append(dict3['label'])
        list1.append(templist)
    return list1


def data_download(data_info, ori_data_path, cut_data_path):
    print("start download vedios:")
    for line in data_info:
        youtube_id = line[0]  # vedio name
        url = line[1]
        start_time = line[2]
        end_time = line[3]
        label = line[4]
        command1 = 'you-get -i ' + url + ' -o ' + ori_data_path + ' -O ' + youtube_id  #
        command2 = 'ffmeg -i ' + youtube_id + ' -ss ' + start_time + ' -t 10  -c cppy -y ' + cut_data_path + youtube_id
        if not os.path.exists(label):  # vedio name
            child1 =Popen(command1,shell = True)
            child1.wait()
            print('vedio has been downloaded, start to cut')
            child2 =  Popen(command2,shell = True)
            child2.wait()
            print('vedio has been cut down')
        else:
            print('this vedio already downloaded')
            continue
    print('all vedios has been downloaded')
        
     

if __name__ == '__main__':
    json_file = params.json_file  # json file that store vedio url
    ori_vedio_dir = params.ori_vedio_dir # path to store downloaded vedio
    cut_vedio_dir = params.cut_vedio_dir 
    dict1 = json_load(json_file)  # the content of json file
    result = dict_info(dict1)   
    data_download(result, ori_vedio_dir, cut_vedio_dir)    

 


        



