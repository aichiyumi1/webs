"'我的主页'"


import streamlit as st
from PIL import Image

page=st.sidebar.radio("首页",["历史","网站","处理图片","词典","留言","安利音乐"])

def img_change(img,rc,gc,bc):
            width,height=img.size
            img_array=img.load()
            for x in range(width):
                for y in range(height):
                    r=img_array[x,y][rc]
                    g=img_array[x,y][gc]
                    b=img_array[x,y][bc]
                    img_array[x,y]=(r,g,b)
            return img

def page1():
    "'历史'"
    st.image("李晨曦_503d269759ee3d6d1ea768c94c166d224f4ade4b.webp")
    st.write("这是秦始皇，统一六国，创立中央集权，功不可没。可他却是从质子出身，有两个爹,一个嬴异人，一个嫪毐（假）。一生堪称爽文男主，死后却被唾弃，背各种各样的锅，后世称为满级背锅侠。在西安有人扮演秦始皇和兵马俑跳科目三，冲上热搜。他可太难了")

def page2():
    "'网站'"
    st.link_button("bilibili","https://www.bilibili.com/") 
    st.link_button("腾讯视频","https://v.qq.com/")
    st.link_button("中国新闻网","https://www.chinanews.com.cn/")
    
    
def page3():
    "'处理图片'"
    st.write(":green[图片处理工具]:full_moon_with_face:")
    uploaded_file=st.file_uploader("上传图片",type=["png","jpeg","jpg","web"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        t1,t2,t3,t4=st.tabs(["原图","s1","s2","s3"])
        ch = st.toggle('反色滤镜')
        with t1:
            st.image(img)
        with t2:
            st.image(img_change(img,1,0,2))
        with t3:
            st.image(img_change(img,2,0,1))
        with t4:
            st.image(img_change(img,0,2,1))

def page4():
    "词典"
    st.write("英汉词典")
    with open("words_space.txt","r",encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list=f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding="utf-8") as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        if word=='Python':
            st.code('''print(你干嘛哈哈哎呦)''')
        if word=="snow":
            st.snow()
        if word=="birthday":
            st.balloons()
        if word=="chicken":
            st.code("你干嘛哈哈哎呦")
        if word=="basketball":
            st.code("唱跳RAP打篮球")
        if word=="pain":
            st.code("哼哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊嗷嗷啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊")
        if word=="delicious":
            st.code("艾玛太香了")
        if word=="toliet":
            st.code("嗨嗨嗨来了奥")
        if word=="shit":
            st.code("我敢吃三斤")
        if word=="walk":
            st.code("教主")
        if word=="gluten":
            st.code("让你吃到真正的石灰")
            st.image("屏幕截图 2024-02-03 181851.png")
        if word=="name":
            st.code("我是超威蓝猫！")
        if word=="walker":
            st.image("李晨曦_Alan-Walker-JustMusic.fr_.jpg")
        if word=="banana":
            st.image("屏幕截图 2024-02-03 181033.png")
        if word=="manure":
            st.image("屏幕截图 2024-02-03 181446.png")
        if word=="stop":
            st.code("砸瓦鲁多")

            
def page5():
    "留言"
    with open("leave_messages.txt","r",encoding='utf-8') as f:
        message_list=f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split("#")
    for i in message_list:
        if i[1]=="阿短":
            with st.chat_message('笑'):
                st.write(i[1],':',i[2])
        elif i[1]=='编程猫':
            with st.chat_message('蚌'):
                st.write(i[1],':',i[2])
    name=st.selectbox('我是......',["阿短","编程猫"])
    new_message=st.text_input('想要说的话......')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding="utf-8") as f:
            message=''
            for i in message_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'/n'
            message=message[:-1]
            f.write(message)

def page6():
    "安利电音音乐"
    a = st.radio(
    'alan walker：',
    ['alone', 'faded', 'the spectre',"sing me to sleep","all falls down","darkside"]
)
    if a=='alone':
        st.audio('1117151514 (1).mp3',format="audio/mp3")
    if a=="faded":
        st.audio("2955849152.mp3",format="audio/mp3")
    if a=="the spectre":
        st.audio("M5000044FNhJ4GLJGc.mp3",format="audio/mp3")
    if a=="sing me to sleep":
        st.audio("M5000026yzhQ1ONbeC.mp3",format="audio/mp3")
    if a=="all falls down":
        st.audio("M500003RyzPE2Z9k88.mp3",format="audio/mp3")
    if a=="darkside":
        st.audio("2635590352.mp3",format="audio/mp3")
        

if page=="历史":
    page1()
elif page =="网站":
    page2()
elif page=="处理图片":
    page3()
elif page=="词典":
    page4()
elif page=="留言":
    page5()
elif page=="安利音乐":
    page6()

