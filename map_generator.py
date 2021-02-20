import folium
from friend_searcher import friends_geolocator, get_user_friends
import random
from folium.plugins import MarkerCluster

# friends_loc_list = friends_geolocator(get_user_friends("@daviddobrik"))
# print(friends_loc_list)

def group_duplicates(friends_loc_list):
    loc_dict = {}
    for friend in friends_loc_list:
        loc_dict[friend[1]] = loc_dict.get(friend[1], []) + [friend[0]]
    # print(loc_dict,list(loc_dict))
    grouped_loc_list = []
    for location,names in loc_dict.items():
        for name in names:
            grouped_loc_list.append((name,location))
    return grouped_loc_list

def generate_map(friends_loc_list):
    fl_map = folium.Map(location=friends_loc_list[0][1],
                        zoom_start=7,
                        tiles="cartodbdark_matter")

    fg = folium.FeatureGroup(name="Twitter Friends map")
    fill_colors = ["#4CC9F0","#4895EF", "#4361EE","#3F37C9","#3A0CA3","#480CA8","#560BAD","#F72585","#7209B7","#B5179E"]

    marker_cluster = MarkerCluster().add_to(fl_map)

    # fill_colors = ["#3B0209","#4E030C", "#6A040F","#9D0208","#D00000","#DC2F02","#E85D04","#F48C06","#FAA307","#FAA307"]

    for friend in friends_loc_list[1:]:
        # icon = folium.features.CustomIcon("images/map_pin.png", icon_size=(30, 30))

        popup_template = f"{friend[0]}"

        popup = folium.Popup(max_width=200, html =popup_template )

        folium.CircleMarker(location=[friend[1][0], friend[1][1]],
                                        radius=10,
                                        popup=popup_template,
                                        fill_color=random.choice(fill_colors),
                                        color="#FFFFFF",
                                        fill_opacity=0.7).add_to(marker_cluster)

    fg.add_child(folium.Marker(location=friends_loc_list[0][1]))
    fl_map.add_child(fg)
    # fl_map.save('templates/raw_map.html')
    return fl_map
