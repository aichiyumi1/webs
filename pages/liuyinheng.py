import streamlit as st
from PIL import Image

user_name = None
page = st.sidebar.radio('我的主页',[':rose:介绍',':sports_medal:上传',':gem:评论区',':man:教程','热门上传','test','test2'])

def login():
    user_name = None
    Login = False
    username = st.text_input("请输入用户名")
    if username:
        usercode = st.text_input("请输入密码")
        if usercode:
            with open("user_login.txt","r",encoding="utf-8") as f:
                login_text = f.read().split("\n")
            for i in range(len(login_text)):
                login_text[i] = login_text[i].split("#")
            for text in login_text:
                if text[0] == username and text[1] == usercode:
                    Login = True
            if Login:
                st.write("登陆成功")
                user_name = username
            else:
                st.write("登陆失败，请重新检查您的用户名和密码并刷新网页")

def register():
    Name = False
    user_name = None
    username = st.text_input("请输入用户名")
    if username:
        usercode = st.text_input("请输入密码")
        if usercode:
            check = st.text_input("请再次输入密码")
            if check:
                if usercode == check:
                    with open("user_login.txt", "r", encoding="utf-8") as f:
                        text = f.read().split("\n")
                    for i in range(len(text)):
                        text[i] = text[i].split("#")
                        if text[i][0] == username:
                            Name = True
                    if Name:
                        st.write("有重复的用户名，请刷新网页并重新登记用户名")
                    elif usercode == check:
                        question_1 = st.text_input("请输入安全问题1")
                        if question_1:
                            answer_1 = st.text_input("请输入安全答案1")
                            if answer_1:
                                question_2 = st.text_input("请输入安全问题2")
                                if question_2:
                                    answer_2 = st.text_input("请输入安全答案2")
                                    if answer_2:
                                        append_list = [username, usercode, question_1, answer_1, question_2, answer_2]
                                        text.append(append_list)
                                        with open("user_login.txt", "w", encoding="utf-8") as f:
                                            write_text = ''
                                            for i in range(len(text)):
                                                write_text += text[i][0] + "#" + text[i][1] + "#" + text[i][2] +"#" + text[i][3] + "#" + text[i][4] + "#" + text[i][5] + "\n"
                                            f.write(write_text)
                                        st.write("注册成功！密码club欢迎您！")
                                        user_name = username
                else:
                    st.write("确认密码和密码不符，请核对后再试")
def code():
    Name_number = None
    user_name = None
    username = st.text_input("请输入你的用户名")
    if user_name:
        with open("user_login.txt", "w", encoding="utf-8") as f:
            text = f.read().split("\n")
        for i in range(len(text)):
            text[i] = text[i].split("#")
            if text[i][0] == username:
                Name_number = i
        if Name_number:
            st.write("接下来将进行安全检测")
            st.write(text[Name_number][2])
            answer_1 = st.text_input("请作答")
            if answer_1:
                st.write(text[Name_number][4])
                answer_2 = st.text_input("请作答")
                if answer_2:
                    if answer_1 == text[Name_number][3] and answer_2 == text[Name_number][5]:
                        st.write("验证成功！您的密码是", text[Name_number][1])
                    else:
                        st.write("对不起，您的答案有误，请核对后重试")
        else:
            st.write("抱歉，未检测到您的用户名，若尚未注册请先注册。")

def page_1():
    st.image("slogan.jpg")
    st.write("Greetings!")
    st.text("声明")
    st.text("本网站旨为密码热爱者提供一个发表和交流的平台，全部开放,")
    st.text("大家可以在这里畅所欲言，但还请维持这个美好的网络环境哦~")
    st.text("                          --By 管理")
    st.text("---------------------------------------------------")
    st.text("介绍")
    st.text("加密分为几类。其中大家最耳熟能详的应该是凯撒密码,")
    st.text("即所有字母向前或向后移动固定的顺序，形成一组新的密")
    st.text("码。")
    st.text("当然，大多数符合密码都组合了超过2到3种，一般大家自制")
    st.text("的密码会附带提示，希望这段话能帮到你哦~")
