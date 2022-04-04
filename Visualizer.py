import pygame


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))  # set window size
pygame.display.set_caption("A* Path Finding Algorithm")

RED: tuple = (255, 0, 0)
GREEN: tuple = (0, 255, 0)
BLUE: tuple = (0, 255, 0)
YELLOW: tuple = (255, 255, 0)
WHITE: tuple = (255, 255, 255)
BLACK: tuple = (0, 0, 0)
PURPLE: tuple = (128, 0, 128)
ORANGE: tuple = (255, 165, 0)
GREY: tuple = (128, 128, 128)
TURQUOISE: tuple = (64, 224, 208)


class Spot:
    def __init__(self, row: int, col: int, width: int, total_rows: int):  # width refers to the width of the cube
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self) -> tuple:
        return self.row, self.col

    def is_closed(self) -> bool:
        return self.color == RED

    def is_open(self) -> bool:
        return self.color == GREEN

    def is_barrier(self) -> bool:
        return self.color == BLACK

    def is_start(self) -> bool:
        return self.color == ORANGE

    def is_end(self) -> bool:
        return self.color == TURQUOISE

    def reset(self) -> None:
        self.color = WHITE

    def make_open(self) -> None:
        self.color = GREEN

    def make_closed(self) -> None:
        self.color = RED

    def make_start(self) -> None:
        self.color = ORANGE

    def make_barrier(self) -> None:
        self.color = BLACK

    def make_end(self) -> None:
        self.color = TURQUOISE

    def make_path(self) -> None:
        self.color = PURPLE

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid: list) -> None:
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # down
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # up
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # right
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


def make_grid(rows: int, width: int) -> list:
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win: pygame.Surface, rows: int, width: int) -> None:
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win: pygame.Surface, grid: list, rows: int, width: int) -> None:
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos: tuple, rows: int, width: int) -> tuple:
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col
