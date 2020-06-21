import textwrap


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        cprint(f"You picked up a ${self.name}".format(
            self=self), "red", attrs=[])
