from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import sin, cos, radians

width, height = 800, 600
shapes = []
current_shape = None
mode = 'point'
color = [1.0, 0.0, 0.0]
line_thickness = 2

transform = {'tx': 0, 'ty': 0, 'angle': 0, 'scale': 1}

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, width, height, 0)

def mouse_click(button, state, x, y):
    global current_shape
    if state == GLUT_DOWN:
        if mode == 'point':
            shapes.append(['point', x, y, color[:]])
        elif mode in ['line', 'rect', 'ellipse']:
            current_shape = [mode, x, y, x, y, color[:]]
            shapes.append(current_shape)
    elif state == GLUT_UP and current_shape:
        current_shape[3] = x
        current_shape[4] = y
        current_shape = None
    glutPostRedisplay()

def motion(x, y):
    if current_shape:
        current_shape[3] = x
        current_shape[4] = y
        glutPostRedisplay()

def keyboard(key, x, y):
    global mode, color, line_thickness
    if key == b'p':
        mode = 'point'
    elif key == b'l':
        mode = 'line'
    elif key == b'r':
        mode = 'rect'
    elif key == b'o':
        mode = 'ellipse'
    elif key == b'1':
        color = [1.0, 0.0, 0.0]
    elif key == b'2':
        color = [0.0, 1.0, 0.0]
    elif key == b'3':
        color = [0.0, 0.0, 1.0]
    elif key == b'+':
        line_thickness += 1
    elif key == b'-':
        line_thickness = max(1, line_thickness - 1)
    elif key == b'c':
        shapes.clear()
    elif key == b'\x1b':  # ESC
        glutLeaveMainLoop()
    # Transformasi
    elif key == b'w':
        transform['ty'] -= 10
    elif key == b's':
        transform['ty'] += 10
    elif key == b'a':
        transform['tx'] -= 10
    elif key == b'd':
        transform['tx'] += 10
    elif key == b'q':
        transform['angle'] += 5
    elif key == b'e':
        transform['angle'] -= 5
    elif key == b'z':
        transform['scale'] *= 0.9
    elif key == b'x':
        transform['scale'] *= 1.1

    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(line_thickness)
    glPushMatrix()
    glTranslatef(transform['tx'], transform['ty'], 0)
    glScalef(transform['scale'], transform['scale'], 1)
    glTranslatef(width//2, height//2, 0)
    glRotatef(transform['angle'], 0, 0, 1)
    glTranslatef(-width//2, -height//2, 0)
    for shape in shapes:
        draw_shape(shape)
    glPopMatrix()
    glFlush()

def draw_shape(shape):
    mode = shape[0]
    if mode == 'point':
        glColor3fv(shape[3])
        glBegin(GL_POINTS)
        glVertex2f(shape[1], shape[2])
        glEnd()
    elif mode == 'line':
        glColor3fv(shape[5])
        glBegin(GL_LINES)
        glVertex2f(shape[1], shape[2])
        glVertex2f(shape[3], shape[4])
        glEnd()
    elif mode == 'rect':
        glColor3fv(shape[5])
        glBegin(GL_LINE_LOOP)
        glVertex2f(shape[1], shape[2])
        glVertex2f(shape[1], shape[4])
        glVertex2f(shape[3], shape[4])
        glVertex2f(shape[3], shape[2])
        glEnd()
    elif mode == 'ellipse':
        glColor3fv(shape[5])
        cx = (shape[1] + shape[3]) / 2
        cy = (shape[2] + shape[4]) / 2
        rx = abs(shape[3] - shape[1]) / 2
        ry = abs(shape[4] - shape[2]) / 2
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            theta = radians(i)
            x = cx + rx * cos(theta)
            y = cy + ry * sin(theta)
            glVertex2f(x, y)
        glEnd()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL 2D Drawing - Clean Version")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    glutMotionFunc(motion)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()