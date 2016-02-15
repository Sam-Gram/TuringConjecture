#!/usr/bin/python
import sys
from Turing import TuringMachine
from States import initial_state, accepting_states, transition_function, final_states

t = TuringMachine(sys.argv[1], 
                  initial_state = "init",
                  final_states = final_states,
                  transition_function=transition_function,
                  show_transitions = True if len(sys.argv) > 2 else False)

while not t.final():
    t.step()

print("Result of the Turing machine calculation:")    
t.show_tape()
