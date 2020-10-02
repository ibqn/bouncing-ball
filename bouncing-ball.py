from pystdlib import stddraw

# Draw a bouncing ball to standard draw.

RADIUS = .05
DT = 20.0

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

rx = .480
ry = .860
vx = .015
vy = .023

stddraw.clear(stddraw.WHITE)

while True:
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledCircle(rx, ry, RADIUS)

    stddraw.setPenColor(stddraw.BLACK)
    stddraw.circle(rx, ry, RADIUS)

    # Update ball position and draw it there.
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
    rx = rx + vx
    ry = ry + vy

    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)
