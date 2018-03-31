import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('ghi.db')


conn.execute('''DROP TABLE IF EXISTS manudis''')
conn.execute('''DROP TABLE IF EXISTS manutot''')
conn.execute('''DROP TABLE IF EXISTS patent2010''')
conn.execute('''DROP TABLE IF EXISTS patent2013''')


conn.execute('''CREATE TABLE manudis
             (company text, disease text, daly2010 real, daly2013 real, color text)''')

conn.execute('''CREATE TABLE manutot
             (company text, daly2010 real, daly2013 real, color text)''')

conn.execute('''CREATE TABLE patent2010
            (company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real, color text)''')
conn.execute('''CREATE TABLE patent2013
            (company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real, color text)''')

datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv'
datasrc20102015 = 'https://docs.google.com/spreadsheets/d/1vwMReqs8G2jK-Cx2_MWKn85MlNjnQK-UR3Q8vZ_pPNk/pub?gid=1560508440&single=true&output=csv'

df = pd.read_csv(datasrc, skiprows=1)
df_new = df.notnull()
print(df_new)
print(df)
i = 0;
colorlist = []
colors = ['FFB31C','0083CA','EF3E2E','003452','86AAB9','CAEEFD','546675','8A5575','305516','B78988','BAE2DA','B1345D','5B75A7','906F76','C0E188','DE9C2A','F15A22','8F918B','F2C2B7','F7C406','B83F98','548A9B','D86375','F1DBC6','0083CA','7A80A3','CA8566','A3516E','1DF533','510B95','DFF352','F2C883','E3744D','26B2BE','5006BA','B99BCF','DC2A5A','D3D472','2A9DC4','C25C90','65A007','FE3289','C6DAB5','DDF6AC','B7E038','1ADBBD','3BC6D5','0ACD57','22419F','D47C5B']
for x in colors:
    y = '#'+x
    colorlist.append(y)
print(colorlist)
manudata = []
manutotal = []


for k in range(25,88):
    company = df.iloc[k,2]
    print(company)
    if isinstance(company,float):
        if math.isnan(company):
            break
    disease = 'TB'

    _k3 = df.iloc[k, 3]
    if df_new.iloc[k, 3] == False:
        temp1 = 0
    elif '-' in _k3:
         temp1 = _k3.replace('-','0')
    elif ',' in _k3:
         temp1 = _k3.replace(',','')
    else:
        temp1 = _k3

    tbdaly2010 = float(temp1)

    _k4 = df.iloc[k, 4]
    if df_new.iloc[k, 4] ==  False:
        temp2 = 0
    elif '-' in _k4:
        temp2 = _k4.replace('-', '0')
    elif ',' in _k4:
        temp2 = _k4.replace(',', '')
    else:
        temp2 = _k4

    tbdaly2013 = float(temp2)

    if tbdaly2010 > 0 or tbdaly2013 > 0:
        color = colors[i]
        row=[company,disease,tbdaly2010,tbdaly2013,color]
        manudata.append(row)
        i += 1
        conn.execute('insert into manudis values (?,?,?,?,?)', row)
i=0
for k in range(25,88):
    company = df.iloc[k,6]
    if isinstance(company,float):
        if math.isnan(company):
            break
    disease = 'HIV'
    hivdaly2010 = float(df.iloc[k,10].replace('-','0').replace(',',''))
    hivdaly2013 = float(df.iloc[k,11].replace('-','0').replace(',',''))
    _k10 =  df.iloc[k, 10]
    if df_new.iloc[k, 10] == False:
        temp1 = 0
    if '-' in _k10:
        temph = _k10.replace('-', '0')
    elif ',' in _k10:
        temph = _k10.replace(',', '')
    else:
        temph = _k10

        hivdaly2010 = float(temph)

    k11 = df.iloc[k, 11]
    if df_new.iloc[k, 11] == False:
        temp1 = 0
    if '-' in k11:
        temph1 = k11.replace('-', '0')
    elif ',' in k11:
        temph1 = k11.replace(',', '')
    else:
        temph1 = k11

    tbdaly2013 = float(temph1)
    if hivdaly2010 > 0 or hivdaly2013 > 0:
        color = colors[i]
        row=[company,disease,hivdaly2010,hivdaly2013,color]
        i += 1
        manudata.append(row)
        conn.execute('insert into manudis values (?,?,?,?,?)', row)
i=0
for k in range(25,88):
    company = df.iloc[k,12]
    if isinstance(company,float):
        if math.isnan(company):
            break

    k13 = df.iloc[k, 13]
    if df_new.iloc[k, 13] == False:
        temp1 = 0
    if '-' in k13:
        temphd = k13.replace('-', '0')
    elif ',' in k13:
        temphd = k13.replace(',', '')
    else:
        temphd = k13

    daly2010 = float(temphd)

    k14 = df.iloc[k, 14]
    if df_new.iloc[k, 14] == False:
        tempd1 = 0
    if '-' in k14:
        tempd1 = k14.replace('-', '0')
    elif ',' in k14:
        tempd1 = k14.replace(',', '')
    else:
        tempd1 = k14

    daly2013 = float(tempd1)

    if daly2010 > 0 or daly2013 > 0:
        color = colors[i]
        row=[company,daly2010,daly2013,color]
        i += 1
        manutotal.append(row)
        conn.execute('insert into manutot values (?,?,?,?)', row)
