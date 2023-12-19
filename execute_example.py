from typing import Optional
from state_machine import StateMachine, State, Event, Transition

# Create a state machine
sm = StateMachine()

# Add states
states = [sm.add_state(str(i), f'State{i}') for i in range(1, 9)]

# Add events
events = [sm.add_event(str(i), f'Event{i}', states[i % 8]) for i in range(20)]

# Add transitions
transitions = [sm.add_transition(str(i), states[i % 8], states[(i+1) % 8], events[i]) for i in range(20)]

# Path 1
print("Path 1")
current_state: Optional[State] = states[0]
for i in range(20):
    print(f"Current state: {current_state.name if current_state else 'None'}")
    current_state = sm.next_state(str(i))
    print(f"Event: {events[i].name}")
print(f"Final state: {current_state.name if current_state else 'None'}")

# Path 2
print("\nPath 2")
current_state = states[0]
for i in range(19, -1, -1):
    print(f"Current state: {current_state.name if current_state else 'None'}")
    current_state = sm.next_state(str(i))
    print(f"Event: {events[i].name}")
print(f"Final state: {current_state.name if current_state else 'None'}")

