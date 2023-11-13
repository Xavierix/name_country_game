import turtle as tt
import pandas
import settings

screen = tt.Screen()
screen.setup(settings.W_WIDTH, settings.W_HEIGHT)

screen.title("Countries of a Region!")

#  # Uncomment the map you want to test.  You can add more just add the name of the gif in the list
#  # The map much have a matching csv and other should be added to the dictionary in settings.
#  # Pick a region!
# test_0 = 'africa'
# test_0 = 'east_asia'
# test_0 = "europe"
# test_0 = 'middle_east'
# test_0 = 'south_america'


#  #  Pulling the image and the CSV file from the dictionary
img = settings.country_dictionary[test_0][0]
csv_file = settings.country_dictionary[test_0][1]

#  #  Creating the image
screen.addshape(img)
tt.shape(img)

#  #  Creating the Dataframe
regions_data_frame = pandas.read_csv(csv_file)

#  #  Creating the list to capture all the countries
list_of_countries = regions_data_frame.name.to_list()

#  #  Using this to test all the countries draw to the map correctly.
for name_x in list_of_countries:

    country_selected = regions_data_frame[regions_data_frame.name == name_x]

    position = int(country_selected.x.iloc[0]), int(country_selected.y.iloc[0])

    select_country = tt.Turtle()
    select_country.hideturtle()
    select_country.penup()
    select_country.goto(position)
    select_country.write(arg=name_x, move=False, align="center", font=settings.FONT)

print("All done!")

#  # user the below to capture click without the screen from closing.
def get_moust_click_coor(x, y):
    print(f"{x},{y}")


tt.onscreenclick(get_moust_click_coor)
tt.mainloop()

screen.exitonclick()
