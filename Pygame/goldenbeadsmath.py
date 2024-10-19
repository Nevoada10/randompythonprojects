"""
Função de inicialização:
    Inicializar a interface gráfica
    Carregar as imagens das peças do material dourado (units, tens, hundreds, etc.)
    Posicionar as peças na interface

Função de arrastar e soltar:
    Ao clicar e segurar em uma peça:
        Registrar a posição inicial do mouse e da peça
    Enquanto a peça estiver sendo arrastada:
        Atualizar a posição da peça para seguir o movimento do mouse
    Ao soltar a peça:
        Verificar a posição final da peça
        Se a posição final estiver sobre uma área designada para formar números:
            Verificar se a peça pode ser colocada naquela posição (ex: se já há uma peça lá)
            Se sim, posicionar a peça naquela área
            Se não, retornar a peça à sua posição original

Função de verificação de números formados:
    Ao posicionar uma peça:
        Verificar se as peças formam um número válido
        Se sim, destacar o número e permitir que seu irmãozinho o utilize para realizar operações matemáticas
        Se não, manter as peças soltas para que ele possa tentar novamente

Função de operações matemáticas: Permitir que seu irmãozinho use os números formados para realizar operações como
adição, subtração, multiplicação, etc.


"""
import pygame
import sys


#######################################################################################################################
# Nevoada
#######################################################################################################################


def main():  # Main function

    # INITIAL STATE:

    # Initialize the window with small proportions
    pygame.init()
    screen = pygame.display.set_mode((16*100,9*100))

    # Load the images of the Golden Beads
    unit = pygame.image.load("unit.png")
    ten = pygame.image.load("ten.png")
    hundred = pygame.image.load("hundred.png")
    thousand = pygame.image.load("thousand.png")

    # Position the images in the lower part of the screen depending on the screen size
    unit_rect = unit.get_rect(center=(16*100,8*100))
    ten_rect = ten.get_rect(center=(5*100,8*100))
    hundred_rect = hundred.get_rect(center=(6*100,8*100))
    thousand_rect = thousand.get_rect(center=(7*100,8*100))

    # Draw the images
    screen.blit(unit, unit_rect)
    screen.blit(ten, ten_rect)
    screen.blit(hundred, hundred_rect)
    screen.blit(thousand, thousand_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add code to draw the images and handle user interactions here

        pygame.display.flip()

    pygame.quit()
    print("Successfully executed")
    sys.exit()


# Functions:


if __name__ == "__main__":  # Check if it's main otherwise it won't run
    exit_code = main()
    sys.exit(exit_code)
