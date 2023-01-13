girls = 5
hair_clip = 10
total_clips = girls * hair_clip

one    = [1,1,1,1,1,1,1,1,1,1]
two    = [1,1,1,1,1,1,1,1,1,1]
three  = [1,1,1,1,1,1,1,1,1,1]
four   = [1,1,1,1,1,1,1,1,1,1]
five   = [1,1,1,1,1,1,1,1,1,1]

# 面向过程解题法
def take_in(p_human:list):
    p_human.append(1)
    pass

def take_out(p_human:list):
    p_human.pop()
    pass

def process():
    take_out(one)
    
    take_in(one)
    take_out(two)
    
    take_out(three)
    take_in(two)
    
    take_out(four)
    take_in(three)

    take_out(five)
    take_in(four)

    print(len(five))
    pass

# 面向对象解题法
class GongZhu:
    def __init__(self) -> None:
        self.hair_clip = [1,1,1,1,1,1,1,1,1,1]
        pass
    def take_in(self):
        self.hair_clip.append(1)
    def take_out(self):
        self.hair_clip.pop()
    pass

def oopProcess():
    One   = GongZhu()
    Two   = GongZhu()
    Three = GongZhu()
    Four  = GongZhu()
    Five  = GongZhu()
    seq   = [One,Two,Three,Four,Five]
    def init():
        One.take_out()
        pass
    def lun():
        seq[0].take_in()
        seq[1].take_out()
        seq[2].take_out()

        seq[1].take_in()
        seq[3].take_out()
        seq[2].take_out()
        
        seq[4].take_out()
        seq[3].take_in()
        pass   
    init()
    lun()

    print(len(Five.hair_clip))
    pass

# 解题函数
# process()
oopProcess()

