import requests
from bs4 import BeautifulSoup
import re
"""
Basic Database for Stephen King books

most likely use dictionaries to store books as keys
and genres, date published, and etc as values

program will allow you to search through date, genres, etc
also can add books if missing or delete books that are mistakes
"""

html_doc = """
<html>
    <head></head>
    <body>
        <table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="worklist_table">
            <tbody>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/carrie.html">Carrie</a></td>
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">1974</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/_salem_s_lot.html">Salem's Lot</a></td>
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">1975</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/shining_the.html">The Shining</a></td>
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">1977</td>
                        <td class="worklist_genre">horror fiction, psychological horror, cccult fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/stand_the.html">The Stand</a></td>
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">1978</td>
                        <td class="worklist_genre">horror fiction, fantasy, fantastique</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dead_zone_the.html">The Dead Zone</a></td> <td class="worklist_middle">Viking Press</td>
                        <td class="worklist_date">1979</td>
                        <td class="worklist_genre">thriller, horror fiction, detective fiction, fantastic</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/firestarter.html">Firestarter</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1980</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/cujo.html">Cujo</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1981</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_gunslinger_the.html">The Dark Tower: The Gunslinger</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td> 
                        <td class="worklist_date">1982</td>
                        <td class="worklist_genre">fantasy, western</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/pet_sematary.html">Pet Sematary</a></td> 
                        <td class="worklist_middle">Doubleday</td> 
                        <td class="worklist_date">1983</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/christine.html">Christine</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1983</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/talisman_the.html">The Talisman</a></td>
                        <td class="worklist_middle">G.P. Putnam's &amp; Sons</td>
                        <td class="worklist_date">1984</td>
                        <td class="worklist_genre">science fiction, horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/cycle_of_the_werewolf.html">Cycle of the Werewolf</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">1985</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/it.html">IT</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1986</td>
                        <td class="worklist_genre">horror fiction, coming-of-Age fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/eyes_of_the_dragon_the.html">The Eyes of the Dragon</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1987</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_drawing_of_the_three_the.html">The Dark Tower: The Drawing of the Three</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td> 
                        <td class="worklist_date">1987</td>
                        <td class="worklist_genre">fantasy, horror, science fiction, western</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/misery.html">Misery</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1987</td>
                        <td class="worklist_genre">horror fiction, psychological thriller, psychological horror</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/tommyknockers_the.html">The Tommyknockers</a></td> 
                        <td class="worklist_middle">G.P. Putnam's &amp; Sons</td> 
                        <td class="worklist_date">1987</td>
                        <td class="worklist_genre">horror fiction, psychological thriller, psychological horror</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_half_the.html">The Dark Half</a></td>
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1989</td>
                        <td class="worklist_genre">thriller, horror fiction, psychological horror</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/stand_the_complete__uncut_edition_the.html">The Stand: The Complete &amp; Uncut Edition</a></td> 
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">1990</td>
                        <td class="worklist_genre">horror fiction, fantasy, fantastique</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/needful_things.html">Needful Things</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1991</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_waste_lands_the.html">The Dark Tower: The Waste Lands</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td> 
                        <td class="worklist_date">1991</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/gerald_s_game.html">Gerald's Game</a></td>
                        <td class="worklist_middle">Viking Press</td>
                        <td class="worklist_date">1992</td>
                        <td class="worklist_genre">suspense, psychological horror</td>
                 </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dolores_claiborne.html">Dolores Claiborne</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1993</td>
                        <td class="worklist_genre">horror fiction, psychological thriller</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/insomnia.html">Insomnia</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1994</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/rose_madder.html">Rose Madder</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1995</td>
                        <td class="worklist_genre">thriller, horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/desperation.html">Desperation</a></td>
                        <td class="worklist_middle">Viking Press</td>
                        <td class="worklist_date">1996</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_two_dead_girls_the.html">The Green Mile: The Two Dead Girls</a></td> 
                        <td class="worklist_middle">Signet</td>
                        <td class="worklist_date">1996</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction, serial, southern gothic, fantastic</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_mouse_on_the_mile_the.html">The Green Mile: The Mouse on the Mile</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">1996</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction, serial, southern gothic, fantastic</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_coffey_s_hands_the.html">The Green Mile: Coffey's Hands</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">1996</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction, serial, southern gothic, fantastic</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_bad_death_of_eduard_delacroix_the.html">The Green Mile: The Bad Death of Eduard Delacroix</a></td>
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">1996</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction, serial, southern gothic, fantastic</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_night_journey_the.html">The Green Mile: Night Journey</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">1996</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction, serial, southern gothic, fantastic</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_coffey_on_the_mile_the.html">The Green Mile: Coffey on the Mile</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">1996</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction, serial, southern gothic, fantastic</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_wizard_and_glass_the.html">The Dark Tower: Wizard and Glass</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td>
                        <td class="worklist_date">1997</td>
                        <td class="worklist_genre">fantasy, horror, science fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/bag_of_bones.html">Bag of Bones</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">1998</td>
                        <td class="worklist_genre">Novel, ghost story, horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/girl_who_loved_tom_gordon_the.html">The Girl Who Loved Tom Gordon</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">1999</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_complete_serial_novel_the.html">The Green Mile: The Complete Serial Novel</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2000</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction, serial, southern gothic, fantastic</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dreamcatcher.html">Dreamcatcher</a></td>
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2001</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/black_house.html">Black House</a></td> 
                        <td class="worklist_middle">Random House</td>
                        <td class="worklist_date">2001</td>
                        <td class="worklist_genre">science fiction, horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/from_a_buick_8.html">From A Buick 8</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2002</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_gunslinger_(revised)_the.html">The Dark Tower: The Gunslinger (Revised)</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">2003</td>
                        <td class="worklist_genre">fantasy, western</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_wolves_of_the_calla_the.html">The Dark Tower: Wolves of the Calla</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2003</td>
                        <td class="worklist_genre">fantasy, horror, science fiction, western</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_song_of_susannah_the.html">The Dark Tower: Song of Susannah</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2004</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the.html">The Dark Tower</a></td> 
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2004</td>
                        <td class="worklist_genre">dark fantasy, science fiction, horror fiction, western fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/colorado_kid_the.html">The Colorado Kid</a></td> 
                        <td class="worklist_middle">Dorchester Publishing Co., Inc.</td> 
                        <td class="worklist_date">2005</td>
                        <td class="worklist_genre">mystery, crime fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/_salem_s_lot_illustrated_edition.html">Salem's Lot Illustrated Edition</a></td> 
                        <td class="worklist_middle">Doubleday</td> 
                        <td class="worklist_date">2005</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/cell.html">Cell</a></td>
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2006</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/lisey_s_story.html">Lisey's Story</a></td>
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2006</td>
                        <td class="worklist_genre">horror, gothic</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/duma_key.html">Duma Key</a></td>
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2008</td>
                        <td class="worklist_genre">horror fiction, psychological horror, paranormal fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/under_the_dome.html">Under the Dome</a></td>
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2009</td>
                        <td class="worklist_genre">novel, horror fiction, dystopian fiction, political fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/11_22_63.html">11/22/63</a></td> 
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2011</td>
                        <td class="worklist_genre">science fiction, alternate history</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_wind_through_the_keyhole_the.html">The Dark Tower: The Wind Through the Keyhole</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2012</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/doctor_sleep.html">Doctor Sleep</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2013</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/joyland.html">Joyland</a></td>
                        <td class="worklist_middle">Titan Books</td>
                        <td class="worklist_date">2013</td>
                        <td class="worklist_genre">Ghost story, horror fiction, crime fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/mr._mercedes.html">Mr. Mercedes</a></td> 
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2014</td>
                        <td class="worklist_genre">horror fiction, detective fiction, hardboiled</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/revival.html">Revival</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2014</td>
                        <td class="worklist_genre">horror fiction, suspense</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/finders_keepers.html">Finders Keepers</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2015</td>
                        <td class="worklist_genre">novel</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/joyland_illustrated_edition.html">Joyland Illustrated Edition</a></td> 
                        <td class="worklist_middle">Hard Case crime</td> 
                        <td class="worklist_date">2015</td>
                        <td class="worklist_genre">ghost story, horror fiction, crime fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/end_of_watch.html">End of Watch</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2016</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/sleeping_beauties.html">Sleeping Beauties</a></td> 
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2017</td>
                        <td class="worklist_genre">horror fiction, fantasy fiction</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/outsider_the.html">The Outsider</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2018</td>
                        <td class="worklist_genre">horror fiction</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/institute_the.html">The Institute</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2019</td>
                        <td class="worklist_genre">horror fiction</td>
                 </tr>
            </tbody>
        </table>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

book_titles = []
book_dates = []
book_genres = []

for a_tag in soup.find_all("a"):
    book_titles.append(a_tag.text)

#print(book_titles)

for td_tag in soup.find_all("td", class_="worklist_date"):
    book_dates.append(td_tag.text)

#print(book_dates)

for td_tag in soup.find_all("td", class_="worklist_genre"):
    book_genres.append(td_tag.text)


mappedA = zip(book_genres, book_dates)
mappedB = zip(book_titles, mappedA)
database = set(mappedB)
#print(database)

print("=" * 100)
print("\n\nWelcome to the Stephen King Basic Book Database!\n\n")
print("=" * 100)

while True:
    print("\nWhat would you like to do?")
    print("1. Search")
    print("2. Add a book (Coming Soon)")
    print("3. Take out a book (Coming Soon)")
    print("4. Exit database")
    to_do = input()

    if to_do == "1":

        print("\nHow would you like to search?")
        print("1. By genre")
        print("2. By publishing year")
        print("3. Show all book titles")
        print("4. Show all book titles and publishing year")
        print("5. Show all book titles and genres\n")

        search_choice = input()
        print("\n")

        if search_choice == "1":
            print("Search which of the following genres")
            print("1. Horror")
            print("2. Fantasy\n")

            search_choice_genre = input()
            if search_choice_genre == "1":
                # Books with genres "horror" or "horror fiction"
                for entry in database:
                    split_entry = entry[1][0].split(", ")
                    if 'horror fiction' in split_entry:
                        print(entry[0])
                    elif 'horror' in split_entry:
                        print(entry[0])
                    else:
                        pass

            elif search_choice_genre == "2":
                # Books with genres "fantasy fiction" or "fantasy" or "Dark fantasy"
                for entry in database:
                    split_entry = entry[1][0].split(", ")
                    if 'fantasy fiction' in split_entry:
                        print(entry[0])
                    elif 'fantasy' in split_entry:
                        print(entry[0])
                    elif 'Dark fantasy' in split_entry:
                        print(entry[0])
                    else:
                        pass

            else:
                print("Oops! This function has not yet been implemented. Coming soon!")

        elif search_choice == "2":
            print("What years would you like to search?")
            print("1. After and on 2000")
            print("2. Before 2000\n")

            search_choice_year = input()
            if search_choice_year == "1":
                # Books published later than year 2000
                for entry in database:
                    if int(entry[1][1]) >= 2000:
                        print(entry[0])

            elif search_choice_year == "2":
                # Books published earlier than 2000
                for entry in database:
                    if int(entry[1][1]) < 2000:
                        print(entry[0])

            else:
                print("Oops! This function has not yet been implemented. Coming soon!")
                exit()

        elif search_choice == "3":
            # Show all books with just titles
            for entry in database:
                print(entry[0])

        elif search_choice == "4":
            # Show all books with just titles and year
            for entry in database:
                print(entry[0], "- " + entry[1][1])

        elif search_choice == "5":
            # Show all books with just titles and their genres
            for entry in database:
                print(entry[0], "- " + entry[1][0])

        else:
            print("Oops! This function has not yet been implemented. Coming soon!")
            exit()
    '''
    elif to_do == "2":
        print("Add a book")

        print("Title: ")
        add_title = input()

        print("Genre: ")
        add_genre = input()

        print("Publishing year: ")
        add_year = input()

        book_titles.append(add_title)
        book_genres.append(add_genre)
        book_dates.append(add_year)

    elif to_do == "3":
        print("Delete a book")'''

    elif to_do == "4":
        exit()

    else:
        print("Invalid choice")




