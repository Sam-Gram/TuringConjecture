initial_state = "init",
accepting_states = ["final"],
transition_function = {("second","0"):("second", "0", "R"),
                       ("second","1"):("second", "1", "R"),
                       ("second"," "):("third"," ","L"),
                       ("init"," "):("second"," ", "R"),
                       ("third", "0"):("third", " ", "L"), # It's even, divide by 2
                       ("third", "1"):("fourth", "1", "L"), # Check first to see if it is done, then go to 3x+1
                       ("fourth", " "):("final", " ", "N"),
                       ("fourth", "1"):("fifth", "1", "R"), # We now need to multiply by 3 and add 1
                       ("fourth", "0"):("fifth", "0", "R"), # Pretty sure we can delete this
                       ("fifth", "1"):("sixth", "1", "R"),
                       ("sixth", " "):("seventh", "0", "L"),
                       ("seventh", "1"):("eighth", "1", "R"),
                       ("eighth", "0"):("ninth","1","L"),
                       ("ninth","0"):("tenth","0","L"),
                       ("ninth","1"):("eleventh","1","L"),
                       ("ninth"," "):("init"," ","N"), #Restart on new number
                       ("tenth","0"):("ninth","0","N"),
                       ("eleventh"," "):("init"," ","N"),
                       ("eleventh","1"):("eleventh", "1", "R"),
                       ("twelfth","1"):("ninth", "0", "L")
                       }
final_states = ["final"]
