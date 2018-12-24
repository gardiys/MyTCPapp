

class Action:
    """Class for prosessing actions"""

    actions = {}

    def __init__(self):
        pass

    def add_actions(self, key, value):
        if key not in self.actions:
            self.actions[key] = set()
        self.actions[key].add(value)

