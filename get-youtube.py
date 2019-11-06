import csv
import os

tag_to_dl="/t/dd00002"
file_name="eval_segments.csv"
csv_file=csv.reader(open(file_name,'r'))

head_url = "https://www.youtube.com/watch?v="

count = 0
data_file = []

for i in csv_file:
    data_file.append(i)

print("please input num to get!")
num = input()
print("now to get "+str(num)+"videos!")
num_video=int(num)


for i in range(len(data_file)-5):

    
    for j in range(len(data_file[5+i])-3):
        flag = data_file[5+i][j+3].find(tag_to_dl)
    
    if flag!=-1:
        url_video = head_url + data_file[5+i][0]
        cmd = "youtube-dl --extract-audio --audio-format mp3 --id " + url_video
        print(cmd)
        try:
            print("ready to dl "+str(count)+" video!")
            os.system(cmd)
        except:
            print("emmmm,something wrong!")
        else:
            count=count+1
            print("get ok!")
        

        start_time = "00:" + str(int(int(data_file[5+i][1].split(".")[0])/60)) + ":" + str(int(int(data_file[5+i][1].split(".")[0])%60))
        end_time = "00:" + str(int(int(data_file[5+i][2].split(".")[0])/60)) + ":" + str(int(int(data_file[5+i][2].split(".")[0])%60))
            
        cmd_con = "ffmpeg -i " + str(data_file[5+i][0]) + ".mp3 -vn -acodec copy -ss " + start_time + " -t " + end_time + " ./out/"+ data_file[5+i][0] +".mp3"
        print(cmd_con)
        try:
            os.system(cmd_con)
        except:
            print("error in convert!\n")
        else:
            print("convert ok!")

    if count==num_video:
        break
