W_WIDTH, W_HEIGHT = 900, 800  # Map display settings

FONT = ('Arial', 8, 'normal')  # font for the country and message type

#  # If you want to add more just make sure the region is listed as the dictionary name and the map and csv
#  # are in the correct folders.
country_dictionary = {
    "africa": ["./maps/africa.gif", "./map_csv/africa.csv"],
    "east_asia": ["./maps/east_asia.gif", "./map_csv/east_asia.csv"],
    "europe": ["./maps/europe.gif", "./map_csv/europe.csv"],
    "middle_east": ["./maps/middle_east.gif", "./map_csv/middle_east.csv"],
    "south_america": ["./maps/south_america.gif", "./map_csv/south_america.csv"],
}

success_message = "You got them all right! Congrats!"
sm_position = (0, W_HEIGHT - 100)
#  # I am aware the print may not work correctly for the game.
