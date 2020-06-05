import display
import os
import datetime
from bs4 import BeautifulSoup
import datetime
import requests

def main():
	display.move_cursor(0,0)
	gui_news()


def gui_news():
    # GET NEWS
    news_vitry = getNews("ile-de-france",  "val-de-marne", "vitry-sur-seine")
    news_vdm = getNews("ile-de-france",  "val-de-marne")
    news_idf = getNews("ile-de-france")

    os.system('clear')

    print("="*29 + "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "="*29)
    print("-"*30 + " NEWS VITRY ".center(20,"-") + "-"*24 + "-(94)-")



    printNews(news_vitry, 2, 6, 80)
    printNews(news_vdm, 8, 13, 80)
    printNews(news_idf, 15, 20, 80)



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
        nn = display.breakline_n(0, nn, width, n_max + 1, '[ ' + dates[i].text.ljust(5) + ' ] '+  posts[i]['title'])


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
