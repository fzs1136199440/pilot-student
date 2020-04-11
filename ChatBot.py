import time

class Bot:

    wait = 1

    def __init__(self):
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def run(self):
        time.sleep(Bot.wait)
        print(self.q)
        self.a = input()
        time.sleep(Bot.wait)
        print(self._think(self.a))


class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what's your name?"

    def _think(self, s):
        return f"Hello {s}"

class GreeetingBot(Bot):
    def __init__(self):
        self.q = "How are you today?"

    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too."
        else:
            return "Sorry to hear that."

import random
class favoriteColorBot(Bot):
    def __init__(self):
        self.q = "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"
