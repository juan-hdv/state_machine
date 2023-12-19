"""
# STATE class
    Each state is represented by:
    - Id: string
    - Name: string

# EVENT class
    Events that triggers a change in the StateMachine. 
    If an event occurs and the StateMachine is in an initial state, 
    then the StateMachine will move from the initial state to the state 
    defined by the Transitions list

    Each event is represented by:
    - Id: string
    - name: string
    - state: State or None. None when the event is not a particular state event but a universal event.

# TRANSITION class
    Define a set of events making the StateMachine to pass from one state to another

    Each transition is represented by:
    - Id: string
    - from_state: State
    - to_state: State or None. None for final state
    - event: Event


# STATEMACHINE class

This class models a State Machine

## Data
    - states: the list of states
    - events: the list of events
    - transitions: the list of transitions
    - current_state: The current state of the StameMachine

## Methods
    - add_state (id: str, name: str) -> State
    - delete_state (id: str) -> None

    - add_event (id: str, name: str, state: State) -> Event
    - delete_event (id: str) -> None
    - associate_state_to_event (event_id: str, state: State) -> None

    - add_transition (id: str, from_state: State, to_state: Optional[State], event: Event) -> Transition
    - delete_transition (id: str) -> None

    - current_state() -> str
    - next_state(event: str) -> str

"""
from typing import Optional, List

class State:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

class Event:
    def __init__(self, id: str, name: str, state: State):
        self.id = id
        self.name = name
        self.state = state

class Transition:
    def __init__(self, id: str, from_state: State, to_state: Optional[State], event: Event):
        self.id = id
        self.from_state = from_state
        self.to_state = to_state
        self.event = event

class StateMachine:
    def __init__(self):
        self.states = []
        self.events = []
        self.transitions = []
        self._current_state = None


    def set_initial_state(self, state: State) -> None:
        self._current_state = state

    def add_state(self, id: str, name: str) -> State:
        state = State(id, name)
        self.states.append(state)
        return state

    def delete_state(self, id: str) -> None:
        self.states = [state for state in self.states if state.id != id]

    def add_event(self, id: str, name: str, state: State) -> Event:
        event = Event(id, name, state)
        self.events.append(event)
        return event

    def delete_event(self, id: str) -> None:
        self.events = [event for event in self.events if event.id != id]

    def associate_state_to_event(self, event_id: str, state: State) -> None:
        for event in self.events:
            if event.id == event_id:
                event.state = state

    def add_transition(self, id: str, from_state: State, to_state: Optional[State], event: Event) -> Transition:
        transition = Transition(id, from_state, to_state, event)
        self.transitions.append(transition)
        return transition

    def delete_transition(self, id: str) -> None:
        self.transitions = [transition for transition in self.transitions if transition.id != id]

    def current_state(self) -> State:
        return self._current_state

    def next_state(self, event_id: str) -> Optional[State]:
        for transition in self.transitions:
            if transition.event.id == event_id and transition.from_state == self._current_state:
                self._current_state = transition.to_state
                return self._current_state
        return None