def page_2():
    st.write("上传")
    code = st.text_input("请输入正文")
    with open("uploaded.txt") as f:
        text = f.read.split("\n")
    if code:
        code_uploaded = user_name + "#" + code
        text.append(code_uploaded)
        with open("uploaded.txt", "w") as f:
            text_uploaded = ''
            for i in range(len(text)):
                text_uploaded += text[i] + "\n"
            f.write(text_uploaded)
        st.write("谜题上传成功")
    
def page_3():
    st.write("我的评论区")
    with open("leave_messages.txt", "r", encoding="utf-8") as f:
        message_list = f.read().split("\n")
    for i in range(len(message_list)):
        message_list[i] = message[i].split("#")
    for i in message_list:
        with st.chat_message(i[1]):
            st.write(i[1] + ":" + i[2])
    name = user_name
    new_message = st.text_input("想要说的话")
    if st.button("留言"):
        message_list.append(str(int(message_list[-1][0])+1), name, new_message)
        with open("leave_message.txt", "w", encoding="utf-8")as f:
            message = ''
            for i in message_list:
                message += i[0] + "#" + i[1] + "\n"
            message = message[:-1]
            f.write(message)
def page_4():
    with open("user_chat.txt", "r", encoding="utf-8") as f:
        text = f.read().split("\n")
    for i in range(len(text)):
        text[i] = text[i].split("#")
        if text[i][1] == user_name:
            st.write(i[0], ":", i[2])
    if st.button("发私信"):
        goal = st.text_input("你要跟谁说？")
        if goal:
            for i in range(len(text)):
                if goal == i[1]:
                    message = st.text_input("说点什么吧")
                    if message:
                        with open("user_chat.txt", "w", encoding="utf-8") as f:
                            text_uploaded = ''
                            for i in range(len(text)):
                                text_uploaded += text[0] + "#"  + text[1] + "#" + text[2] + "\n"
                            f.write(text_uploaded)
            st.write("发送成功~")
                    
def page_5():
    st.write("图片处理")
    file = st.file_uploader("上传图片", type=["png","jpg","jpeg"])
    if file:
        file_name = file.name
        file_type = file.type
        file_size = file.size
        tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(file)
        with tab2:
            st.image(change_color(file,0,2,1))
        with tab3:
            st.image(change_color(file,1,2,0))
        with tab4:
            st.image(change_color(file,2,1,0))
def page_6():
    st.write("智能词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_list:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt","w",encoding="utf-8") as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + "#" + str(v) + "\n"
            message = message[:-1]
            f.write(message)
        st.write("查询次数:", times_dict[n])
        if word == "Python":
            st.code("""print("hello world!")""")
        if word == "snow":
            st.snow()
        if word == "birthday":
            st.balloons()

def page_7():
    with open("uploaded.txt", "r", encoding="utf-8")as f:
        code = f.read().split("\n")
    for i in range(len(code)):
        code[i] = code[i].split("#")
        st.write("由", code[i][0], "大佬发布的谜题：")
        st.text(code[i][1])
        st.text("-------------------------------------------------------")

def page_login():
    st.write("上传或发言前，请先登录。")
    global user_name
    if st.button("登录"):   
        login()
    if st.button("注册"):
        register()

    if st.button("忘记密码？"):
        code()
            

def change_color(image,rc,gc,bc):
    width,height = image.size()
    image_array = image.load()
    for x in range(width):
        for y in range(height):
            r = image_array[x, y][rc]
            g = image_array[x, y][gc]
            b = image_array[x, y][bc]
    return image

if page == ":rose:介绍":
    page_1()
elif page == ":sports_medal:上传":
    if user_name:
        page_2()
    else:
        page_login()
elif page == ":gem:评论区":
    if user_name:
        page_3()
    else:
        page_login()
elif page == ":man:私聊":
    if user_name:
        page_4()
    else:
        page_login()
elif page == "test":
    page_5()
elif page == "test2":
    page_6()
elif page == "热门上传":
    page_7()