import unittest
from state_machine import StateMachine, State, Event, Transition

class TestStateMachine(unittest.TestCase):
    def setUp(self):
        self.sm = StateMachine()
        self.state1 = self.sm.add_state('1', 'State1')
        self.state2 = self.sm.add_state('2', 'State2')
        self.event1 = self.sm.add_event('1', 'Event1', self.state1)

    def test_add_state(self):
        state3 = self.sm.add_state('3', 'State3')
        self.assertIn(state3, self.sm.states)

    def test_delete_state(self):
        self.sm.delete_state('1')
        self.assertNotIn(self.state1, self.sm.states)

    def test_add_event(self):
        event2 = self.sm.add_event('2', 'Event2', self.state2)
        self.assertIn(event2, self.sm.events)

    def test_delete_event(self):
        self.sm.delete_event('1')
        self.assertNotIn(self.event1, self.sm.events)

    def test_associate_state_to_event(self):
        self.sm.associate_state_to_event('1', self.state2)
        self.assertEqual(self.event1.state, self.state2)

    def test_add_transition(self):
        transition = self.sm.add_transition('1', self.state1, self.state2, self.event1)
        self.assertIn(transition, self.sm.transitions)

    def test_delete_transition(self):
        transition = self.sm.add_transition('2', self.state1, self.state2, self.event1)
        self.sm.delete_transition('2')
        self.assertNotIn(transition, self.sm.transitions)

    def test_current_state(self):
        self.sm._current_state = self.state1
        self.assertEqual(self.sm.current_state(), self.state1)

    def test_next_state(self):
        self.sm._current_state = self.state1
        self.sm.add_transition('1', self.state1, self.state2, self.event1)
        self.assertEqual(self.sm.next_state('1'), self.state2)

if __name__ == '__main__':
    unittest.main()
