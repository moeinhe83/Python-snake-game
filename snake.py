# Snake Game

# Library
from tkinter import *
from random import randint

# Static value
GAME_WEITH = 600
GAME_HIGHT = 600
SPACE_SIZE = 30
SLOWNESS = 200
BODY_SIZE = 2
SNAKE_COLOR = 'red'
FOOD_COLOR = 'white'
BACKGROUND_COLOR = 'black'

# Dynamic value
score = 0
direction = 'down'

# Class For Snake
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)


# Class For Food
class Food:
    def __init__(self):
        x = randint(0, (GAME_WEITH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = randint(0, (GAME_HIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        square = canvas.create_oval(
            x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag='food')

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(
        x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        lable.config(text=f'Score: {score}')
        canvas.delete('food')
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_game_over(snake):
        game_over()
    else:
        window.after(SLOWNESS, next_turn, snake, food)

# Function For Game Over
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=("Latha", 60), text="Game Over", fill='red', tag='gameover')

# Function For Check Game Over 
def check_game_over(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x > GAME_WEITH:
        return True
    elif y < 0 or y > GAME_HIGHT:
        return True

    for sq in snake.coordinates[1:]:
        if x == sq[0] and y == sq[1]:
            return True
    return False

# Function For Change Direction 
def change_direction(new_dir):
    global direction
    if new_dir == 'left':
        if direction != 'right':
            direction = new_dir
    elif new_dir == 'right':
        if direction != 'left':
            direction = new_dir
    elif new_dir == 'up':
        if direction != 'down':
            direction = new_dir
    elif new_dir == 'down':
        if direction != 'up':
            direction = new_dir

# Make graphic window
window = Tk()
window.title('Snake Game')
window.resizable(height=False, width=False)

# Lable For Score
lable = Label(window, text=f'Score: {score}', font=('Latha', 30))
lable.pack()  # Pack method for run lable in window

# Dimensions Window 
canvas = Canvas(window, bg=BACKGROUND_COLOR,
                height=GAME_HIGHT, width=GAME_WEITH)
canvas.pack()  # Pack method for run canvas in window
window.update()

# Key For Keyboard
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Run Snake & Food Class
snake = Snake()
food = Food()
next_turn(snake, food)


# Show graphic window
window.mainloop()

# Finish
# Create By Moein Heshmati