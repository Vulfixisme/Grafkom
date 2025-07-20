from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sin, cos, radians 

angle_x = 0
angle_y = 0
last_x = 0
last_y = 0
is_dragging = False

pos_x = 0
pos_y = 0
pos_z = 0

def init_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    ambient = [0.2, 0.2, 0.2, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    diffuse = [0.7, 0.7, 0.7, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    specular = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)
    position = [2.0, 5.0, 5.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMateriali(GL_FRONT, GL_SHININESS, 50)

def draw_manual_cube():
    vertices = [
        [-1, -1, -1],
        [ 1, -1, -1],
        [ 1,  1, -1],
        [-1,  1, -1],
        [-1, -1,  1],
        [ 1, -1,  1],
        [ 1,  1,  1],
        [-1,  1,  1]
    ]

    faces = [
        [0, 1, 2, 3],  # back
        [4, 5, 6, 7],  # front
        [0, 4, 7, 3],  # left
        [1, 5, 6, 2],  # right
        [3, 2, 6, 7],  # top
        [0, 1, 5, 4]   # bottom
    ]

    normals = [ 
        [0, 0, -1],  # back
        [0, 0, 1],   # front
        [-1, 0, 0],  # left
        [1, 0, 0],   # right
        [0, 1, 0],   # top
        [0, -1, 0]   # bottom
    ]

    glBegin(GL_QUADS)
    for i in range(len(faces)):
        glNormal3fv(normals[i])   
        for vertex in faces[i]:
            glVertex3fv(vertices[vertex])
    glEnd()



def draw_cube():
    glutSolidCube(2)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 5, 10, 0, 0, 0, 0, 1, 0)
    glTranslatef(pos_x, pos_y, pos_z)
    glRotatef(angle_x, 1.0
    

    
    draw_manual_cube()
    glutSwapBuffers()

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def mouse(button, state, x, y):
    global is_dragging, last_x, last_y
    if button == GLUT_LEFT_BUTTON:
        is_dragging = (state == GLUT_DOWN)
        last_x = x
        last_y = y

def motion(x, y):
    global angle_x, angle_y, last_x, last_y
    if is_dragging:
        angle_y += (x - last_x)
        angle_x += (y - last_y)
        last_x = x
        last_y = y
        glutPostRedisplay()

def keyboard(key, x, y):
    global pos_x, pos_y, pos_z, angle_x, angle_y
    step = 0.2
    rot_step = 5
    if key == b'w':
        pos_y += step
    elif key == b's':
        pos_y -= step
    elif key == b'a':
        pos_x -= step
    elif key == b'd':
        pos_x += step
    elif key == b'q':
        pos_z += step
    elif key == b'e':
        pos_z -= step
    elif key == b'i':
        angle_x += rot_step
    elif key == b'k':
        angle_x -= rot_step
    elif key == b'j':
        angle_y -= rot_step
    elif key == b'l':
        angle_y += rot_step
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Cube with Lighting, Camera, and Keyboard Control")
    glEnable(GL_DEPTH_TEST)
    init_lighting()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()

    