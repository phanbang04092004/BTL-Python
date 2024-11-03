
# Tạo tiêu đề CSV từ tất cả các thuộc tính của Player
header = [
    "name","nation", "team", "position", "age",
    # Playing Time
    "matches_played", "starts", "minutes",
    # Performance
    "non_penalty_goals", "penalty_goals", "assists", "yellow_cards", "red_cards",
    # Expected
    "xG", "npxG", "xAG",
    # Progression
    "PrgC", "PrgP", "PrgR",
    # Per 90 minutes
    "Per_90_Gls", "Per_90_Ast", "Per_90_G+A", "Per_90_G-PK", "Per_90_G+A-PK",
    "Per_90_xG", "Per_90_xAG", "Per_90_xG+xAG", "Per_90_npxG", "Per_90_npxG+xAG",
    # Goalkeeping
    "GA", "GA90", "SoTA", "Saves", "Save%", "W", "D", "L", "CS", "CS%",
    # Goalkeeping Penalty Kicks
    "PKatt", "PKA", "PKsv", "PKm", "GK_Save%",
    # Shooting Standard
    "Gls", "Sh", "SoT", "SoT%", "Sh/90", "SoT/90", "G/Sh", "G/SoT", "Dist", "FK", "PK", "PKatt",
    # Shooting Expected
    "xG_shooting", "npxG_shooting", "npxG/Sh", "G-xG", "np:G-xG",
    # Passing Total
    "Pass_Cmp", "Pass_Att", "Pass_Cmp%", "TotDist", "PrgDist",
    # Passing Short
    "Short_Cmp", "Short_Att", "Short_Cmp%",
    # Passing Medium
    "Medium_Cmp", "Medium_Att", "Medium_Cmp%",
    # Passing Long
    "Long_Cmp", "Long_Att", "Long_Cmp%",
    # Expected Passing
    'Ast',"xAG", "xA", "A-xAG", "KP", "1/3", "PPA", "CrsPA", "PrgP",
    # Pass Types
    "Pass_Live", "Pass_Dead", "Pass_FK", "Pass_TB", "Pass_Sw", "Pass_Crs", "Pass_TI", "Pass_CK",
    # Pass Corner Kicks
    "In","Out","Str",
    # Pass Outcomes
    "Pass_Cmp_outcome", "Pass_Off", "Pass_Blocks",
    # Goal and Shot Creation SCA
    "SCA","SCA90",
    # Goal and Shot Creation SCA Types
    "SCA_PassLive", "SCA_PassDead","SCA_TO", "SCA_Sh", "SCA_Fld", "SCA_Def",
    # Goal and Shot Creation GCA
    "GCA", "GCA90",
    # Goal and Shot Creation GCA Types
    "GCA_PassLive", "GCA_PassDead","GCA_TO", "GCA_Sh", "GCA_Fld", "GCA_Def",
    # Defensive Actions Tackles
    "Tkl", "TklW", "Def_3rd", "Mid_3rd", "Att_3rd",
    # Defensive Actions Challenges
    "Challenges_Tkl", "Challenges_Att", "Challenges_Tkl%", "Challenges_Lost",
    # Defensive Actions Blocks
    "Blocks","Blocks_Sh","Blocks_Pass","Blocks_Int","Blocks_Tkl+Int","Blocks_Clr","Blocks_Err",
    # Possession Touches
    "Touches", "Def_Pen", "Def_3rd", "Mid_3rd", "Att_3rd", "Att_Pen", "Live_Touches",
    # Possession Take-ons
    "Take_Att", "Take_Succ", "Take_Succ%", "Take_Tkld", "Take_Tkld%",
    # Possession Carries
    "Carries", "Carries_TotDist", "Carries_ProDist", "Carries_ProgC", "Carries_1/3", "Carries_CPA", "Carries_Mis", "Carries_Dis",
    # Possession Receiving
    "Receiving_Rec", "Receiving_PrgR",
    # Playing Time Starts
    "Starts", "Mn/Start" ,"Compl" ,
    # Playing Time Subs
    "Subs" ,"Mn/Sub" ,"unSub" , 
    # Playing Time Team Success
    "PPm", "onG", "onGA", 
    # Playing Time Team Success xG
    "onxG", "onxGA",
    # Miscellaneous Stats
    "Performance_Fls", "Performance_Fld", "Performance_Off", "Performance_Crs", "Performance_OG", "Performance_Recov",
    "Aerial_Won", "Aerial_Lost", "Aerial_Won%"
]

