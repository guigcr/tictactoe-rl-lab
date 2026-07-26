import random
from collections import namedtuple

Point = namedtuple('Point', 'x, y')

# Constants
BLOCK_SIZE = 20

class SnakeGameAI:
    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        # Initial direction: Right
        self.direction = (BLOCK_SIZE, 0)
        self.head = Point(self.width / 2, self.height / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
        ]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_iteration += 1
        
        # 1. Update direction based on action: [straight, right, left]
        self._move(action)
        self.snake.insert(0, self.head)
        
        # 2. Check if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 3. Check if food was eaten
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        return reward, game_over, self.score

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # Wall collision
        if pt.x > self.width - BLOCK_SIZE or pt.x < 0 or pt.y > self.height - BLOCK_SIZE or pt.y < 0:
            return True
        # Self collision
        if pt in self.snake[1:]:
            return True
        return False

    def _move(self, action):
        # Clockwise directions: [Right, Down, Left, Up]
        clockwise = [(BLOCK_SIZE, 0), (0, -BLOCK_SIZE), (-BLOCK_SIZE, 0), (0, BLOCK_SIZE)]
        idx = clockwise.index(self.direction)

        if action == [1, 0, 0]:
            new_dir = clockwise[idx]  # Keep going straight
        elif action == [0, 1, 0]:
            next_idx = (idx + 1) % 4
            new_dir = clockwise[next_idx]  # Turn right
        else:  # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clockwise[next_idx]  # Turn left

        self.direction = new_dir
        x = self.head.x + self.direction[0]
        y = self.head.y + self.direction[1]
        self.head = Point(x, y)
