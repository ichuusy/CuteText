import random
import datetime

class CuteText():
    def __init__(self):
        texts = ["(๑o_o)╦╤─","( •́⌒•̀)⌐╦╦═─","( ❛ᴗ❛)╦╦═─","(╹ᴗ╹)━★","(✿°3°)≧U≦)( ・・)つ―●○◎-","( ๑•◡•)╦̵̵̿╤──","(๑o_o)╦╤─","( •́⌒•̀)⌐╦╦═─","( ❛ᴗ❛)╦╦═─","(╹ᴗ╹)━★","(✿°3°)≧U≦)( ・・)つ―●○◎-","( ๑•◡•)╦̵̵̿╤──","(◕o◕)=ε/̵͇̿̿/’̿’̿ ̿(˚▽˚’!)(˚▽˚’!)(˚▽˚’!)","( •́∇•̀)⌐╦╦═─","( ❛‿❛)▄ ┻┳","(҂`з´)⌐╦╦═─","(╹ω╹)╦̵̵̿╤──","(˵≧.≦)⌐╦╦═─","(✿ ❛ω❛)⌐╦╦═─","( ❛U❛)▄ ┻┳","(❛_❛) ▄┻┳","(✿>▽<)╦̵̵̿╤─","( ͡^ ͜ ͡^ ) ╦╤─","( •́_•̀)⌐╦╦═─ ","( ▼o▼)o┳-","( ▼▼)o┳-","( ❛ᴗ❛)╦╦═─","( ͡° ͜ʖ ͡°)╦╦═─","(≧_≦)⌐╦╦═─"," ( ๑•◡•)╦̵̵̿╤──","(●▽●)⌐╦╦═─","(✿❛_❛) ▄┻┳","( ͡^ . ͡^ ) ╦╤─","( ͡° ͜ʖ ͡° )▄︻┻┳═一","(҂×▵×)╦╤─","(╹-╹)▄ ┻┳─","ξ(✿❛_❛) ▄┻┳","( ͡° ͜ ͡° )▄︻┻┳═一","( ❛o❛)▄ ┻┳★","ξ(✿ ❛‿❛)ξ▄︻┻┳═","ʕ >ᴥ<ʔ︻̷┻̿═━一-","━╤デ╦︻(❛u❛✿)","( ❛U❛)╦╦═─","( ❛‿❛)▄︻┻┳═"]
        self.text = random.choice(texts)

    def cuteprint(self,args): # Prints cute text.
        return f"{self.text} {args}"

    def cutetime(self,set,time : int=None): # Prints cute times.
        now = datetime.datetime.now()
        if set == "now":
            return f"{self.text} {datetime.datetime.ndow()}"
        elif set == "timestamp":
            return f"{self.text} {datetime.datetime.timestamp(now)}"
        elif set == "fromtimestamp":
            if time == None:
                raise AttributeError
            else:
                return f"{self.text} {datetime.datetime.fromtimestamp(time)}"
        elif set == "ctime":
            return f"{self.text} {datetime.datetime.ctime(now)}"
        else:
            raise AttributeError