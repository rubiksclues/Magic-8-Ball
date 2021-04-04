# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:56:32 2021

@author: Courtney
"""
import random
print("""       -- WELCOME TO THE CERTAINLY MAGIC 8 BALL! --
Ask a question and recieve a fortune with only a 99% chance it will be vague, unhelpful, or barely a fortune at all!
  It's 100% Magic! Spectacular! You CAN'T miss this!
 Maybe give it a shake?""")

#sets program responses
fortunes = [
"Yikes! You might step on IDK...a lego or something?",
"Jeez, all you're going to do is type SHAKE again...really?",
"WOAH youre...you're gonna pay lots of bills. Sorry bout your luck bud",
"*yaaaaawn* Sorry, I don't really FEEEEEL like peering into to future right now...maybe shake it again and something else will happen",
"You may or may not have some sort of experience someday...",
"Never, for any reason, ever, do anything, to anyone, no matter what",
"Maybe one day, you will stop shaking this ball and end the program. If this is your first fortune, sorry I'm just gettin vibes off of you",
"You will be reading this sentence. Pretty riveting, moving, and life-changing I'm sure",
"You will continue to require food, water, and sleep to survive. Who else could have let you forsee such news?",
"TMI but it seems to be that you'll have to pee. Eventually. You probably noticed that rhymed but who can ever be sure...",
"It looks like...This can't bee...According to all known laws of aviation theres no way a bee should be able to fly.",
"If I make any references they will be outdated, causing you to shake your head in shame. Your fault for shaking the magic 8 ball, I say...",
".............fruits.",
"You are, or are not, alive.",
"Ooh wait uhm, sorry but I'm on my lunch break right now...shake again another time, thaaaaanks.",
"Laundry day? I'm honestly just saying whatever.",
"Hey do you have 5 dollars I could borrow? Can't tell if you do but I honestly just want to buy candy bar and never pay you back. Be a friend?",
"I can see you....far in the future....AMAZING! You will be...reading...something.",
 ]

#runs program on loop until program is ended by user input
RunProgram = True

"""creates a user input running on while loop, prints randomly chosen response from fortunes variable,
ends program when user inputs STOP command"""
while RunProgram:
  shake = input("""type SHAKE to well...shake the super magic 8 ball.
  When you inevitably get sick of this, type STOP to end the program.
""")
  if shake == "SHAKE":
    print("I suspect in your future..." + random.choice(fortunes))
  if shake == "STOP":
    RunProgram = False

if not RunProgram:
  print("-- Well you certainly know how to waste time, so long sucker! --")