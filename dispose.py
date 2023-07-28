import csv
import re
from bs4 import BeautifulSoup
import os


def add_title():

    # 写入表头
    list_title = []
    list_title.append(
        ["用户名", "ID", "注册日期", "IP属地", "个人简介", "在看电影数", "想看电影数", "看过电影数", "片单数",
         "在读书数",
         "想读书数", "读过书数", "书单数", "在听音乐数", "想听音乐数", "听过音乐数", "歌单数", "评论数", "在看舞台剧数",
         "想看舞台剧数", "看过舞台剧数", "常去小组数", "参加同城活动数", "感兴趣同城活动数", "关注数", "被关注数",
         "豆列数",
         "相册创建数", "相册关注数", "想玩游戏数", "玩过游戏数", "在玩游戏数",
         "用过移动应用数", "作品数"])
    c = open("test.csv", 'a', newline='', encoding='utf-8')
    writer = csv.writer(c)
    writer.writerows(list_title)
    c.close()


def html_to_csv():

    fp = open('1.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')

    try:
        User_name = re.sub(" ", "", soup.select('title')[0].text)
        User_name = re.sub("\n", "", User_name)  # todo 用户名
    except:
        User_name = None


    # 基本信息
    basic_info = soup.select('.user-info > .pl')
    if basic_info:
        basic_info = basic_info[0].text
    else:
        basic_info = "\n\n\n"





    # basic_info = soup.select('.user-info > .pl')[0].text
    basic_info = re.sub(" ", "", basic_info)



    user_info = []
    user_info = basic_info.split('\n')

    user_info[1] = re.sub(" ", "", user_info[1])  # 清洗空格
    ID = user_info[1]  # todo ID

    user_info[2] = re.sub(" ", "", user_info[2])  # 清洗空格
    user_info[2] = re.sub("加入", "", user_info[2])
    Register_date = user_info[2]  # todo 注册日期



    try:
        user_info[3] = re.sub(" ", "", user_info[3])  # 清洗空格
        user_info[3] = re.sub("IP属地：", "", user_info[3])
        IP = user_info[3]  # todo IP属地
    except:
        IP = None

    try:
        Intro = soup.select('textarea')[0].text  # todo 个人简介
    except:
        Intro = None

    try:
        movie_info = re.sub(" ", "", soup.select(
            'div#movie > h2 > span.pl')[0].text)
        movie_info = re.sub("\n", "", movie_info)
        movie_info = re.sub("·", "\n", movie_info)
        movie = []
        movie = movie_info.split('\n')
    except:
        Ing_movie = 0
        Want_movie = 0
        Ed_movie = 0
        Dan_movie = 0
    try:
        Ing_movie = re.sub("\D", "", movie[0])  # todo 在看电影数
    except:
        Ing_movie = 0
    try:
        Want_movie = re.sub("\D", "", movie[1])  # todo 想看电影数
    except:
        Want_movie = 0
    try:
        Ed_movie = re.sub("\D", "", movie[2])  # todo 看过电影数
    except:
        Ed_movie = 0
    try:
        Dan_movie = re.sub("\D", "", movie[3])  # todo 片单数
    except:
        Dan_movie = 0

    try:
        book_info = re.sub(" ", "", soup.select(
            'div#book > h2 > span.pl')[0].text)
        book_info = re.sub("\n", "", book_info)
        book_info = re.sub("·", "\n", book_info)
        book = []
        book = book_info.split('\n')
    except:
        Ing_book = 0
        Want_book = 0
        Ed_book = 0
        Dan_book = 0
    try:
        Ing_book = re.sub("\D", "", book[0])  # todo 在读书数
    except:
        Ing_book = 0
    try:
        Want_book = re.sub("\D", "", book[1])  # todo 想读书数
    except:
        Want_book = 0
    try:
        Ed_book = re.sub("\D", "", book[2])  # todo 读过书数
    except:
        Ed_book = 0
    try:
        Dan_book = re.sub("\D", "", book[3])  # todo 书单数
    except:
        Dan_book = 0

    try:
        music_info = re.sub(" ", "", soup.select(
            'div#music > h2 > span.pl')[0].text)
        music_info = re.sub("\n", "", music_info)
        music_info = re.sub("·", "\n", music_info)
        music = []
        music = music_info.split('\n')
    except:
        Ing_music = 0
        Want_music = 0
        Ed_music = 0
        Dan_music = 0
    try:
        Ing_music = re.sub("\D", "", music[0])  # todo 在听音乐数
    except:
        Ing_music = 0
    try:
        Want_music = re.sub("\D", "", music[1])  # todo 想听音乐数
    except:
        Want_music = 0
    try:
        Ed_music = re.sub("\D", "", music[2])  # todo 听过音乐数
    except:
        Ed_music = 0
    try:
        Dan_music = re.sub("\D", "", music[3])  # todo 歌单数
    except:
        Dan_music = 0

    try:
        review = re.sub(" ", "", soup.select(
            'div#review > h2 > span.pl')[0].text)
        review = re.sub("\n", "", review)
        review = re.sub("\D", "", review)  # todo 评论数
    except:
        review = 0

    try:
        drama_info = re.sub(" ", "", soup.select(
            'div#drama > h2 > span.pl')[0].text)
        drama_info = re.sub("\n", "", drama_info)
        drama_info = re.sub("·", "\n", drama_info)
        drama = []
        drama = drama_info.split('\n')
    except:
        Ing_drama = 0
        Want_drama = 0
        Ed_drama = 0
        Dan_drama = 0
    try:
        Ing_drama = re.sub("\D", "", drama[0])  # todo 在看舞台剧数
    except:
        Ing_drama = 0
    try:
        Want_drama = re.sub("\D", "", drama[1])  # todo 想看舞台剧数
    except:
        Want_drama = 0
    try:
        Ed_drama = re.sub("\D", "", drama[2])  # todo 看过舞台剧数
    except:
        Ed_drama = 0

    try:
        group_info = re.sub(" ", "", soup.select(
            'div#group > h2')[0].text)
        group_info = re.sub("\n", "", group_info)
        group = []
        group = group_info.split('\n')
    except:
        Group = 0
    try:
        Group = re.sub("\D", "", group[0])  # todo 常去的小组数
    except:
        Group = 0

    try:
        event_info = re.sub(" ", "", soup.select(
            'div#event > h2 > span.pl')[0].text)
        event_info = re.sub("\n", "", event_info)
        event_info = re.sub("·", "\n", event_info)
        event = []
        event = event_info.split('\n')
    except:
        Ing_event = 0
        Want_event = 0

    try:
        Ing_event = re.sub("\D", "", event[0])  # todo 参加同城活动数
    except:
        Ing_event = 0
    try:
        Want_event = re.sub("\D", "", event[1])  # todo 感兴趣同城活动数
    except:
        Want_event = 0

    try:
        Focuser = re.sub(" ", "", soup.select(
            'div#friend > h2 > span.pl > a')[0].text)
        Focuser = re.sub("\n", "", Focuser)
        Focuser = re.sub("\D", "", Focuser)  # todo 关注数
    except:
        Focuser = 0

    try:
        Follower = re.sub(" ", "", soup.select(
            'p.rev-link > a')[0].text)
        Follower = re.sub("\n", "", Follower)
        Follower = re.sub("\D", "", Follower)  # todo 被关注数
    except:
        Follower = 0

    try:
        Doulist = re.sub(" ", "", soup.select(
            'div#doulist > h2 > span.pl > a')[0].text)
        Doulist = re.sub("\n", "", Doulist)
        Doulist = re.sub("\D", "", Doulist)  # todo 豆列数
    except:
        Doulist = 0

    try:
        photo_info = re.sub(" ", "", soup.select(
            'div#photo > h2 > span.pl')[0].text)
        photo_info = re.sub("\n", "", photo_info)
        photo_info = re.sub("·", "\n", photo_info)
        photo = []
        photo = photo_info.split('\n')
    except:
        Ing_photo = 0
        Want_photo = 0

    try:
        Ing_photo = re.sub("\D", "", photo[0])  # todo 创建相册数
    except:
        Ing_photo = 0
    try:
        Want_photo = re.sub("\D", "", photo[1])  # todo 关注相册数
    except:
        Want_photo = 0

    try:
        game_info = re.sub(" ", "", soup.select(
            'div#game > h2 > span.pl')[0].text)
        game_info = re.sub("\n", "", game_info)
        game_info = re.sub("·", "\n", game_info)
        game = []
        game = game_info.split('\n')
    except:
        Ing_game = 0
        Want_game = 0
        Ed_game = 0

    try:
        Ing_game = re.sub("\D", "", game[2])  # todo 在玩游戏数
    except:
        Ing_game = 0
    try:
        Want_game = re.sub("\D", "", game[0])  # todo 想玩游戏数
    except:
        Want_game = 0

    try:
        Ed_game = re.sub("\D", "", game[1])  # todo 玩过游戏数
    except:
        Ed_game = 0

    try:
        app_info = re.sub(" ", "", soup.select(
            'div#apps > h2 > span.pl > a')[0].text)
        app_info = re.sub("\n", "", app_info)
        app_info = re.sub("\D", "", app_info)    # todo 用过应用数
    except:
        app_info = 0

    try:
        Port = re.sub(" ", "", soup.select(
            'div#portfolio > h2 > span.pl > a')[0].text)
        Port = re.sub("\n", "", Port)
        Port = re.sub("\D", "", Port)  # todo 作品数
    except:
        Port = 0

    # try:
    #     with open("user_comments.txt", "r", encoding='utf-8') as f:
    #         comments = f.read()  # 读取文本
    # except:
    #     comments = None

    trip_list = []
    trip_list.append(
        [User_name, ID, Register_date, IP, Intro, Ing_movie, Want_movie, Ed_movie, Dan_movie, Ing_book, Want_book, Ed_book,
         Dan_book, Ing_music, Want_music, Ed_music, Dan_music, review, Ing_drama, Want_drama, Ed_drama, Group, Ing_event,
         Want_event, Focuser, Follower, Doulist, Ing_photo, Want_photo, Want_game, Ed_game, Ing_game,
         app_info, Port])  # todo 输出

    # 将数据写入csv文件
    c = open("test.csv", 'a', newline='', encoding='utf-8')
    writer = csv.writer(c)
    writer.writerows(trip_list)
