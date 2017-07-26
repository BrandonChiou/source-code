from __future__ import print_function

fa_in = open("uniprot_swiss.fasta", "r")
fa_Info = []   #store info
fa_Seq = []   #store sequence
fa_Num = -1
delnum = 0
for line in fa_in.readlines():
    line = line.rstrip()
    #print (line)
    if line[0] == ">":     #判斷為資訊，就存在fa_Info，否則存在fa_Seq
        fa_Info.append(line)
        fa_Num += 1
        fa_Seq.append("")
    else:
        fa_Seq[fa_Num] += line
#測試輸出
print (fa_Info[0])
print (fa_Seq[0][:60]+'\n'+fa_Seq[0][60:])
print (len(fa_Seq[0]))
print (fa_Num+1)
#
fa_out = open("rm_short_swiss.fasta", "w")
for i in range(fa_Num + 1) :
    

    if len(fa_Seq[i]) < 30 :
        delnum += 1
    #elif len(fa_Seq[i]) > 60 :      #每行寫60个碱基
       # fa_out.write(fa_Seq[i][:60] + "\n")
       # fa_Seq[i] = fa_Seq[i][60:]
    else:
        fa_out.write(fa_Info[i] + "\n")
        fa_out.write(fa_Seq[i] + "\n")
print (delnum)    #刪掉的序列數

		
		
		
		
		
		
		
		
		
		
		
