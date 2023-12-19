from typing import Optional
from state_machine import StateMachine, State, Event, Transition

# Create a state machine
sm = StateMachine()

# Add states
states = [sm.add_state(str(i), f'State{i}') for i in range(0, 8)]

# Add events
events = [sm.add_event(str(i), f'Event{i}', states[i % 8]) for i in range(20)]

# Add transitions forming a graph structure
transitions = [
    sm.add_transition('0', states[0], states[1], events[0]),
    sm.add_transition('1', states[1], states[2], events[1]),
    sm.add_transition('2', states[2], states[3], events[2]),
    sm.add_transition('3', states[3], states[4], events[3]),
    sm.add_transition('4', states[4], states[5], events[4]),
    sm.add_transition('5', states[5], states[6], events[5]),
    sm.add_transition('6', states[6], states[7], events[6]),
    sm.add_transition('7', states[7], states[0], events[7]),
    sm.add_transition('8', states[0], states[2], events[8]),
    sm.add_transition('9', states[2], states[4], events[9]),
    sm.add_transition('10', states[4], states[6], events[10]),
    sm.add_transition('11', states[6], states[0], events[11]),
    sm.add_transition('12', states[1], states[3], events[12]),
    sm.add_transition('13', states[3], states[5], events[13]),
    sm.add_transition('14', states[5], states[7], events[14]),
    sm.add_transition('15', states[7], states[1], events[15]),
    sm.add_transition('16', states[0], states[3], events[16]),
    sm.add_transition('17', states[3], states[6], events[17]),
    sm.add_transition('18', states[6], states[1], events[18]),
    sm.add_transition('19', states[1], states[4], events[19])
]

sm.set_initial_state(states[0])

# Path 1
print("Path 1")
current_state: Optional[State] = states[0]
for i in range(8):
    print(f"Current state: {current_state.name if current_state else 'None'}")
    current_state = sm.next_state(str(i))
    print(f"Event: {events[i].name}")
print(f"Final state: {current_state.name if current_state else 'None'} IS State0 !!!")
assert current_state == states[0]

# Path 2
print("\nPath 2")
current_state = states[0]
for i in range(8, 12):
    print(f"Current state: {current_state.name if current_state else 'None'}")
    current_state = sm.next_state(str(i))
    print(f"Event: {events[i].name}")

print(f"Current state: {current_state.name if current_state else 'None'}")
current_state = sm.next_state(str(0))
print(f"Event: {events[0].name}")

for i in range(12, 16):
    print(f"Current state: {current_state.name if current_state else 'None'}")
    current_state = sm.next_state(str(i))
    print(f"Event: {events[i].name}")
print(f"Final state: {current_state.name if current_state else 'None'} IS State1 !!!")
assert current_state == states[1]
