from collections import Counter
print("Enter source file")
file_name=input()
f=open(file_name,"r")
src_file=f.read()
print("Enter test file")
dest=input()
g=open(dest,"r")
dst_file=g.read()
index=[]
word=[]
tag=[]
root=[]
a=[]

#Splitting the file into individual lists of index, word, tag and root

for line in src_file.split('\n'):
    bef,sep,aft=line.partition(' ')
    index.append(bef)
    a.append(aft)
b=[]
for line in a:
    bef,sep,aft=line.partition(' ')
    word.append(bef)
    b.append(aft)
for line in b:
    bef,sep,aft=line.partition(' ')
    tag.append(bef)
    root.append(aft)

temp=[]
sentence_list=[]

#Creating sentence units

for i in range(len(word)):
    if word[i]!="":
        temp.append(index[i]+" "+word[i]+" "+tag[i]+" "+root[i])
    elif word[i]=="":
        sentence_list.append(temp)
        temp=[]

index_list=[]
word_list=[]
tag_list=[]
root_list=[]
for i in range(len(word)):
    if word[i]!="":
        index_list.append(int(index[i]))
        word_list.append(word[i])
        tag_list.append(tag[i])
        root_list.append(int(root[i]))

set_tag=set(tag_list)
tagset=[]
for i in set_tag:
    tagset.append(i)
count=0

#Calculating root arcs

for i in range(len(index)):
    if(index[i]=="1"):
        count+=1
root_arcs=0
l_arcs=0
r_arcs=0
l_list=[]
r_list=[]
a=0
b=0
c=0
d=0
e=0
count1=0
count2=0
for i in range(len(root_list)):
    if(root_list[i]==0):
        root_arcs+=1

#Calculating left and right arcs count

for i in range(len(root_list)):
    if index_list[i]<root_list[i] and root_list[i]!=0:
        l_arcs+=1
    elif root_list[i]!=0:
        r_arcs+=1
i1=[]
w1=[]
t1=[]
r1=[]
tag_dict={}
ts1=[]
ts2=[]
larc_list=[]
n2=[]
l2=[]
rarc_list=[]
tag_dict2={}
ts3=[]
ts4=[]
n3=[]
l3=[]

print("\nUniversity of Central Florida\nCAP 6640 Spring 2018 - Dr. Demetrios Glinos\nDependency Parser by Yash Shah\nCorpus Statistics:")
print("\n# Tokens\t     ",len(word_list),"\n# Sentences  \t ",count,"\n# Tags\t\t\t ",len(tagset),"\n# Root Arcs  \t ",root_arcs,"\n# Left Arcs  \t ",l_arcs,"\n# Right Arcs     ",r_arcs)

#Left arcs and right arcs

for i in range(len(word)):
    if not word[i]=="":
        i1.append(int(index[i]))
        w1.append(word[i])
        t1.append(tag[i])
        r1.append(int(root[i]))
    elif word[i]=="":
        for j in range(len(i1)):
            if(i1[j]<r1[j] and r1[j]!=0):
                rnum=r1[j]
                dtag=t1[rnum-1]
                pair=t1[j]+" "+dtag
                if not pair in tag_dict:
                    tag_dict[pair]=1
                    ts1.append(t1[j])
                    ts2.append(dtag)
                elif pair in tag_dict:
                    m=tag_dict.get(pair)
                    m+=1
                    tag_dict[pair]=int(m)
            elif (i1[j] > r1[j] and r1[j] != 0):
                rnum = r1[j]
                dtag = t1[rnum - 1]
                pair = t1[j] + " " + dtag
                if not pair in tag_dict2:
                    tag_dict2[pair] = 1
                    ts3.append(t1[j])
                    ts4.append(dtag)
                elif pair in tag_dict2:
                    m = tag_dict2.get(pair)
                    m += 1
                    tag_dict2[pair] = int(m)
        i1=[]
        w1=[]
        t1=[]
        r1=[]
for a in tag_dict:
    n2.append(tag_dict[a])

for i in range(len(ts1)):
    l2.append([ts1[i],ts2[i],n2[i]])

for a in tag_dict2:
    n3.append(tag_dict2[a])

for i in range(len(ts3)):
    l3.append([ts3[i],ts4[i],n3[i]])

larc_list=sorted(l2)
rarc_list=sorted(l3)

