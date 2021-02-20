from flask import Flask, render_template, request
from friend_searcher import friends_geolocator, get_user_friends
from map_generator import generate_map, group_duplicates
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map_generation", methods=["POST"])
def wait_for_map_generation():
    # if not request.form.get("domain"):
    #     return render_template("failure.html")
    username = "@" + request.form.get("username")
    print(username)
    friends_loc_list = friends_geolocator(get_user_friends(username))
    print(friends_loc_list)
    generate_map(group_duplicates(friends_loc_list))
    return render_template("map.html")
