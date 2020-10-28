from random import randint
class User:
    def __init__(self,name):
        self.name = name
        self.pos =0

    def user_move(self,pos):
        if pos == 100:
            return True
        else :
            self.pos =pos
            return False

    def user_get_pos(self):
        return self.pos

    def user_get_name(self):
        return self.name



