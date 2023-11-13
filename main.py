import pandas, settings, message as ms, turtle as tt


screen = tt.Screen()
screen.setup(settings.W_WIDTH, settings.W_HEIGHT)
screen.title("Countries of a Region!")


def print_out_file(list1, list2, reg):
    """Enter the contain list of all countries as list1.
    Then enter the correctly answered list of countries
    to compare what was missed.  Enter the region as reg
    to capture the region name in the document."""
    missed_countries = []
    for country in list1:
        if country not in list2:
            missed_countries.append(country)

    missed_countries_print = pandas.DataFrame(missed_countries)

    # will save the doc in its own folder
    missed_countries_print.to_csv(f"./review_items/{reg}_countries_to_review.csv")


game_on = True
stay_in_region = True

#  # The first loop, so you can pick a region, if you exit the country list
#  # you can choose another location.
while game_on:
    stay_in_region = True
    #  # Pick a region!
    chosen_region = screen.textinput(title="Pick a region.",
                                     prompt="Enter a number.\n"
                                            "1. Africa\n"
                                            "2. East Asia\n"
                                            "3. Europe\n"
                                            "4. Middle East\n"
                                            "5. South America")
    match chosen_region:
        case "1":
            region = 'africa'
        case "2":
            region = 'east_asia'
        case "3":
            region = "europe"
        case "4":
            region = 'middle_east'
        case "5":
            region = 'south_america'
        case "Exit":
            game_on = False
            break
        case _:
            print("Please one of the numbers listed!")
            break

    #  # selecting region image and csv file
    img = settings.country_dictionary[region][0]
    csv_file = settings.country_dictionary[region][1]
    screen.addshape(img)
    tt.shape(img)

    #  # initializing a container for the correct guesses
    countries_correct = []

    #  # converting csv file to data frame the creating a list from the series
    regions_data_frame = pandas.read_csv(csv_file)
    countries_list = regions_data_frame.name.to_list()

    #  # loop through the country guesses
    while stay_in_region:
        # creating variables to capture the count of countries guessed
        # correctly vs the total list
        cc, cl = len(countries_correct), len(countries_list)
        if cc / cl == 1:
            # If the user guessed all countries the game ends
            success = ms.Message()
            success.write(settings.success_message, settings.sm_position)
            game_on = False
            stay_in_region = False
        else:
            print(cc, cl, countries_correct, countries_list)
            chosen_country = screen.textinput(title=f"{cc}/{cl} Countries Correct.",
                                              prompt="Enter country name:").title()
            if chosen_country == "Exit":
                print_out = screen.textinput(title=f"Sorry to see you leave.",
                                             prompt="Would you like a printout of what was left?\n"
                                                    "Y/N").lower()
                if print_out == "y":
                    print_out_file(countries_list, countries_correct, region)

                stay_in_region = False
                break
            elif chosen_country in countries_list and chosen_country not in countries_correct:
                countries_correct.append(chosen_country)
                country_selected = regions_data_frame[regions_data_frame.name == chosen_country]
                country_cords = int(country_selected.x.iloc[0]), int(country_selected.y.iloc[0])
                message = ms.Message()
                message.write_name(chosen_country, country_cords)
            else:
                pass

tt.mainloop()
screen.exitonclick()
