import requests
from bs4 import BeautifulSoup
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
                        <td class="worklist_middle">Doubleday</td><td class="worklist_date">April, 1974</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/_salem_s_lot.html">Salem's Lot</a></td>
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">October, 1975</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/shining_the.html">The Shining</a></td>
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">1977</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/stand_the.html">The Stand</a></td>
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">1978</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dead_zone_the.html">The Dead Zone</a></td> <td class="worklist_middle">Viking Press</td>
                        <td class="worklist_date">August, 1979</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/firestarter.html">Firestarter</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">September, 1980</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/cujo.html">Cujo</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">September, 1981</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_gunslinger_the.html">The Dark Tower: The Gunslinger</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td> 
                        <td class="worklist_date">June, 1982</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/pet_sematary.html">Pet Sematary</a></td> 
                        <td class="worklist_middle">Doubleday</td> 
                        <td class="worklist_date">1983</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/christine.html">Christine</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">April, 1983</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/talisman_the.html">The Talisman</a></td>
                        <td class="worklist_middle">G.P. Putnam's &amp; Sons</td>
                        <td class="worklist_date">November, 1984</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/cycle_of_the_werewolf.html">Cycle of the Werewolf</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">April, 1985</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/it.html">IT</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">September, 1986</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/eyes_of_the_dragon_the.html">The Eyes of the Dragon</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">February, 1987</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_drawing_of_the_three_the.html">The Dark Tower: The Drawing of the Three</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td> 
                        <td class="worklist_date">May, 1987</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/misery.html">Misery</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">June, 1987</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/tommyknockers_the.html">The Tommyknockers</a></td> 
                        <td class="worklist_middle">G.P. Putnam's &amp; Sons</td> 
                        <td class="worklist_date">November, 1987</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_half_the.html">The Dark Half</a></td> <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">November, 1989</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/stand_the_complete__uncut_edition_the.html">The Stand: The Complete &amp; Uncut Edition</a></td> 
                        <td class="worklist_middle">Doubleday</td>
                        <td class="worklist_date">May, 1990</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/needful_things.html">Needful Things</a></td> <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1991</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title">
                        <a href="https://www.stephenking.com/library/novel/dark_tower_the_waste_lands_the.html">The Dark Tower: The Waste Lands</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td> 
                        <td class="worklist_date">August, 1991</td>
                    </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/gerald_s_game.html">Gerald's Game</a></td> <td class="worklist_middle">Viking Press</td>
                        <td class="worklist_date">1992</td>
                    </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dolores_claiborne.html">Dolores Claiborne</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1993</td>
                    </tr>
                <tr class="alternate_light">
                    <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/insomnia.html">Insomnia</a></td> 
                    <td class="worklist_middle">Viking Press</td> 
                    <td class="worklist_date">1994</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/rose_madder.html">Rose Madder</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">1995</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/desperation.html">Desperation</a></td>
                        <td class="worklist_middle">Viking Press</td>
                        <td class="worklist_date">1996</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_two_dead_girls_the.html">The Green Mile: The Two Dead Girls</a></td> 
                        <td class="worklist_middle">Signet</td>
                        <td class="worklist_date">March, 1996</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_mouse_on_the_mile_the.html">The Green Mile: The Mouse on the Mile</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">April, 1996</td>
                </tr>
                <tr class="alternate_dark">
                    <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_coffey_s_hands_the.html">The Green Mile: Coffey's Hands</a></td> 
                    <td class="worklist_middle">Signet</td> 
                    <td class="worklist_date">May, 1996</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_bad_death_of_eduard_delacroix_the.html">The Green Mile: The Bad Death of Eduard Delacroix</a></td>
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">June, 1996</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_night_journey_the.html">The Green Mile: Night Journey</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">July, 1996</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_coffey_on_the_mile_the.html">The Green Mile: Coffey on the Mile</a></td> 
                        <td class="worklist_middle">Signet</td> 
                        <td class="worklist_date">August, 1996</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_wizard_and_glass_the.html">The Dark Tower: Wizard and Glass</a></td> 
                        <td class="worklist_middle">Donald M. Grant, Publisher</td>
                        <td class="worklist_date">November, 1997</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/bag_of_bones.html">Bag of Bones</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">September, 1998</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/girl_who_loved_tom_gordon_the.html">The Girl Who Loved Tom Gordon</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">April, 1999</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/green_mile_the_complete_serial_novel_the.html">The Green Mile: The Complete Serial Novel</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2000</td>
                </tr>
                <tr class="alternate_dark">
                    <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dreamcatcher.html">Dreamcatcher</a></td>
                    <td class="worklist_middle">Scribner</td> 
                    <td class="worklist_date">March, 2001</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/black_house.html">Black House</a></td> 
                        <td class="worklist_middle">Random House</td>
                        <td class="worklist_date">September, 2001</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/from_a_buick_8.html">From A Buick 8</a></td> <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">2002</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_gunslinger_(revised)_the.html">The Dark Tower: The Gunslinger (Revised)</a></td> 
                        <td class="worklist_middle">Viking Press</td> 
                        <td class="worklist_date">June, 2003</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_wolves_of_the_calla_the.html">The Dark Tower: Wolves of the Calla</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">November, 2003</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_song_of_susannah_the.html">The Dark Tower: Song of Susannah</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">June, 2004</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the.html">The Dark Tower</a></td> <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">September, 2004</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/colorado_kid_the.html">The Colorado Kid</a></td> 
                        <td class="worklist_middle">Dorchester Publishing Co., Inc.</td> 
                        <td class="worklist_date">October, 2005</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/_salem_s_lot_illustrated_edition.html">Salem's Lot Illustrated Edition</a></td> 
                        <td class="worklist_middle">Doubleday</td> 
                        <td class="worklist_date">November, 2005</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/cell.html">Cell</a></td>
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">January, 2006</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/lisey_s_story.html">Lisey's Story</a></td> <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">October, 2006</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/duma_key.html">Duma Key</a></td>
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">January, 2008</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/under_the_dome.html">Under the Dome</a></td> <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">November, 2009</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/11_22_63.html">11/22/63</a></td> 
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">November, 2011</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/dark_tower_the_wind_through_the_keyhole_the.html">The Dark Tower: The Wind Through the Keyhole</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">April, 2012</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/doctor_sleep.html">Doctor Sleep</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">2013</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/joyland.html">Joyland</a></td>
                        <td class="worklist_middle">Titan Books</td>
                        <td class="worklist_date">June, 2013</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/mr._mercedes.html">Mr. Mercedes</a></td> 
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">June, 2014</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/revival.html">Revival</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">November, 2014</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/finders_keepers.html">Finders Keepers</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">June, 2015</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/joyland_illustrated_edition.html">Joyland Illustrated Edition</a></td> 
                        <td class="worklist_middle">Hard Case Crime</td> 
                        <td class="worklist_date">September, 2015</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/end_of_watch.html">End of Watch</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">June, 2016</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/sleeping_beauties.html">Sleeping Beauties</a></td> 
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">September, 2017</td>
                </tr>
                <tr class="alternate_light">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/outsider_the.html">The Outsider</a></td>
                        <td class="worklist_middle">Scribner</td>
                        <td class="worklist_date">May, 2018</td>
                </tr>
                <tr class="alternate_dark">
                        <td class="worklist_title"><a href="https://www.stephenking.com/library/novel/institute_the.html">The Institute</a></td> 
                        <td class="worklist_middle">Scribner</td> 
                        <td class="worklist_date">September, 2019</td>
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

database = dict(zip(book_titles, book_dates))

print(database)





