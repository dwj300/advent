#!/usr/bin/env python3

def solve(xmin, xmax, ymin, ymax):
    p2 = 0
    ans = -1 * float('inf')
    for vvx in range(250):
        for vvy in range(-250, 250):
            vx, vy = vvx, vvy
            x, y = 0, 0
            l = -1 * float('inf')
            success = False
            for _ in range(1000):
                x += vx
                y += vy
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                vy -= 1
                l = max(l, y)
                if xmin <= x <= xmax and ymin <= y <= ymax:
                    success = True
            if success:
                p2 += 1
                ans = max(ans, l)
            
    return ans, p2

if __name__ == "__main__":
    print(solve(217,240, -126, -69))
