import pygame
import numpy as np
import sys
from math import sin, cos, radians

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rotación de un Cubo en 3D')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define los vértices de un cubo
vertices = [
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1]
]

# Define las aristas del cubo
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

# Función para proyectar 3D a 2D
def project(x, y, z):
    scale = 200 / (z + 5)
    x_proj = x * scale + width // 2
    y_proj = -y * scale + height // 2
    return (x_proj, y_proj)

# Función para rotar el cubo
def rotate(vertices, angle):
    rotation_matrix_y = [
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ]
    return [np.dot(rotation_matrix_y, v) for v in vertices]

# Bucle principal
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    
    # Rotar los vértices del cubo
    rotated_vertices = rotate(vertices, radians(angle))
    
    # Dibujar las aristas del cubo
    for edge in edges:
        points = []
        for vertex in edge:
            points.append(project(*rotated_vertices[vertex]))
        pygame.draw.line(screen, WHITE, points[0], points[1], 1)
    
    pygame.display.flip()
    clock.tick(60)
    angle += 1
