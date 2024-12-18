import math
import time
import sys

def render_donut():
    A = 0 
    B = 0 

    while True:
        z = [0] * 1760  
        b = [' '] * 1760

        for j in range(0, 628, 7): 
            for i in range(0, 628, 2):
                c = math.sin(i / 100)
                d = math.cos(j / 100)
                e = math.sin(A)
                f = math.sin(j / 100)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i / 100)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e

                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))

                o = int(x + 80 * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o] = D
                    b[o] = ".-~:;=!*#$@"[max(0, min(N, len(".-~:;=!*#$@") - 1))]

        # Print the frame in one go
        sys.stdout.write("\x1b[H" + ''.join(b[k] + ('\n' if k % 80 == 79 else '') for k in range(1760)))
        sys.stdout.flush()

        A += 0.04  
        B += 0.02  
        time.sleep(0.03)

if __name__ == "__main__":
    try:
        render_donut()
    except KeyboardInterrupt:
        sys.stdout.write("\x1b[2J\x1b[H")
        sys.stdout.flush()
        print("Exited gracefully.")
