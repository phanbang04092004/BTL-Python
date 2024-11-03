from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from player import Player
from player import Player_Manager

player_manager = Player_Manager()

def validdata(n):
    if n == '': return "N/a"
    return float(n)

def GetDataFromWeb(url, Xpath_player, Data_Name):
    driver = webdriver.Chrome()
    driver.get(url)

    resultPlayerData = []
    try:
        time.sleep(5)
        table2 = driver.find_element(By.XPATH, Xpath_player)
        rows2 = table2.find_elements(By.TAG_NAME, 'tr')

        for row in rows2:  # Bỏ qua hàng tiêu đề
            cols = row.find_elements(By.TAG_NAME, 'td')
            data = []
            for id, play in enumerate(cols[:-1]):
                if id == 1:
                    a = play.text.strip().split()
                    if len(a) == 2:
                        data.append(a[1])
                    else:
                        data.append(play.text.strip())
                else:
                    s = play.text.strip()
                    if id >= 4:
                        s = s.replace(",", "")
                        s = validdata(s)
                    data.append(s)
            if len(data) != 0: resultPlayerData.append(data)

    finally:
        driver.quit()
        print("Finish Page " + DataName)
    return resultPlayerData


url = "https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats"
xpath_player = '//*[@id="stats_standard"]'
DataName = "Standard"
list_player_result = GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p = player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p == None:
        new_p=Player(i[0],i[1],i[2],i[3],i[4])
        #bo qua i5 vi i5 la nam sinh
        new_p.setPlaying_time(i[6:9])
        #bo qua i9
        new_p.setPerformance([i[13],i[14],i[11],i[16],i[17]])
        new_p.setExpected(i[18:21])
        #bo qua i22
        new_p.setProgression(i[22:25])
        new_p.setPer90(i[25:])
        player_manager.add_Player(new_p)
player_manager.filtering()



url = 'https://fbref.com/en/comps/9/2023-2024/keepers/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_keeper"]'
DataName = "Goalkeeping"
list_player_result = GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setGoalkeeping(i[10:20],i[20:])


url = 'https://fbref.com/en/comps/9/2023-2024/shooting/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_shooting"]'
DataName = "Shooting"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setShooting(i[7:19],i[19:])


url = 'https://fbref.com/en/comps/9/2023-2024/passing/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_passing"]'
DataName = "Passing"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPassing(i[7:12],i[12:15],i[15:18],i[18:21],i[21:])


url = 'https://fbref.com/en/comps/9/2023-2024/passing_types/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_passing_types"]'
DataName = "Pass Types"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPassTypes(i[8:16],i[16:19],i[19:22])



url = 'https://fbref.com/en/comps/9/2023-2024/gca/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_gca"]'
DataName = "Goal and Shot Creation"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)


for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setGoalShotCreation(i[7:9],i[9:15],i[15:17],i[17:23])


url = 'https://fbref.com/en/comps/9/2023-2024/defense/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_defense"]'
DataName = "Defensive Actions"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setDefensiveActions(i[7:12],i[12:16],i[16:23])



url = 'https://fbref.com/en/comps/9/2023-2024/possession/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_possession"]'
DataName = "Possession"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPossession(i[7:14],i[14:19],i[19:27],i[27:29])


url = 'https://fbref.com/en/comps/9/2023-2024/playingtime/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_playing_time"]'
DataName = "Playing Time"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)

for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPlayingTimeDetail(i[11:14],i[14:17],i[17:20],i[23:25])


url = 'https://fbref.com/en/comps/9/2023-2024/misc/2023-2024-Premier-League-Stats'
xpath_player = '//*[@id="stats_misc"]'
DataName = "Miscellaneous"
list_player_result= GetDataFromWeb(url,xpath_player, DataName)


for i in list_player_result:
    p=player_manager.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setMiscStats(i[10:14]+i[18:20],i[20:23])

player_manager.sortingByName()


import csv
from tieu_de import header, row

# Đường dẫn lưu file CSV
file_path = 'C:/Users/Admin/OneDrive/Tài liệu/python/Bai_Tap_Lon/data/result.csv'

# Mở file CSV và ghi dữ liệu
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Ghi tiêu đề (header)
    writer.writerow(header)
    
    # Ghi dữ liệu của các cầu thủ
    for player in player_manager.list_player:
        r = row(player)
        writer.writerow(r)

print("Exam 1 Success - Player Data Saved as CSV")
