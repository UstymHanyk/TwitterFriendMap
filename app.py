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
    username = request.form.get("username")
    if "@" not in username:
        username = "@" + username
    friends_loc_list = friends_geolocator(get_user_friends(username))
    fl_map = generate_map(group_duplicates(friends_loc_list))
    return fl_map._repr_html_()
    # return render_template('index.html', map=map._repr_html_())
