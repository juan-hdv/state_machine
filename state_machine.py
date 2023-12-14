"""
This class models a State Machine

The StateMachine is ocmposed by:

# STATES

Represent the list of states.

## Data
    - states: the list of states

    Each state is represented by:
    - Id: string
    - Name: string

## Methods
    - create_node (id, name)
    - delete_node (id)


# EVENTS

Events that triggers a change in the StateMachine. 
If an event occurs and the StateMachine is in an initial state, 
then the StateMachine will move from the initial state to the state 
defined by the Transitions list

## Data
    - events: the list of events

    Each event is represented by:
    - Id: string
    - name: string
    - state: State or None. None when the event is not a particular state event but a universal event.

## Methods
    - create_event (id, name, state)
    - delete_event (id)
    - associate_state_to_event (id, state)

# TRANSITIONS

Define a set of events making the StateMachine to pass from one state to another

## Data
    - transitions: list of transitions

    Each transition is represented by:
    - Id: string
    - from_state: State
    - to_state: State or None. None for final state
    - event: Event

## Methods
    - create_transition (id, from_state, to_state, event)
    - delete_transition (id)
    - current_state() -> State. Returns current state of the StateMachine
    - next_state(event)-> State. Returns the next state of the StateMachine, given an event
"""