###############################PATENT PATENT PATENT CODE BELOW ######################################################################
###############################PATENT PATENT PATENT CODE BELOW ######################################################################
def cleanfloat(var):
    if type(var) != float:
        var = float(var.replace(',',''))
    if var != var:
        var = 0
    return var
oldrow = ['']
pat2010 = []
for i in range(1,43):
    prow = []
    comp = df.iloc[1,i]
    print(comp)
    prow.append(comp)
    for j in range(11,21):
        if j == 11:
            tb1 = cleanfloat(df.iloc[8,i])
            tb2 = cleanfloat(df.iloc[9,i])
            tb3 = cleanfloat(df.iloc[10,i])
            tb=[tb1,tb2,tb3]
            temp = (tb1+tb2+tb3)
            prow.append(temp)
        elif j == 12:
            mal1 = cleanfloat(df.iloc[11,i])
            mal2 = cleanfloat(df.iloc[12,i])
            mal=[mal1,mal2]
            temp = (mal1+mal2)
            prow.append(temp)
        elif j == 20:
            total = cleanfloat(df.iloc[j,i])
            prow.append(total)
        else:
            temp = df.iloc[j,i]
            if isinstance(temp,float) == False and isinstance(temp,int) == False:
                temp = float(temp.replace(',',''))
            if temp != temp:
                temp = 0
            prow.append(temp)
    if prow[0] == oldrow [0]:
        for ind in range(1,len(prow)):
            prow[ind] += oldrow[ind]
    oldrow = prow
    if comp != df.iloc[1,i+1]:
        pat2010.append(prow)
unmet = ['Unmet Need']
for j in range(11,21):
    if j == 11:
        print(df.iloc[7,46])
        tb1 = cleanfloat(df.iloc[8,45])
        tb2 = cleanfloat(df.iloc[9,45])
        tb3 = cleanfloat(df.iloc[10,45])
        tb=[tb1,tb2,tb3]
        temp = (tb1+tb2+tb3)
        unmet.append(temp)
    elif j == 12:
        mal1 = cleanfloat(df.iloc[11,45])
        mal2 = cleanfloat(df.iloc[12,45])
        mal=[mal1,mal2]
        temp = (mal1+mal2)
        unmet.append(temp)
    elif j == 20:
        total = cleanfloat(df.iloc[j,45])
        unmet.append(total)
    else:
        temp = df.iloc[j,45]
        if isinstance(temp,float) == False and isinstance(temp,int) == False:
            temp = float(temp.replace(',',''))
        if temp != temp:
            temp = 0
        unmet.append(temp)
pat2010.append(unmet)
colind = 0
for item in pat2010:
    item.append(colors[colind])
    colind+=1
    conn.execute(' insert into patent2010 values (?,?,?,?,?,?,?,?,?,?,?,?) ', item)
print(pat2010)


oldrow = ['']
pat2013 = []
for i in range(50,91):
    prow = []
    comp = df.iloc[1,i]
    prow.append(comp)
    for j in range(11,21):
        if j == 11:
            tb1 = cleanfloat(df.iloc[8,i])
            tb2 = cleanfloat(df.iloc[9,i])
            tb3 = cleanfloat(df.iloc[10,i])
            tb=[tb1,tb2,tb3]
            temp = (tb1+tb2+tb3)
            prow.append(temp)
        elif j == 12:
            mal1 = cleanfloat(df.iloc[11,i])
            mal2 = cleanfloat(df.iloc[12,i])
            mal=[mal1,mal2]
            temp = (mal1+mal2)
            prow.append(temp)
        elif j == 20:
            total = cleanfloat(df.iloc[j,i])
            prow.append(total)
        else:
            temp = df.iloc[j,i]
            if isinstance(temp,float) == False and isinstance(temp,int) == False:
                temp = float(temp.replace(',',''))
            if temp != temp:
                temp = 0
            prow.append(temp)
    if prow[0] == oldrow [0]:
        for ind in range(1,len(prow)):
            prow[ind] += oldrow[ind]
    oldrow = prow
    if comp != df.iloc[1,i+1]:
        pat2013.append(prow)
unmet = ['Unmet Need']
for j in range(11,21):
    if j == 11:
        print(df.iloc[8,93])
        tb1 = cleanfloat(df.iloc[8,94])
        tb2 = cleanfloat(df.iloc[9,94])
        tb3 = cleanfloat(df.iloc[10,94])
        tb=[tb1,tb2,tb3]
        temp = (tb1+tb2+tb3)
        unmet.append(temp)
    elif j == 12:
        mal1 = cleanfloat(df.iloc[11,94])
        mal2 = cleanfloat(df.iloc[12,94])
        mal=[mal1,mal2]
        temp = (mal1+mal2)
        unmet.append(temp)
    elif j == 20:
        total = cleanfloat(df.iloc[j,94])
        unmet.append(total)
    else:
        temp = df.iloc[j,94]
        if isinstance(temp,float) == False and isinstance(temp,int) == False:
            temp = float(temp.replace(',',''))
        if temp != temp:
            temp = 0
        unmet.append(temp)
pat2013.append(unmet)
colind = 0
for item in pat2013:
    item.append(colors[colind])
    colind+=1
    conn.execute(' insert into patent2013 values (?,?,?,?,?,?,?,?,?,?,?,?) ', item)
print(pat2013)

##############   END OF PATENT CODE  ############################################################################
##############   END OF PATENT CODE  ############################################################################

conn.commit()