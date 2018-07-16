radius = 8
grid = [[' 'for j in range(4*radius+1)] for i in range(2*radius+1)]
# the circle center is at grid[radius][radius]
def draw(x):

    h = ((radius**2 - (radius - x/2)**2)**0.5)
    h = int(h+0.4)
    for i in range(h):
        grid[radius - i][x] = 'x'
        grid[radius + i][x] = 'x'

for i in range(4*radius+1):
    draw(i)
print('\n'.join([''.join(r) for r in grid]))
