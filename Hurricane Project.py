# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

##############################################################################
     #   Unhash last line to run each   #
#############################################################################

# write your update damages function here:
def updatedamages(damages):
    d=[]
    for i in damages:
        if i=="Damages not recorded":
            d.append(i)
        else:
            str_num=""
            factor=1
            for j in range(len(i)):
                if i[j]=="M":
                    factor=10**6
                elif i[j]=="B":
                    factor=10**9
                else:
                    str_num+=i[j]
            num=float(str_num)*factor
            d.append(num)
    return d
Udamages=updatedamages(damages)
#print(Udamages)

# write your construct hurricane dictionary function here:
def dict(names,months,years,max_sustained_winds,areas_affected,damages,deaths):
    dictH={}
    for i in range(len(names)):
        data={"Name":names[i], "Month":months[i], "Year":years[i], "Max Sustained Wind":max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": Udamages[i], "Deaths":deaths[i]}
        dictH[names[i]]=data
    return dictH
dictH=dict(names,months,years,max_sustained_winds,areas_affected,damages,deaths)
#print(dictH)

# write your construct hurricane by year dictionary function here:
def By_Year(dictH):
    yearH={}
    year=1924
    while year<=2021:
     Hs=[]
     for i in dictH.values():
         if i["Year"]==year:
             Hs.append(i)
     if Hs!=[]:
        yearH[year]=Hs
     year+=1
    return yearH
#print(By_Year(dictH))

# write your count affected areas function here:
def frequency(areas_affected):
    areas=[]
    freq={}
    for H in areas_affected:
        for a in H:
            if a not in areas:
                areas.append(a)
                freq[a]=1
            else:
                freq[a]+=1
    return freq
#print(frequency(areas_affected))

# write your find most affected area function here:
def MostHit(areas_affected):
    areas=[]
    freq={}
    for H in areas_affected:
        for a in H:
            if a not in areas:
                areas.append(a)
                freq[a]=1
            else:
                freq[a]+=1
    most=1
    most_area="No way no how"
    for n in range(len(areas)):
        attempt=freq[areas[n]]
        if attempt>most:
            most=attempt
            most_area=areas[n]
    print(most_area+" was hit ",most,"times!")  
#MostHit(areas_affected)

# write your greatest number of deaths function here:
def MostDeath(dictH):
    most=1
    mostH="No way no how"
    for i in dictH.values():
        attempt=i["Deaths"]
        if attempt>most:
            most=attempt
            mostH=i["Name"]
    print(mostH+" was the deadliest, with ",most," deaths...")
#MostDeath(dictH)

# write your catgeorize by mortality function here:
def mortality_scale(dictH):
    mortH={}
    m0=[]
    m1=[]
    m2=[]
    m3=[]
    m4=[]
    m5=[]
    for H in dictH.values():
        if H["Deaths"]>10000:
            m5.append(H)
        elif H["Deaths"]>1000:
            m4.append(H)
        elif H["Deaths"]>500:
            m3.append(H)
        elif H["Deaths"]>100:
            m2.append(H)
        elif H["Deaths"]>0:
            m1.append(H)
        else:
            m0.append(H)
    mortH[0]=m0
    mortH[1]=m1
    mortH[2]=m2
    mortH[3]=m3
    mortH[4]=m4
    mortH[5]=m5
    return mortH
#print(mortality_scale(dictH))

# write your greatest damage function here:
def great_damage(dictH):
    greatest=0
    Hgreat="A lovely bit of squirrel"
    for H in dictH.values():
        attempt=H["Damage"]
        if attempt=="Damages not recorded":
            continue
        elif attempt>greatest:
            greatest=int(attempt)
            Hgreat=H["Name"]
    print(Hgreat,"caused the most damages, costing ",greatest)
#great_damage(dictH)

# write your catgeorize by damage function here:
def damage_cat(dictH):
    damH={}
    d0=[]
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    d5=[]
    for H in dictH.values():
        if H["Damage"]=="Damages not recorded":
                    d0.append(H)
        elif H["Damage"]>5*10**10:
            d5.append(H)
        elif H["Damage"]>10**10:
            d4.append(H)
        elif H["Damage"]>10*9:
            d3.append(H)
        elif H["Damage"]>10**8:
            d2.append(H)
        elif H["Damage"]>0:
            d1.append(H)
    damH[0]=d0
    damH[1]=d1
    damH[2]=d2
    damH[3]=d3
    damH[4]=d4
    damH[5]=d5
    return damH
#print(damage_cat(dictH))