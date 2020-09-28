import display
import os
import datetime
from bs4 import BeautifulSoup
import datetime
from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

def main():
    display.move_cursor(0,0)
    gui_news()


def gui_news():
    # GET NEWS

    news_vitry = getNews("ile-de-france",  "val-de-marne", "vitry-sur-seine")
    news_vdm = getNews("ile-de-france",  "val-de-marne")
    news_idf = getNews("ile-de-france")


    os.system('clear')

    print("="*53 + "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "="*53)
    display.print_n(0, 1, "-"*54 + " NEWS VITRY ".center(20,"-") + "-"*54)
    printNews(news_vitry, 2, 16, 128)
    display.print_n(0, 16, "-"*54 + " NEWS 94 ".center(20,"-") + "-"*54)
    printNews(news_vdm, 17, 31, 128)
    display.print_n(0, 31, "-"*54 + " NEWS IDF ".center(20,"-") + "-"*54)
    printNews(news_idf, 32, 46, 128)



def getNews(region, departement = "", city = "", page=1):
    if page > 1:
        request = "https://faitsdivers365.fr/" + region + "/" + departement +\
        "/" + city + "/page/" + str(page) + "/"
    else:
        request = "https://faitsdivers365.fr/" + region + "/" + departement + "/" + city + "/"


    html_doc = requests.get(request)
    soup = BeautifulSoup(html_doc.text, "html.parser")

    posts = soup.find_all('a', {'class': 'mh-thumb-icon'})
    dates = soup.find_all('span', {'class': 'mh-meta-date updated'})

    return {"posts":posts, "dates":dates};


def printNews(news, n, n_max, width):
    posts, dates = news["posts"], news["dates"]
    nn = n
    for i in range(0, 19):
        nn = display.breakline_n(0, nn, width - 1, n_max, '[ ' + dates[i].text.ljust(5) + ' ] '+  posts[i]['title'])

def printTC():
    # GET TRANSPORT
    try:
        #r_C_ALL = requests.get('https://api.transilien.com/gare/87545293/depart', auth=HTTPBasicAuth('tnhtn1120', 'C35XsX9ya'))
        r_C_BNF = requests.get('https://api.transilien.com/gare/87545293/depart/87328328', auth=HTTPBasicAuth('tnhtn1120', 'C35XsX9ya'))
        r_C_CHS = requests.get('https://api.transilien.com/gare/87545293/depart/87545285', auth=HTTPBasicAuth('tnhtn1120', 'C35XsX9ya'))
        H_C_BNF = ET.fromstring(r_C_BNF.content)
        H_C_CHS = ET.fromstring(r_C_CHS.content)
    except Exception:
        return



    display.print_n(0, 46, "="*43 + "< RER C >-" + "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "-< RER C >" + "="*43)
    i = 0
    for E_C_BNF, E_C_CHS in zip(H_C_BNF.findall('train'), H_C_CHS.findall('train')):

        if i < 2:
            print("<<<" +str(i) +">>>")
            display.print_n(0, 47 + i, (E_C_BNF.find('date').text + ' ' + E_C_BNF.find('miss').text).center(24))
            display.print_n(25, 47 + i, '|' + (E_C_CHS.find('date').text + ' ' + (E_C_CHS.find('miss').text)).center(23))
        i+=1



def idf():
        region="ile-de-france"
        city=""

        departements="paris", "hauts-de-seine", "val-de-marne", \
                     "seine-saint-denis", "essone", "seine-et-marne", \
                     "yvelines","val-doise"

        district_92="boulogne-billancourt", "nanterre","colombes", \
                    "asnieres-sur-seine", "rueil-malmaison", "courbevoie"

        district_93="saint-denis","aulnay-sous-bois","aubervilliers","drancy",\
                    "bobigny", "le-raincy"

        district_94="creteil", "vitry-sur-seine", "champigny-sur-marne", \
                    "maisons-alfort", "ivry-sur-seine", "lhay-les-roses", \
                    "nogent-sur-marne"

        district_77="meaux","chelles","melun", "pontault-combault",\
                    "fontainebleau", "provins"

        district_78="versailles","sartrouville","mantes-la-jolie", \
                    "saint-germain-en-laye", "poissy", "rambouillet"

        district_91="evry","corbeil-essonnes","massy","savigny-sur-orge", \
                    "palaiseau","etampes"

        district_95="argenteuil","sarcelles","cergy","garges-les-gonesse", \
                    "franconville","pontoise"

        idf = {("paris", 75): "", ("hauts-de-seine",92): district_92,\
              ("seine-saint-denis",93): district_93,\
              ("val-de-marne", 94): district_94,\
              ("seine-et-marne",77):district_77, ("yvelines", 78):district_78,\
              ("essonne",91):district_91, ("val-doise",95):district_95}

        for departement, districts in idf.items():
            print('*', departement[0], departement[1])
            for district in districts:
                print('     -->', district)
                res = getNews("ile-de-france", departement[0], district)
                for i in range(0, 1):
                    print('[ ' + res["dates"][i].text.ljust(5) + ' ] '+  res["posts"][i]['title'])