print("\nLeft arc non-zero counts")
for i in range(len(larc_list)):
    if(larc_list[i][0]==larc_list[i-1][0]):
        print("[",larc_list[i][1],", ",larc_list[i][2],"] ")
    else:
        print("\n",larc_list[i][0],": [",larc_list[i][1],",",larc_list[i][2],"]")

print("\nRight arc non-zero counts")
for i in range(len(rarc_list)):
    if(rarc_list[i][0]==rarc_list[i-1][0]):
        print("[",rarc_list[i][1],", ",rarc_list[i][2],"] ")
    else:
        print("\n",rarc_list[i][0],": [",rarc_list[i][1],",",rarc_list[i][2],"]")

print("\nArc confusion array:\n")
for i in range(len(larc_list)):
    str=larc_list[i][0]+" "+ larc_list[i][1]
    if (larc_list[i][0] != larc_list[i - 1][0]):
        print(larc_list[i][0] + ":")
    if(str in tag_dict2):
            a=tag_dict2.get(str)
            b+=1
            print("[ ",larc_list[i][1],", ",larc_list[i][2],", ",a,"] ")
print("\nNumber of confusing arcs",b,"\nInput sentence\n\n",dst_file,"\nParsing actions and transitions")
tgt_word=[]
tgt_tag=[]
for line in dst_file.split('\n'):
    bef,sep,aft=line.partition('/')
    tgt_word.append(bef)
    tgt_tag.append(aft)
tgt_input=[]
stack=[]
stack2=[]
temp_st=""
for line in dst_file.split('\n'):
    tgt_input.append(line)
str=""
a=0
b=0
while(a==0):
    b=0
    c=0
    if(len(stack)<2 and len(tgt_input)!=0):
        print(stack," ",tgt_input,"SHIFT")
        stack.append(tgt_input[0])
        stack2.append(tgt_tag[0])
        del(tgt_input[0],tgt_tag[0])
        b=1
        e=1
    elif(len(stack)>=2):
        c=0
        temp_st=stack2[-2]+" "+stack2[-1]
        if(stack2[-1][0]=="." or stack2[-1][0]=="R" and stack2[-2][0]=="V"):
            stack_len=len(stack)
            print(stack," ",tgt_input)
            print("Right Arc",stack[-2],"-->",stack[-1])
            del(stack[-1])
            del(stack2[-1])
            b=1
        elif(stack2[-2][0]=="I" and stack2[-1][0]=="."):
            print(stack," ",tgt_input,"SWAP")
            tgt_input.append(stack[-2])
            tgt_tag.append(stack2[-2])
            del(stack[-2])
            del(stack2[-2])
            b=1
        elif(stack2[-2][0]=="V" or stack2[-2][0]=="I") and (stack2[-1][0]=="D" or stack2[-1][0]=="I" or stack2[-1][0]=="J" or stack2[-1][0]=="P" or stack2[-1][0]=="R") and len(tgt_input)!=0:
            print(stack," ",tgt_input," SHIFT ")
            stack.append(tgt_input[0])
            stack2.append(tgt_tag[0])
            del(tgt_input[0])
            del(tgt_tag[0])
            b=1
        elif((temp_st in tag_dict) and (temp_st in tag_dict2)):
            count1=tag_dict.get(temp_st)
            count2=tag_dict2.get(temp_st)
            count1=int(count1)
            count2=int(count2)
            if count1>count2:
                print(stack," ",tgt_input,"Left arc: ",stack[-2],"<--",stack[-1])
                del(stack2[-2])
                del(stack[-2])
                b=1
                c=1
            elif(count2>count1):
                print(stack," ",tgt_input,"Right arc",stack[-2],"-->",stack[-1])
                del(stack[-1])
                del(stack2[-1])
                b=1
                c=1
        elif temp_st in tag_dict and c==0:
            print(stack," ",tgt_input,"Left-arc",stack[-2],"<--",stack[-1])
            del(stack2[-2])
            del(stack[-2])
            b=1
        elif temp_st in tag_dict2 and c==0:
            print(stack," ",tgt_input,"Right-arc",stack[-2],"-->",stack[-1])
            del(stack[-1])
            del(stack2[-1])
            b=1
    elif(len(tgt_input)==0):
        e=1
        if(len(stack)==1):
            print(stack," ",tgt_input,"Root -->",stack[0])
            a=1
        b=1
    elif(b==0 and e==0 and len(tgt_input)!=0):
        print(stack," ",tgt_input,"Shift")
        stack.append(tgt_input[0])
        stack2.append(tgt_tag[0])
        del(tgt_input[0],tgt_tag[0])





















