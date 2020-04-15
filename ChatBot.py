from time import sleep
from termcolor import colored

class Bot:

    wait = 1

    def __init__(self):
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'green')

    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))


class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what's your name?"

    def _think(self, s):
        return f"Hello {s}"

class GreetingBot(Bot):
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
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}."

from simpleeval import simple_eval

class CalcBot(Bot):
    def __init__(self):
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try:"

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}."

    
        
        
            

# 下面我们需要一个主流程把上面的所有 Bot 串起来（这样就可以一起运行了），这是我们的对话系统的主类定义：

class Magpie:

    def __init__(self, wait=1):
         Bot.wait = wait
         self.bots = []

    def add(self, bot):
        self.bots.append(bot) # list.append()用于在列表末尾添加新的对象。

    def _prompt(self, s):
        print(s)
        print()

    def run(self):
        self._prompt("This is Magpie dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()


# 初始化一个Magpie实例来运行：

# 创建一个聊天延时为 1s 的对话系统
magpie = Magpie(1)
# 向其中加入我们已经定义好的各个对话 bot 的对象实例
magpie.add(HelloBot())
magpie.add(GreetingBot())
magpie.add(favoriteColorBot())
# 运行它
magpie.run()