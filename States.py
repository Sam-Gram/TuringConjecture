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
                       ("fifth", "1"):("multiply","1","R"),
                       ("multiply", " "):("first-carry","0","L"), #Why isn't my 0 being written in?
                       ("first-carry", "1"):("second-carry","0","L"),
                       ("second-carry", "0"):("check","1","L"),
                       ("second-carry", "1"):("one-right","0","R"), #one-right
                       ("check", "0"):("check","0","L"),
                       ("check", "1"):("zero-right","1","R"),
                       ("one-right", "0"):("jump-carry","1","L"), #jump-carry
                       ("one-right", "1"):("jump-carry","0","L"),
                       ("zero-right", "0"):("move-left","1","L"),
                       ("zero-right", "1"):("jump-carry","0","L"),
                       ("carry", " "):("init","1","L"), # this needs to be init, but I marked it final so I could look at the tape (no infinite loop)
                       ("carry", "0"):("check","1","L"),
                       ("carry", "1"):("one-right","1","R"),
                       ("move-left", "1"):("check","1","L"),
                       ("jump-carry", "0"):("carry","0","L"), #carry
                       ("jump-carry", "1"):("carry","0","L"),
                       ("check", " "):("init"," ","N")
                       }
final_states = ["final"]
