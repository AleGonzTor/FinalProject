import pygame

def mostrar_ventana_ganaste(screen):
    WIDTH, HEIGHT = screen.get_size()
    font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font(None, 48)

    exit_surface = button_font.render("Salir del Juego", True, (255, 255, 255))
    exit_rect = exit_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))

    ventana_abierta = True
    while ventana_abierta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if exit_rect.collidepoint(mx, my):
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0))


        text_surface = font.render("¡Nivel completado!", True, (255, 255, 0))
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        screen.blit(text_surface, text_rect)

        screen.blit(exit_surface, exit_rect)

        pygame.display.update()