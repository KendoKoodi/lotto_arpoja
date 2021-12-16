# lotto_arpoja

This program is supposed to pick 7 from 40 number pool of numbers (Finnish monopoly company Veikkaus' lottery) forming a lottery line and one additional extra number from the remaining 33 numbers. It is part of a school project on basic Pyhon course.

Lottery engine shuffles the list of numbers user chosen times (4 is default). Limit of suffles is 1-100. Numbers are shuffled each time before popping. Index of number that is popped is chosen with random.

User can generate 1-10 lines at one go.

Lines are saved to a file (/numerot/arvotut_lotto.txt).

TODO:
  * addin a star number to end of line, that is randomly picked and copied from the 7 numbers drawn before
  * moving date adding code to it's own file and making it fuction
  * making the date adding function shift the actual lottery day when religious holiday happens to be on Saturday
  * shift to using SQLite for saving the lines (...should fix the way too complicated row parser also)
  * simplify the way line of number is formed so that it is a single list variable rather than tuple containing two lists
  * comparing function that can compare actual Veikkaus numbers to generated numbers and find hits.
