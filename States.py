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
                       ("fifth", "1"):("sixth","0","L"), 
                       ("sixth", "0"):("carry-add-one","0","R"),
                       ("sixth", "1")
                       ("carry-add-one", "1")
                       ("move-left", " "):()
                       ("move-left", "1"):()
                       ("move-left", "0"):()
                       
                       
                       }
final_states = ["final"]
