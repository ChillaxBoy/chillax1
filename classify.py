import os
import shutil

#原始照片分类
path_img='H:\FTV\FRAME\FRAMET'#照片原始文件夹路径
ls = os.listdir(path_img)
#print(len(ls))
for i in ls:
    if i.find('mcam_1_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam1\ " + i)
    elif i.find('mcam_2_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam2\ " + i)
    elif i.find('mcam_3_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam3\ " + i)
    elif i.find('mcam_4_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam4\ " + i)
    elif i.find('mcam_5_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam5\ " + i)
    elif i.find('mcam_6_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam6\ " + i)
    elif i.find('mcam_7_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam7\ " + i)
    elif i.find('mcam_8_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam8\ " + i)
    elif i.find('mcam_9_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam9\ " + i)
    elif i.find('mcam_10_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam10\ " + i)
    elif i.find('mcam_11_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam11\ " + i)
    elif i.find('mcam_12_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam12\ " + i)
    elif i.find('mcam_13_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam13\ " + i)
    elif i.find('mcam_14_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam14\ " + i)
    elif i.find('mcam_15_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam15\ " + i)
    elif i.find('mcam_16_')!=-1:
        shutil.move(path_img + '/' + i, "H:\FTV\FRAME\FRAMET\cam16\ " + i)


#重命名
for j in range(1,17):
    if j == 1:
        path = "H:\FTV\FRAME\FRAMET\cam1"
    elif j == 2:
        path = "H:\FTV\FRAME\FRAMET\cam2"
    elif j == 3:
        path = "H:\FTV\FRAME\FRAMET\cam3"
    elif j == 4:
        path = "H:\FTV\FRAME\FRAMET\cam4"
    elif j == 5:
        path = "H:\FTV\FRAME\FRAMET\cam5"
    elif j == 6:
        path = "H:\FTV\FRAME\FRAMET\cam6"
    elif j == 7:
        path = "H:\FTV\FRAME\FRAMET\cam7"
    elif j == 8:
        path = "H:\FTV\FRAME\FRAMET\cam8"
    elif j == 9:
        path = "H:\FTV\FRAME\FRAMET\cam9"
    elif j == 10:
        path = "H:\FTV\FRAME\FRAMET\cam10"
    elif j == 11:
        path = "H:\FTV\FRAME\FRAMET\cam11"
    elif j == 12:
        path = "H:\FTV\FRAME\FRAMET\cam12"
    elif j == 13:
        path = "H:\FTV\FRAME\FRAMET\cam13"
    elif j == 14:
        path = "H:\FTV\FRAME\FRAMET\cam14"
    elif j == 15:
        path = "H:\FTV\FRAME\FRAMET\cam15"
    elif j == 16:
        path = "H:\FTV\FRAME\FRAMET\cam16"
    filelist = os.listdir(path)
    count=0
    #for file in filelist:
        #print(file)
    for file in filelist:
        Olddir=os.path.join(path,file)
        if os.path.isdir(Olddir):
            continue
        filename=os.path.splitext(file)[0]
        filetype=os.path.splitext(file)[1]
        Newdir=os.path.join(path,str(count).zfill(3)+filetype)
        os.rename(Olddir,Newdir)
        count+=1