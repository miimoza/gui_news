import display
import os
import datetime
from bs4 import BeautifulSoup
from datetime import datetime

def main():
	display.move_cursor(0,0)
	gui_news()
	for i in range(0, 28):
		display.move_cursor(i, 48)
		print("|")


def gui_news():
    # GET NEWS



    os.system('clear')

    print("="*13 + "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "="*13)
    print("-"*14 + " NEWS VITRY ".center(20,"-") + "-"*5 + "-(94)-")

    getToday("ile-de-france")

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


def getToday(region, departement = "", city = ""):
    res = getNews(region, departement, city)
    posts, dates = res["posts"], res["dates"]

    d0 = datetime.strptime(dates[0].text, '%H:%M')
    print(d0)
    print("="*20 + "[ NEWS:" + (region + ", " + departement + ", " + city).center(50) +"]" + "="*20)

    page = 1;
    i = 0;
    while (datetime.strptime(dates[i].text, '%H:%M') <= d0):
        print('[ ' + dates[i].text.ljust(5) + ' ] '+  posts[i]['title'])
        i+=1
        if (i >= len(posts)):
            page += 1
            res = getNews(region, departement, city, page)
            posts, dates = res["posts"], res["dates"]
            i = 0

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
