# Kinetics3-Analysis

analysis content from Kinetics3 dataset's json file then download youtube vedios to local
## 1. install you-get tool
## 2. install ffmpeg tool
## 3. run json_Analysis.py to download train dataset from youtube:
 python json_Analysis.py --json_file kinetics_train.json --ori_vedio_dir ./trian/ori_vedio --cut_vedio_dir ./trian/cut_vedio
## 4. run json_Analysis.py to download validation dataset from youtube:
  python json_Analysis.py --json_file kinetics_val.json --ori_vedio_dir ./test/ori_vedio --cut_vedio_dir ./test/cut_vedio
## 5. 目录结构如下：
   ├── json_Analysis.py
   ├── kinetics_train.json
   ├── kinetics_val.json
   ├── test
   │   ├── cut_vedio
   │   └── ori_vedio
   └── train
       ├── cut_vedio
       └── ori_vedio