def row(player):
    return [
    player.name,player.nation, player.team, player.position, player.age,
    # Playing Time
    player.playing_time["matches_played"], player.playing_time["starts"], player.playing_time["minutes"],
    # Performance
    player.performance["non_penalty_goals"], player.performance["penalty_goals"], player.performance["assists"],
    player.performance["yellow_cards"], player.performance["red_cards"],
    # Expected
    player.expected["xG"], player.expected["npxG"], player.expected["xAG"],
    # Progression
    player.progression["PrgC"], player.progression["PrgP"], player.progression["PrgR"],
    # Per 90 minutes
    player.per_90["Gls"], player.per_90["Ast"], player.per_90["G+A"], player.per_90["G-PK"],
    player.per_90["G+A-PK"], player.per_90["xG"], player.per_90["xAG"], player.per_90["xG+xAG"],
    player.per_90["npxG"], player.per_90["npxG+xAG"],
    # Goalkeeping Performance
    player.goalkeeping["Performance"]["GA"], player.goalkeeping["Performance"]["GA90"],
    player.goalkeeping["Performance"]["SoTA"], player.goalkeeping["Performance"]["Saves"],
    player.goalkeeping["Performance"]["Save%"], player.goalkeeping["Performance"]["W"],
    player.goalkeeping["Performance"]["D"], player.goalkeeping["Performance"]["L"],
    player.goalkeeping["Performance"]["CS"], player.goalkeeping["Performance"]["CS%"],
    # Goalkeeping Penalty Kicks
    player.goalkeeping["Penalty Kicks"]["PKatt"], player.goalkeeping["Penalty Kicks"]["PKA"],
    player.goalkeeping["Penalty Kicks"]["PKsv"], player.goalkeeping["Penalty Kicks"]["PKm"],
    player.goalkeeping["Penalty Kicks"]["Save%"],
    # Shooting Standard
    player.shooting["Standard"]["Gls"], player.shooting["Standard"]["Sh"],
    player.shooting["Standard"]["SoT"], player.shooting["Standard"]["SoT%"],
    player.shooting["Standard"]["Sh/90"], player.shooting["Standard"]["SoT/90"],
    player.shooting["Standard"]["G/Sh"], player.shooting["Standard"]["G/SoT"],
    player.shooting["Standard"]["Dist"], player.shooting["Standard"]["FK"],
    player.shooting["Standard"]["PK"], player.shooting["Standard"]["PKatt"],
    # Shooting Expected
    player.shooting["Expected"]["xG"], player.shooting["Expected"]["npxG"],
    player.shooting["Expected"]["npxG/Sh"], player.shooting["Expected"]["G-xG"],
    player.shooting["Expected"]["np:G-xG"],
    # Passing Total
    player.passing["Total"]["Cmp"], player.passing["Total"]["Att"],
    player.passing["Total"]["Cmp%"], player.passing["Total"]["TotDist"],
    player.passing["Total"]["PrgDist"],
    # Passing Short
    player.passing["Short"]["Cmp"], player.passing["Short"]["Att"],
    player.passing["Short"]["Cmp%"],
    # Passing Medium
    player.passing["Medium"]["Cmp"], player.passing["Medium"]["Att"],
    player.passing["Medium"]["Cmp%"],
    # Passing Long
    player.passing["Long"]["Cmp"], player.passing["Long"]["Att"],
    player.passing["Long"]["Cmp%"],
    # Expected Passing
    player.passing["Expected"]["Ast"], player.passing["Expected"]["xAG"],
    player.passing["Expected"]["xA"], player.passing["Expected"]["A-xAG"],
    player.passing["Expected"]["KP"], player.passing["Expected"]["1/3"],
    player.passing["Expected"]["PPA"], player.passing["Expected"]["CrsPA"],
    player.passing["Expected"]["PrgP"],
    # Pass Types
    player.pass_types["Pass Types"]["Live"], player.pass_types["Pass Types"]["Dead"],
    player.pass_types["Pass Types"]["FK"], player.pass_types["Pass Types"]["TB"],
    player.pass_types["Pass Types"]["Sw"], player.pass_types["Pass Types"]["Crs"],
    player.pass_types["Pass Types"]["TI"], player.pass_types["Pass Types"]["CK"],
    # Pass Corner Kicks
    player.pass_types["Corner Kicks"]["In"],player.pass_types["Corner Kicks"]["Out"],player.pass_types["Corner Kicks"]["Str"],
    # Pass Outcomes
    player.pass_types["Outcomes"]["Cmp"], player.pass_types["Outcomes"]["Off"],
    player.pass_types["Outcomes"]["Blocks"],
    # Goal and Shot Creation 
    player.goal_shot_creation["SCA"]["SCA"],player.goal_shot_creation["SCA"]["SCA90"],

    player.goal_shot_creation["SCA Types"]["PassLive"],player.goal_shot_creation["SCA Types"]["PassDead"],player.goal_shot_creation["SCA Types"]["TO"],
    player.goal_shot_creation["SCA Types"]["Sh"],player.goal_shot_creation["SCA Types"]["Fld"],player.goal_shot_creation["SCA Types"]["Def"],

    player.goal_shot_creation["GCA"]["GCA"],player.goal_shot_creation["GCA"]["GCA90"],

    player.goal_shot_creation["GCA Types"]["PassLive"],player.goal_shot_creation["GCA Types"]["PassDead"],player.goal_shot_creation["GCA Types"]["TO"],
    player.goal_shot_creation["GCA Types"]["Sh"],player.goal_shot_creation["GCA Types"]["Fld"],player.goal_shot_creation["GCA Types"]["Def"],
    # Defensive Actions
    player.defensive_actions["Tackles"]["Tkl"], player.defensive_actions["Tackles"]["TklW"],
    player.defensive_actions["Tackles"]["Def 3rd"], player.defensive_actions["Tackles"]["Mid 3rd"],
    player.defensive_actions["Tackles"]["Att 3rd"],
    player.defensive_actions["Challenges"]["Tkl"], player.defensive_actions["Challenges"]["Att"],
    player.defensive_actions["Challenges"]["Tkl%"], player.defensive_actions["Challenges"]["Lost"],
    player.defensive_actions["Blocks"]["Blocks"] ,player.defensive_actions["Blocks"]["Sh"] ,
    player.defensive_actions["Blocks"]["Pass"] ,player.defensive_actions["Blocks"]["Int"] ,
    player.defensive_actions["Blocks"]["Tkl + Int"] ,player.defensive_actions["Blocks"]["Clr"] ,
    player.defensive_actions["Blocks"]["Err"],
    # Possession
    player.possession["Touches"]["Touches"], player.possession["Touches"]["Def Pen"],
    player.possession["Touches"]["Def 3rd"], player.possession["Touches"]["Mid 3rd"],
    player.possession["Touches"]["Att 3rd"], player.possession["Touches"]["Att Pen"],
    player.possession["Touches"]["Live"],
    player.possession["Take-Ons"]["Att"], player.possession["Take-Ons"]["Succ"],
    player.possession["Take-Ons"]["Succ%"], player.possession["Take-Ons"]["Tkld"],
    player.possession["Take-Ons"]["Tkld%"],
    player.possession["Carries"]["Carries"], player.possession["Carries"]["TotDist"],
    player.possession["Carries"]["ProDist"], player.possession["Carries"]["ProgC"],
    player.possession["Carries"]["1/3"], player.possession["Carries"]["CPA"],
    player.possession["Carries"]["Mis"], player.possession["Carries"]["Dis"],
    player.possession["Receiving"]["Rec"],player.possession["Receiving"]["PrgR"],
    # Playing Time
    player.playing_time_detail["Starts"]["Starts"],
    player.playing_time_detail["Starts"]["Mn/Start"],
    player.playing_time_detail["Starts"]["Compl"],

    player.playing_time_detail["Subs"]["Subs"],
    player.playing_time_detail["Subs"]["Mn/Sub"] ,
    player.playing_time_detail["Subs"]["unSub"] ,

    player.playing_time_detail["Team Success"]["PPM"] ,
    player.playing_time_detail["Team Success"]["onG"] ,
    player.playing_time_detail["Team Success"]["onGA"] ,

    player.playing_time_detail["Team Success xG"]["onxG"] ,
    player.playing_time_detail["Team Success xG"]["onxGA"] ,
    # Miscellaneous Stats
    player.Miscellaneous_Stats["Performance"]["Fls"], player.Miscellaneous_Stats["Performance"]["Fld"],
    player.Miscellaneous_Stats["Performance"]["Off"], player.Miscellaneous_Stats["Performance"]["Crs"],
    player.Miscellaneous_Stats["Performance"]["OG"], player.Miscellaneous_Stats["Performance"]["Recov"],
    player.Miscellaneous_Stats["Aerial Duels"]["Won"], player.Miscellaneous_Stats["Aerial Duels"]["Lost"],
    player.Miscellaneous_Stats["Aerial Duels"]["Won%"]
]
