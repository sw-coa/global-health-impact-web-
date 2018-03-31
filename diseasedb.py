import sqlite3
import pandas as pd

conn = sqlite3.connect('ghi.db')
conn.execute('''DROP TABLE IF EXISTS disease2010''')
conn.execute('''DROP TABLE IF EXISTS disease2013''')
conn.execute('''DROP TABLE IF EXISTS disbars''')
conn.execute('''DROP TABLE IF EXISTS distypes''')


conn.execute('''CREATE TABLE disease2013
             (disease text, distype text, impact real, daly real, need text, color text)''')

conn.execute('''CREATE TABLE disease2010
             (disease text, distype text, impact real, daly real, need text, color text)''')

conn.execute('''CREATE TABLE disbars
            (disease text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real, need2010 real, need2013 real)''')

conn.execute('''CREATE TABLE distypes
            (disease text,distype text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real,position real)''')


datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv'
df = pd.read_csv(datasrc, skiprows=1)
datasrc2 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQI7j2NartMCCF_N-OCkFqAyD67N9Q32yybE21x-zaRPrETsszdZep91dVVVSCjeXXbPjPfZVdE-odE/pub?gid=1560508440&single=true&output=csv'
df2 = pd.read_csv(datasrc2, skiprows=1)

disease2010db = []
disease2013db = []

i = 0
for k in range(8,20):
    distypes = ['TB','TB','TB','Malaria','Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    colors = ['#FFB31C','#FFB31C','#FFB31C','#0083CA','#0083CA','#EF3E2E','#003452','#86AAB9','#CAEEFD','#546675','#8A5575','#305516']
    dis = ['Drug Susceptable TB','MDR-TB','XDR-TB','p. falc Malaria','p. vivax Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    color = colors[i]
    disease = dis[i]
    distype = distypes[i]
    temp = df.iloc[k,43]
    temp1 = df.iloc[k,45]
    temp2 = df.iloc[k,46]
    if type(temp) != float and type(temp1)!=float and type(temp2)!=float:
        impact = float(temp.replace(',',''))
        daly = float(temp1.replace(',',''))
        need = float(temp2.replace(',',''))
        i += 1
        row = [disease,distype,impact,daly,need,color]
        disease2010db.append(row)
        conn.execute('insert into disease2010 values (?,?,?,?,?,?)', row)

i = 0
for k in range(8,20):
    distypes = ['TB','TB','TB','Malaria','Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    colors = ['#FFB31C','#FFB31C','#FFB31C','#0083CA','#0083CA','#EF3E2E','#003452','#86AAB9','#CAEEFD','#546675','#8A5575','#305516']
    dis = ['Drug Susceptable TB','MDR-TB','XDR-TB','p. falc Malaria','p. vivax Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    color = colors[i]
    disease = dis[i]
    distype = distypes[i]
    temp = df.iloc[k,94]
    temp1 = df.iloc[k,96]
    temp2 = df.iloc[k,97]
    print('hi yoo')
    print(distype)
    print(disease)
    if type(temp) != float and type(temp1)!=float and type(temp2)!=float:
        impact = float(temp.replace(',',''))
        daly = float(temp1.replace(',',''))
        need = float(temp2.replace(',',''))
        i += 1
        row = [disease,distype,impact,daly,need,color]
        disease2013db.append(row)
        conn.execute('insert into disease2013 values (?,?,?,?,?,?)', row)

def stripdata(x,y):
    tmp = df.iloc[x,y]
    if tmp=="#DIV/0!" or tmp=="nan":
        return(0)
    if isinstance(tmp,float) == False:
        return(float(tmp.replace(',','').replace(' ','0').replace('%','')))
    else:
        return(0)

def stripdata2(x,y):
    tmp = df2.iloc[x,y]
    if tmp=="#DIV/0!" or tmp=="nan":
        return(0)
    if isinstance(tmp,float) == False:
        res = float(tmp.replace(',','').replace(' ','0').replace('%',''))
        if res > 10000:
            res = res * 0.00001
        #print(res)
        return (0.01*res)
    else:
        return(0)

disbars = []
j=0

for k in range(91, 100):
    colors = ['#FFB31C', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    diseasename = df.iloc[k,7]
    print(diseasename)
    color = colors[j]
    efficacy2010 = stripdata(k,8)
    efficacy2013 = stripdata(k,9)
    coverage2010 = stripdata(k,10)
    coverage2011 = stripdata(k,11)
    need2010 = stripdata(k,12)
    need2013 = stripdata(k,13)
    roww = [diseasename,color,efficacy2010,efficacy2013,coverage2010,coverage2011,need2010,need2013]
    #print(roww)
    disbars.append(roww)
    j+=1
    conn.execute('insert into disbars values (?,?,?,?,?,?,?,?)', roww)

#=====================================Jing-3/3/2-18============================================
i=1
j=0
mark=0
efficacy2010 = 0
efficacy2013 = 0
coverage2010 = 0
coverage2011 = 0
for k in [94,96,98,99,100,102]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    dismap =[2,3,1]
    position = [2,0,1]
    disease = ['Normal-TB','MDR-TB','XDR-TB']
    disetype='TB'
    m = dismap[mark]
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata2(k,1)
    efficacy2013 += stripdata2(k,2)
    coverage2010 += stripdata2(k,3)
    coverage2011 += stripdata2(k,5)
    print('==========efficacy2010=====')
    print(k)
    print(df2.iloc[k,0])
    print(df2.iloc[k,1])
    print(df2.iloc[k,2])
    print(df2.iloc[k,3])
    print(df2.iloc[k,5])
    print(coverage2011)
    print(efficacy2010)


    if i==m :
        efficacy2010 /= m
        efficacy2013 /= m
        coverage2010 /= m
        coverage2011 /= m
        i=0
        mark+=1
        roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2011,p]
        distypes.append(roww)
        print(roww)
        conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
        efficacy2010 = 0
        efficacy2013 = 0
        coverage2010 = 0
        coverage2011 = 0

    j+=1
    i+=1
cur = conn.execute(' select * from distypes where distype=? ',('TB',))
data = cur.fetchall()

#print(data)


i=1
j=0
mark=0
efficacy2010 = 0
efficacy2013 = 0
coverage2010 = 0
coverage2011 = 0
for k in [94,96,98,99,100,102]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    dismap =[2,3,1]
    position = [2,0,1]
    disease = ['p. falc Malaria', 'p. vivax Malaria', 'Malaria']
    disetype='Malaria'
    m = dismap[mark]
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata2(k,1)
    efficacy2013 += stripdata2(k,2)
    coverage2010 += stripdata2(k,3)
    coverage2011 += stripdata2(k,5)
    print('==========This is Malaria=====')
    #print(k)
    #print(df2.iloc[k,0])
    #print(df2.iloc[k,1])
    #print(df2.iloc[k,2])
    #print(df2.iloc[k,3])
    #print(df2.iloc[k,5])
    #print(coverage2010)
    #print(efficacy2010)

    if i==m :
        efficacy2010 /= m
        efficacy2013 /= m
        coverage2010 /= m
        coverage2011 /= m
        i=0
        mark+=1
        roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2011,p]
        distypes.append(roww)
        print(roww)
        conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
        efficacy2010 = 0
        efficacy2013 = 0
        coverage2010 = 0
        coverage2011 = 0

    j+=1
    i+=1
cur = conn.execute(' select * from distypes where distype=? ',('Malaria',))
data = cur.fetchall()
print(data)

conn.commit()
