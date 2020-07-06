import requests
from bs4 import BeautifulSoup


def scraip(num):

    # エラーコードの初期化
    error = 0

    ###########################################
    # ネット競馬ログイン
    ###########################################
    # メールアドレスとパスワードの指定
    USER = "*******"
    PASS = "*******"

    login_info = {
        "login_id": USER,
        "pswd": PASS,
    }

    session = requests.session()

    url_login = "https://regist.netkeiba.com/account/?pid=login&action=auth"

    ses = session.post(url_login, data=login_info)

    print("ネット競馬ログインの完了")

    ###############################################
    # 馬の数の取得
    ###############################################
    # データ分析・基本に移動

    data_analysis_basic_url = 'https://nar.netkeiba.com/race/data.html?race_id=' + num + '&mode=coursedata&rf=shutuba_submenu'
    res = session.get(data_analysis_basic_url)
    soup = BeautifulSoup(res.content, "html.parser")
    basic_tag = soup.find_all('td')
    for i in range(len(basic_tag)):
        basic_tag[i] = basic_tag[i].text
        # print(str(i)+":",end="")
        # print(basic_tag[i])
    horse_num_max = int(len(basic_tag) / 49)
    #print(horse_num_max)

    # 馬の数が0の場合エラーで返す
    if horse_num_max==0:
        return "error"

    # 分析データを格納するリストの作成
    racedata = [[0 for column in range(64)] for row in range(horse_num_max)]

    print("馬の数の取得の完了")

    ###############################################
    # データ分析(基本)の取得
    ###############################################
    for i in range(horse_num_max):
        # 馬番の格納
        racedata[i][0] = i + 1
        # 馬名の格納
        horse_name = basic_tag[i * 49 + 2].split('\n')
        racedata[i][1] = horse_name[1]

        racedata[i][2] = basic_tag[i * 49 + 6]
        racedata[i][3] = basic_tag[i * 49 + 7]
        racedata[i][4] = basic_tag[i * 49 + 8]
        racedata[i][5] = basic_tag[i * 49 + 9]
        racedata[i][6] = basic_tag[i * 49 + 10]
        racedata[i][7] = basic_tag[i * 49 + 11].rstrip('%')
        racedata[i][8] = basic_tag[i * 49 + 12].rstrip('%')
        racedata[i][9] = basic_tag[i * 49 + 13].rstrip('%')
        racedata[i][10] = basic_tag[i * 49 + 14].rstrip('%')
        racedata[i][11] = basic_tag[i * 49 + 15].rstrip('%')
        racedata[i][12] = basic_tag[i * 49 + 17]
        racedata[i][13] = basic_tag[i * 49 + 18]
        racedata[i][14] = basic_tag[i * 49 + 19]
        racedata[i][15] = basic_tag[i * 49 + 20]
        racedata[i][16] = basic_tag[i * 49 + 21]
        racedata[i][17] = basic_tag[i * 49 + 22].rstrip('%')
        racedata[i][18] = basic_tag[i * 49 + 23].rstrip('%')
        racedata[i][19] = basic_tag[i * 49 + 24].rstrip('%')
        racedata[i][20] = basic_tag[i * 49 + 25].rstrip('%')
        racedata[i][21] = basic_tag[i * 49 + 26].rstrip('%')
        racedata[i][22] = basic_tag[i * 49 + 28]
        racedata[i][23] = basic_tag[i * 49 + 29]
        racedata[i][24] = basic_tag[i * 49 + 30]
        racedata[i][25] = basic_tag[i * 49 + 31]
        racedata[i][26] = basic_tag[i * 49 + 32]
        racedata[i][27] = basic_tag[i * 49 + 33].rstrip('%')
        racedata[i][28] = basic_tag[i * 49 + 34].rstrip('%')
        racedata[i][29] = basic_tag[i * 49 + 35].rstrip('%')
        racedata[i][30] = basic_tag[i * 49 + 36].rstrip('%')
        racedata[i][31] = basic_tag[i * 49 + 37].rstrip('%')
        racedata[i][32] = basic_tag[i * 49 + 39]
        racedata[i][33] = basic_tag[i * 49 + 40]
        racedata[i][34] = basic_tag[i * 49 + 41]
        racedata[i][35] = basic_tag[i * 49 + 42]
        racedata[i][36] = basic_tag[i * 49 + 43]
        racedata[i][37] = basic_tag[i * 49 + 44].rstrip('%')
        racedata[i][38] = basic_tag[i * 49 + 45].rstrip('%')
        racedata[i][39] = basic_tag[i * 49 + 46].rstrip('%')
        racedata[i][40] = basic_tag[i * 49 + 47].rstrip('%')
        racedata[i][41] = basic_tag[i * 49 + 48].rstrip('%')

    print("データ分析(基本)の取得の完了")

    ###############################################
    # データ分析(距離)の取得
    ###############################################
    data_analysis_distance_url = 'https://nar.netkeiba.com/race/data.html?race_id=' + num + '&mode=distance&rf=shutuba_submenu'
    res = session.get(data_analysis_distance_url)
    soup = BeautifulSoup(res.content, "html.parser")
    distance_tag = soup.find_all('td')
    for i in range(len(distance_tag)):
        distance_tag[i] = distance_tag[i].text
        # print(str(i)+":",end="")
        # print(distance_tag[i])

    if len(distance_tag) != 0:
        for i in range(horse_num_max):
            racedata[i][42] = distance_tag[i * 60 + 50]
            racedata[i][43] = distance_tag[i * 60 + 51]
            racedata[i][44] = distance_tag[i * 60 + 52]
            racedata[i][45] = distance_tag[i * 60 + 53]
            racedata[i][46] = distance_tag[i * 60 + 54]
            racedata[i][47] = distance_tag[i * 60 + 55].rstrip('%')
            racedata[i][48] = distance_tag[i * 60 + 56].rstrip('%')
            racedata[i][49] = distance_tag[i * 60 + 57].rstrip('%')
            racedata[i][50] = distance_tag[i * 60 + 58].rstrip('%')
            racedata[i][51] = distance_tag[i * 60 + 59].rstrip('%')
    else:
        for i in range(horse_num_max):
            racedata[i][42] = "-"
            racedata[i][43] = "-"
            racedata[i][44] = "-"
            racedata[i][45] = "-"
            racedata[i][46] = "-"
            racedata[i][47] = "-"
            racedata[i][48] = "-"
            racedata[i][49] = "-"
            racedata[i][50] = "-"
            racedata[i][51] = "-"
        print("＊" + num + "Rの距離別成績がありません")
        error = 1

    # for i in range(len(racedata)):
    #    print(racedata[i])

    print("データ分析(距離)の取得の完了")

    ###############################################
    # タイム指数(タイム指数表からの取得) 注意：tagの個数が違う可能性
    ###############################################
    timeindex_all_url = 'https://nar.netkeiba.com/race/speed.html?race_id=' + num + '&rf=shutuba_submenu'
    res = session.get(timeindex_all_url)
    soup = BeautifulSoup(res.content, "html.parser")
    timeindex_tag = soup.find_all('td')
    for i in range(len(timeindex_tag)):
        timeindex_tag[i] = timeindex_tag[i].text
        # print(str(i) + ":" + timeindex_tag[i])

    # タイム指数表の列数の計算
    tablenum = len(timeindex_tag) // horse_num_max

    if len(timeindex_tag) != 0:
        for i in range(horse_num_max):
            for j in range(7, 14):
                timeindex_tag[i * tablenum + j] = timeindex_tag[i * tablenum + j].rstrip("*\n")
                temp = timeindex_tag[i * tablenum + j]
                if temp[-1] == "-" or temp[-1] == "未":
                    racedata[i][45 + j] = "-"
                elif '-' in temp:
                    timelist = temp.split("-")
                    racedata[i][45 + j] = "-" + timelist[1]
                else:
                    racedata[i][45 + j] = temp[-2:]
    else:
        for i in range(horse_num_max):
            racedata[i][52] = "-"
            racedata[i][53] = "-"
            racedata[i][54] = "-"
            racedata[i][55] = "-"
            racedata[i][56] = "-"
            racedata[i][57] = "-"
            racedata[i][58] = "-"
        print("＊", end="")
        error = 1

    # for i in range(len(racedata)):
    #    print(racedata[i])

    print("タイム指数(タイム指数表からの取得)の完了")

    ###############################################
    # タイム指数(馬ページからの取得)
    ###############################################
    horse_url_tag = soup.find_all('td', {'class': 'Horse_Name'})
    if len(horse_url_tag) != 0:
        for i in range(horse_num_max):
            # テスト用
            # print(str(i) + ":" + str(horse_url_tag[i]))
            horse_url = str(horse_url_tag[i])
            horsesplit = horse_url.split('"')
            horse_url = horsesplit[3]
            res = session.get(horse_url)
            soup = BeautifulSoup(res.content, "html.parser")
            horsetimeindex_tag = soup.find_all('td', {
                'class': ['index1 txt_right', 'index2 txt_right', 'index3 txt_right', 'index4 txt_right',
                          'index5 txt_right', 'index6 txt_right']})
            for j in range(5):
                try:
                    horsetimeindex_tag[j * 2 + 1] = horsetimeindex_tag[j * 2 + 1].text
                    horsetimeindex_tag[j * 2 + 1] = horsetimeindex_tag[j * 2 + 1].lstrip("\n")
                    horsetimeindex_tag[j * 2 + 1] = horsetimeindex_tag[j * 2 + 1].rstrip("\n")
                    racedata[i][59 + j] = horsetimeindex_tag[j * 2 + 1]
                except:
                    racedata[i][59 + j] = "-"
    else:
        for i in range(horse_num_max):
            for j in range(5):
                racedata[i][59 + j] = "-"
        print(num + "Rのタイム指数はありません")
        error = 1

    # for i in range(len(racedata)):
    #    print(racedata[i])

    print("タイム指数(馬ページからの取得)の完了")

    return racedata
