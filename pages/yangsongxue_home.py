"""我的首页"""
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['游戏推荐', '漫画推荐','小说推荐','我推的孩子','我的图片处理工具', '我的智慧词典', '我的留言区', '答题'])

def page1():
    '''游戏推荐'''
    with open('yangsongxue_霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('游戏推荐')
    st.write(' ')
    st.text('1.原神')
    st.image('yangsongxue_原神.jpg')
    st.text('懂得都懂，下一个')
    st.write('-----------------------------------')
    st.text('2.崩坏:星穹铁道')
    st.image('yangsongxue_崩铁.jpg')
    st.text('出了不到一年就拿奖就已经证明了它的实力')
    st.write('-----------------------------------')
    st.text('3.重返未来1999')
    st.image('yangsongxue_1999.jpg')
    st.text('画面精美，风格吸引，战斗不复杂，不骗氪，抽卡几率大')
    st.write('-----------------------------------')
    st.text('4.偶像梦幻祭')
    st.image('yangsongxue_es.jpg')
    st.text('"这里有偶像的一切!"49位偶像任君挑选')
    st.write('-----------------------------------')
    st.text('5.食物语')
    st.image('yangsongxue_食物语.jpg')
    st.text('美食化灵，是玩养成的')
    st.text('天杀的百田，食物语沒了拉你陪葬(bushi)')
    st.write('-----------------------------------')
    st.text('6.世界计划')
    st.image('yangsongxue_初音.jpg')
    st.text('沒有国服，但打歌手感好爽')
    st.write('-----------------------------------')
    st.text('7.以闪亮之名')
    st.image('yangsongxue_以闪.jpg')
    st.text('换裝游戏，能捏脸，能自己做衣服') 

def page2():
    '''漫画推荐'''
    st.write('漫画推荐')
    st.write(' ')
    st.text('1.某天成为公主')
    st.image('yangsongxue_公主.jpg')
    st.text('画风超绝的，剧情也很棒')
    st.write('-----------------------------------')
    st.text('2.我的同学都很奇怪')
    st.image('yangsongxue_同学.jpg')
    st.text('搞笑日常番')
    st.write('-----------------------------------')
    st.text('3.超赞同梦会')
    st.image('yangsongxue_同梦会.jpg')
    st.text('明明挺好看的，但沒什么人看')
    st.write('-----------------------------------')
    st.text('4.萌师在上')
    st.image('yangsongxue_萌师.jpg')
    st.text('主角超可爱的') 
    st.write('-----------------------------------')
    st.text('5.星梦偶像计划')
    st.image('yangsongxue_星梦.jpg')
    st.text('画风好，剧情棒，就是美人哥哥出场少') 
    
def page3():
    '''小说推荐'''
    st.write('小说推荐')
    st.write(' ')
    st.text('1.破云')
    st.text('如果说学校让我们远离毒品, 那么看完"破云", 我是真心厌恶毒品')
    st.write('-----------------------------------')
    st.text('2.破云2吞海')
    st.text('同上')
    st.write('-----------------------------------')
    st.text('3.破云3擒川')
    st.text('这个不是，沒有这本书，整个活而已')
    st.write('-----------------------------------')
    st.text('4.默读')
    st.text('把人心的冷漠﹑人性的扭曲描写得特別好')
    st.write('-----------------------------------')
    st.text('5.我在惊悚游戏里封神')
    st.text('还沒看完，但前面挺好看的')
    st.write('-----------------------------------')
    st.text('6.诡秘之主')
    st.text('朋友推荐的，前面有点慢热，但后面超精彩')
    st.write('-----------------------------------')

def page4():
    '''我推的孩子'''
    st.write('我推的孩子')
    st.write(' ')
    st.text('1.原神: ')
    st.image('yangsongxue_散.jpg')
    st.text('散兵')
    st.image('yangsongxue_风.jpg')
    st.text('(左至右)空﹑魈﹑万叶﹑平藏﹑温迪')
    st.image('yangsongxue_枫丹.jpg')
    st.text('菲米尼﹑琳妮特﹑林尼')
    st.image('yangsongxue_璃月.jpg')
    st.text('重云﹑行秋﹑胡桃﹑香菱')
    st.write('-----------------------------------')
    st.text('2.崩铁: ')
    st.image('yangsongxue_黑塔.jpg')
    st.text('黑塔')
    st.image('yangsongxue_银狼.jpg')
    st.text('银狼')
    st.image('yangsongxue_飲月.jpg')
    st.text('饮月')
    st.write('-----------------------------------')
    st.text('3.1999: ')
    st.image('yangsongxue_X.jpg')
    st.text('X')
    st.write('-----------------------------------')
    st.text('4.我的同学都很奇怪: ')
    st.image('yangsongxue_莱安.jpg')
    st.text('莱安')
    st.write('-----------------------------------')
    st.text('5.paradox live: ')
    st.image('yangsongxue_1Nm8.jpg')
    st.text('1Nm8')
    st.image('yangsongxue_cozmez.jpg')
    st.text('cozmez')
    st.write('-----------------------------------')
    st.text('6.绝对演绎: ')
    st.image('yangsongxue_含玨.jpg')
    st.text('李含玨')
    st.image('yangsongxue_叶瑾.jpg')
    st.text('叶瑾')
    st.write('-----------------------------------')
    st.text('7.世界计划: ')
    st.image('yangsongxue_nene.jpg')
    st.text('草薙宁宁')
    st.image('yangsongxue_toyo.jpg')
    st.text('青柳冬弥')
    st.image('yangsongxue_类.jpg')
    st.text('神代类')
    st.image('yangsongxue_杏.jpg')
    st.text('白石杏')
    st.image('yangsongxue_绘名.jpg')
    st.text('东云绘名')
    st.write('-----------------------------------')
    st.text('8.es: ')
    st.image('yangsongxue_mayoi.jpg')
    st.text('礼濑真宵')
    st.image('yangsongxue_泉.jpg')
    st.text('濑名泉')
    st.image('yangsongxue_飒马.jpg')
    st.text('神崎飒马')
    st.image('yangsongxue_rrss.jpg')
    st.text('日日树涉')
    st.image('yangsongxue_夏.jpg')
    st.text('逆先夏目')
    st.image('yangsongxue_日和.jpg')
    st.text('巴日和')
    st.write('-----------------------------------')
    st.text('9.食物语: ')
    st.image('yangsongxue_鲤.jpg')
    st.text('怀抱鲤')
    st.image('yangsongxue_子推.jpg')
    st.text('子推燕')
    st.text('') 
    st.text('因为我懒，所以有很多都沒写，反正不止这么点')
    
def page5():
    '''我的图片处理工具'''
    st.write(":volcano:图片換色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

def page6():
    '''我的智慧词典'''
    st.write(':blue智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数: ', times_dict[n])
        if word=='python':
            st.code('''
                    # 恭喜你触发彩蛋, 这是一行python代码
                    print('hello world')''')
        if word == 'snow':
            st.snow()
        if word == 'birthday':
            st.balloons()

def page7():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '我是一只社恐社恐鸟':
            with st.chat_message('🐦'):
                st.write(i[1],':',i[2])
        elif i[1] == '一只路过喵':
            with st.chat_message('😺'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['我是一只社恐社恐鸟', '一只路过喵'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page8():
    st.write('如果你推被人骂？你会')
    cb1 = st.checkbox('一拳把屏幕打穿')
    cb2 = st.checkbox('顺着网线偷他家')
    cb3 = st.checkbox('祝他次次保底')
    cb4 = st.checkbox('让他被他推讨厌')
    m = [cb1, cb2]
    n = [cb3, cb4]
    if st.button('确认答案'):
        if True in m:
            st.write('你好暴力哎~')
        elif True in n:
            st.write('你好恶毒哎~')
        else:
            st.write('？你推都被人骂了，你居然无动于衷？')
        
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '游戏推荐':
    page1()
elif page == '漫画推荐':
    page2()
elif page == '小说推荐':
    page3()
elif page == '我推的孩子':
    page4()
elif page == '我的图片处理工具':
    page5()
elif page == '我的智慧词典':
    page6()
elif page == '我的留言区':
    page7()
elif page == '答题':
    page8()