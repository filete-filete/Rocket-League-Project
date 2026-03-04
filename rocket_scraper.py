import requests, bs4
import datetime

def get_html(platform,username):
    # get the HTML for filete filete from rlstats.net
    response = requests.get("https://rlstats.net/profile/"+platform+"/"+username)
    # playFile = open(r"C:\Users\felix\rocket_league_project\rlstats.html","w", encoding="utf-8")
    # playFile.write(response.text)
    # playFile.close()
    return response.text

def get_stats(platform, username):
    
    # open file:
    file = open(r"C:\Users\felix\rocket_league_project\rlstats.txt","a", encoding="utf-8")
    # print username, platform, date and time
    file.write(username+", "+platform+", ")
    now = datetime.datetime.now()
    file.write(str(now.date())+", "+str(now.time())+", ")
    
    rlstats_html = get_html(platform,username)
    rlstats_soup = bs4.BeautifulSoup(rlstats_html, "html.parser")
    
    # find selector for the general total stats
    totals_selector = "#stats > div > div > div.block-body > div > table"
    totals_element = rlstats_soup.select(totals_selector)
    # total stats
    for i in range(6):
        file.write('"'+totals_element[0].find_all("td")[i].contents[0]+'"'+", ") #total goals, saves, etc
    # find selector for casual
    casual_selector = "#skills > div.center > div > div.block-body > div.block-skills > div.unranked-block.center > table"
    casual_element = rlstats_soup.select(casual_selector)
    #stats for casual
    file.write(casual_element[0].find_all("td")[1].contents[0]+", ")
    # find selector for rank, division, mmr and matches this season
    ranked_selector = "#skills > div.center > div > div.block-body > div.block-skills > table:nth-child(1)"
    ranked_element = rlstats_soup.select(ranked_selector)
    # stats for 1v1 ranked
    file.write(ranked_element[0].find_all("td")[0].contents[0]+", ")   #rank
    file.write(ranked_element[0].find_all("td")[3].contents[0]+", ")   #division
    file.write(ranked_element[0].find_all("td")[6].contents[1]+", ")   #mmr
    file.write(ranked_element[0].find_all("td")[9].contents[0]+", ")   #total matches this season
    # stats for 2v2 ranked
    file.write(ranked_element[0].find_all("td")[1].contents[0]+", ")   #rank
    file.write(ranked_element[0].find_all("td")[4].contents[0]+", ")   #division
    file.write(ranked_element[0].find_all("td")[7].contents[1]+", ")   #mmr
    file.write(ranked_element[0].find_all("td")[10].contents[0]+", ")  #total matches this season
    # stats for 3v3 ranked
    file.write(ranked_element[0].find_all("td")[2].contents[0]+", ")   #rank
    file.write(ranked_element[0].find_all("td")[5].contents[0]+", ")   #division
    file.write(ranked_element[0].find_all("td")[8].contents[1]+", ")   #mmr
    file.write(ranked_element[0].find_all("td")[11].contents[0]+", ")  #total matches this season
    # all finished, end with a new line char
    file.write("\n")
    file.close()




