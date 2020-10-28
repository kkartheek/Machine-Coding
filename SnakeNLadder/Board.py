
class Cell:
    def __init__(self,num=-1):
        self.num = num
        self.snake = []
        self.ladder = []
    def add_snake(self,start,end):
        if len(self.ladder)==0:
            self.snake.append(start)
            self.snake.append(end)
            #print(start,end,len(self.snake),self.snake[0],self.snake[1])
        else :
            print(f"ladder already present between {self.ladder[0]} and {self.ladder[1]}")

    def add_ladder(self,start,end):
        if len(self.snake) ==0:
            self.ladder.append(start)
            self.ladder.append(end)
        else :
            print(f"Snake already present between {self.snake[0]} and {self.snake[1]}")

    def has_snake(self):
        if len(self.snake) > 0 and self.snake[0]== self.num:
            return True
        else:
            return False

    def has_ladder(self):
        if len(self.ladder) >0 and self.ladder[0]==self.num :
            return True
        else:
            return False

    def get_snake(self):
        if self.has_snake():
            return self.snake[1]

    def get_ladder(self):
        if self.has_ladder():
            return self.ladder[1]