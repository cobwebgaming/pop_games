from flask import Flask, render_template
from utils import get_wiki_page_first_paragraph

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", games=create_games_list_items())

@app.route("/gta")
def gta1():
  return render_template("game_layout.html", data=create_gta_data())
  
@app.route("/the_forest")
def the_forest():
  return render_template("game_layout.html", data=create_the_forest_data())

@app.route("/minecraft")
def minecraft():
  return render_template("game_layout.html", data=create_minecraft_data())

@app.route("/fnaf")
def fnaf():
  return render_template("game_layout.html", data=create_fnaf_data())
   
@app.route("/hello_neighbor")
def hello_neighbor():
  return render_template("game_layout.html", data=create_hello_neighbor_data())

class GameData:
    def __init__(self):
        self.tab_img = 'tab_img'
        self.title = 'a'
        self.main_img = 'img'
        self.desc = 'd'
        self.opinion = 'o'
        self.yt_url = ['', '', '']
  
def create_gta_data():
    opinion = """ This game is really fun, it has many cool mods and missions. i'll give it a 10 out of 10 rating! """
    gta = GameData()
    gta.tab_img = "static/img/gta_logo.png"
    gta.title = 'Grand Theft Auto'
    gta.main_img = 'static/img/gta0.png'
    gta.desc = get_wiki_page_first_paragraph('Grand_Theft_Auto')
    gta.opinion = opinion
    gta.yt_url[0] = 'https://www.youtube.com/embed/pWS8GkWs-dU'
    gta.yt_url[1] = 'https://www.youtube.com/embed/ZA4Kzi0z47E'
    gta.yt_url[2] = 'https://www.youtube.com/embed/kaD5NAMdkTY'
    return gta
    
def create_the_forest_data():
    opinion = """ The Forest is a really scary game... i'll give it a 8/10 rating" """
    the_forest = GameData()
    the_forest.tab_img = "static/img/the_forest_logo.png"
    the_forest.title = 'The Forest'
    the_forest.main_img = 'static/img/the_forest.png'
    the_forest.desc = get_wiki_page_first_paragraph('The_Forest_(video_game)')
    the_forest.opinion = opinion
    the_forest.yt_url[0] = 'https://www.youtube.com/embed/RBl-H5FQEog'
    the_forest.yt_url[1] = 'https://www.youtube.com/embed/j4BUgKT1LpQ'
    the_forest.yt_url[2] = 'https://www.youtube.com/embed/qeUIbD7301A'
    return the_forest
    
def create_minecraft_data():
    opinion = """ I played this game when I was a beginner YouTuber. now it started to be boring to me but it's still popular...my rating is 8/10 """
    minecraft = GameData()
    minecraft.tab_img = "static/img/minecraft_logo.png"
    minecraft.title = 'Minecraft'
    minecraft.main_img = 'static/img/minecraft.png'
    minecraft.desc = get_wiki_page_first_paragraph('Minecraft')
    minecraft.opinion = opinion
    minecraft.yt_url[0] = 'https://www.youtube.com/embed/Do_Tp8LyYP0'
    minecraft.yt_url[1] = 'https://www.youtube.com/embed/v8nqVoEHPf4'
    minecraft.yt_url[2] = 'https://www.youtube.com/embed/08Bh8_Oa-B8'
    return minecraft

def create_fnaf_data():
    opinion = """ This game is scary too but i still like it. 10/10 """
    fnaf = GameData()
    fnaf.tab_img = "static/img/fnaf_logo.png"
    fnaf.title = "Five Nights at Freddy's"
    fnaf.main_img = 'static/img/fnaf.png'
    fnaf.desc = get_wiki_page_first_paragraph("Five_Nights_at_Freddy's")
    fnaf.opinion = opinion
    fnaf.yt_url[0] = 'https://www.youtube.com/embed/-IjsRrraOQA'
    fnaf.yt_url[1] = 'https://www.youtube.com/embed/GlZtlTon7_I'
    fnaf.yt_url[2] = 'https://www.youtube.com/embed/EpudDCqYdiA'
    return fnaf
    
def create_hello_neighbor_data():
    opinion = """This game is scary but it's funny though. 10/10 """
    hello_neighbor = GameData()
    hello_neighbor.tab_img = "static/img/hello_neighbor_logo.png"
    hello_neighbor.title = "Hello Neighbor"
    hello_neighbor.main_img = 'static/img/hello_neighbor.png'
    hello_neighbor.desc = get_wiki_page_first_paragraph("Hello_Neighbor")
    hello_neighbor.opinion = opinion
    hello_neighbor.yt_url[0] = 'https://www.youtube.com/embed/QSVKcKZS3Fo'
    hello_neighbor.yt_url[1] = 'https://www.youtube.com/embed/H8z2B3w2JU4'
    hello_neighbor.yt_url[2] = 'https://www.youtube.com/embed/iTe0fstiYWI'
    return hello_neighbor

class GamesListItem:
    def __init__(self, img_src, game_url, desc):
        self.img_src = img_src
        self.game_url = game_url
        self.desc = desc


def create_games_list_items():

    gta_desc = '''
Grand Theft Auto is an action-adventure video game
    '''
    the_forest_desc = '''
The forest is a Hrror game
    '''

    fnaf_desc = '''
Five Nights At Freddy's is a scary game
    '''

    hello_neighbor_desc = '''
Survival Horror scary game!
    '''

    minecraft_desc = '''
Minecraft is a sandbox video game
    '''

    return [GamesListItem("static/img/gta0.png", "/gta", gta_desc),
             GamesListItem("static/img/the_forest.png", "/the_forest", the_forest_desc), 
             GamesListItem("static/img/fnaf.png", "/fnaf", fnaf_desc), 
             GamesListItem("static/img/hello_neighbor.png","/hello_neighbor", hello_neighbor_desc),
             GamesListItem("static/img/minecraft.png", "/minecraft", minecraft_desc)]

if __name__ == "__main__":
    app.run(debug=True)
  
    
