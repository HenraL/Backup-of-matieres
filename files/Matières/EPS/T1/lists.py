import datetime, os
date=datetime.datetime.now()
Date="{}/{}/{}".format(date.day,date.month,date.year)
DateFile="{} {} {}".format(date.day,date.month,date.year)
try:
    fileList=os.listdir("data")
except:
    os.mkdir("data")
    fileList=os.listdir("data")
chosenFile=""
path="data/{}".format(chosenFile)
Level_5_not_acquired={
    "mark":["0,7","1,4","2,1","2,8","3,5","4,2","4,9","5,6","6,3"],
    "TG":["9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39"],
    "TB":["7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29"]}
Level_5_acquired={
    "list1":{
        "mark":["7","7,7","8,4","9,1","9,8","10,5"],
        "TG":["6'26","6'20","6'13","6'07","6'01","5'55"],
        "TB":["5'19","5'11","5'03","4'55","4'51","4'47"]},
    "list2":{
        "mark":["11,2","11,9","12,6","13,3","14"],
        "TG":["5'49","5'43","5'37","5'31","5,25"],
        "TB":["4'43","4'40","4'37","4'34","4'31"]}}
mark=["0,7","1,4","2,1","2,8","3,5","4,2","4,9","5,6","6,3","7","7,7","8,4","9,1","9,8","10,5","11,2","11,9","12,6","13,3","14"]
TG=["9'03","8'41","8'20","8'00","7'41","7'24","7'08","6'53","6'39","6'26","6'20","6'13","6'07","6'01","5'55","5'49","5'43","5'37","5'31","5,25"]
TB=["7'28","7'09","6'51","6'34","6'19","6'05","5'52","5'40","5'29","5'19","5'11","5'03","4'55","4'51","4'47","4'43","4'40","4'37","4'34","4'31"]
Project_Gap_main_corresponds=["0","2","4"]
Project_Gap_main=["+ de 15 secondes","15-10 secondes","<10 secondes"]
Recovery_main=[
            "Trop passive, pas de liaison directe avec l'effort consenti",
            "Récupération active immédiatement après l'effort (course lente, étirements)",
            "Toutes les dimensions de la récupération sont présentes, chronologiquement positionnées. On conjure l'effort fait et l'effort à faire."
            ]
Recovery_main_corresponds=["0","1","2"]

chosen={"Last name":"","First name":"","mark":"","gender":"","gap":"","Recovery main":""}
c_choice=['Last name','First name','mark','gender','gap','Recovery main','T1_T1','T1_T2','T1_T3','T1_E1','T1_R1','T2_T1','T2_T2','T2_T3','T2_E2','T2_R2','TB']#,'T1_E4','T1_R5','T2_E4','T2_R5'
forbidden_choices=["","---------Choisissez un élément---------"]