
import random

class Grid:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0 for i in range(size)] for j in range(size)]
        self.score = 0

    def _get_empty_cells(self):
        return [(i, j) for i in range(self.size)
                for j in range(self.size)
                if self.grid[i][j] == 0]

    def _is_win(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 2048:
                    return True
        return False

    def _merge(self, row):
        merged = []
        prev = 0
        for num in row:
            if num == prev:
                merged[-1] *= 2
            else:
                merged.append(num)
            prev = num

        if len(row) != len(merged):
            self.score += 10 * sum(
                [x for x in merged if abs(x) == 1 or abs(x) == 2])

        while merged and merged[-1] == 0:
            merged.pop()
        while merged and merged[0] == 0:
            merged.pop(0)

        return merged

    def _move(self, direction):

        if direction == 'up':
            for i in range(self.size):
                self.grid[i] = self._merge(self.grid[i][:])
        elif direction == 'right':
            self.grid = list(map(list, zip(*self.grid[::-1])))
            for i in range(self.size):
                self.grid[i] = self._merge(self.grid[i][:])
            self.grid = list(map(list, zip(*self.grid[::-1])))
        elif direction == 'down':
            for i in range(self.size):
                self.grid[i] = self._merge(self.grid[i][:])
        elif direction == 'left':
            self.grid = list(map(list, zip(*self.grid[::-1])))
            for i in range(self.size):
                self.grid[i] = self._merge(self.grid[i][:])
            self.grid = list(map(list, zip(*self.grid[::-1])))

        empty_cells = self._get_empty_cells()
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def render_grid(self):
        for row in self.grid:
            print(' '.join(str(n) for n in row))

    def _place_initial_numbers(self):
        # Randomly place either a 2 or 4 in the initial grid
        empty_cells = self._get_empty_cells()
        for _ in range(2):
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def __str__(self):
        display_grid=['. ','# ']
        lines =[]
        for row in self.grid:
            rows = ''.join([display_grid[x//2] if x else '  ' for x in row])
            lines.append(rows)
            if row == self.grid[-1]:
                lines.append('score: %d\n' % self.score)
        return '\n'.join(lines)

    def game_over(self):
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return False
        return True

def run():
    grid = Grid()
    grid._place_initial_numbers()
    while True:
        grid.render_grid()
        direction = input('Enter a direction (w,a,s,d): ')
        if direction == 'w':
            grid._move('up')
        elif direction == 'a':
            grid._move('left')
        elif direction == 's':
            grid._move('down')
        elif direction == 'd':
            grid._move('right')
        else:
            print('Invalid direction. Valid directions are w,a,s,d')

        if grid.game_over():
            grid.render_grid()
            print('Game over with score:', grid.score)
            input('Press Enter to play again: ')
            grid = Grid()
            grid._place_initial_numbers()

if __name__ == "__main__":
    run()

def _merge(self, row):
    merged = []
    prev = 0
    for num in row:
        if num == prev:
            merged[-1] *= 2
        else:
            merged.append(num)
        prev = num

    if len(row) != len(merged):
        self.score += 10 * sum([x for x in merged if abs(x) == 1 or abs(x) == 2])

    while len(merged)>1 and merged[-1] == merged[-2] and merged[-1] % 2 == 0:
        merged[-2] *= 2
        merged.pop()

    while len(merged) > 1 and merged[0] == merged[1] and merged[0] % 2 == 0:
        merged[0] *= 2
        del merged[1]

    while merged and merged[-1] == 0:
        merged.pop()
    while merged and merged[0] == 0:
        merged.pop(0)

    return merged
