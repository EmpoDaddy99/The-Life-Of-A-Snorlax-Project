import pygame
import ctypes
from PIL import Image

pygame.init()
user32 = ctypes.windll.user32

screen = pygame.display.set_mode((user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)), pygame.FULLSCREEN)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption('The Life of a Snorlax')

# icon
icon = pygame.image.load('pokemon.png')
pygame.display.set_icon(icon)
# snorlax
snorlax = pygame.image.load('snorlax_full_sprite.png')
images0 = [pygame.image.load('snorlax0.png'), pygame.image.load('snorlax1.png'), pygame.image.load('snorlax2.png'),
		   pygame.image.load('snorlax1.png')]
images1 = [pygame.image.load('snorlax3.png'), pygame.image.load('snorlax4.png'), pygame.image.load('snorlax5.png'),
		   pygame.image.load('snorlax4.png')]
images2 = [pygame.image.load('snorlax6.png'), pygame.image.load('snorlax7.png'), pygame.image.load('snorlax8.png'),
		   pygame.image.load('snorlax7.png')]
images3 = [pygame.image.load('snorlax9.png'), pygame.image.load('snorlax10.png'), pygame.image.load('snorlax11.png'),
		   pygame.image.load('snorlax10.png')]

running = True
dir = 'down'
counter = 0
loc_X = 64 * 3
loc_Y = 822 * 3 - 48 * 9
isUp = False
isUpRest = False
isDown = False
isDownRest = False
isLeft = False
isLeftRest = False
isRight = False
isRightRest = False

def redraw():
	global counter
	global loc_X
	global loc_Y
	screen.blit(pygame.transform.scale(pygame.image.load('Amity_Square_DP.png'), (1023 * 4, 822 * 4)),
				(32 - loc_X, 32 - loc_Y))
	if isDown:
		screen.blit(images0[counter // 3], (w / 2 - 42, h / 2 - 51))
		counter = counter % 11 + 1
		if loc_Y < 822 * 3:
			loc_Y += 48
	if isLeft:
		screen.blit(images1[counter // 3], (w / 2 - 42, h / 2 - 51))
		counter = counter % 11 + 1
		if loc_X > 0:
			loc_X -= 64
	if isRight:
		screen.blit(images2[counter // 3], (w / 2 - 42, h / 2 - 51))
		counter = counter % 11 + 1
		if loc_X < 1023 * 3 - 256:
			loc_X += 64
	if isUp:
		screen.blit(images3[counter // 3], (w / 2 - 42, h / 2 - 51))
		counter = counter % 11 + 1
		if loc_Y > 0:
			loc_Y -= 48
	if isDownRest:
		screen.blit(pygame.image.load('snorlax1.png'), (w / 2 - 42, h / 2 - 51))
	if isLeftRest:
		screen.blit(pygame.image.load('snorlax4.png'), (w / 2 - 42, h / 2 - 51))
	if isRightRest:
		screen.blit(pygame.image.load('snorlax7.png'), (w / 2 - 42, h / 2 - 51))
	if isUpRest:
		screen.blit(pygame.image.load('snorlax10.png'), (w / 2 - 42, h / 2 - 51))
	# if isStart:
	if isUp == False and isUpRest == False and isDown == False and isDownRest == False and isLeft == False and isLeftRest == False and isRight == False and isRightRest == False:
		screen.blit(pygame.image.load('snorlax10.png'), (w / 2 - 42, h / 2 - 51))
	pygame.display.update()

while running:
	pygame.time.delay(50)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			if event.key == pygame.K_DOWN:
				isUp = False
				isUpRest = False
				isDown = True
				isDownRest = False
				isLeft = False
				isLeftRest = False
				isRight = False
				isRightRest = False
			if event.key == pygame.K_UP:
				isUp = True
				isUpRest = False
				isDown = False
				isDownRest = False
				isLeft = False
				isLeftRest = False
				isRight = False
				isRightRest = False
			if event.key == pygame.K_LEFT:
				isUp = False
				isUpRest = False
				isDown = False
				isDownRest = False
				isLeft = True
				isLeftRest = False
				isRight = False
				isRightRest = False
			if event.key == pygame.K_RIGHT:
				isUp = False
				isUpRest = False
				isDown = False
				isDownRest = False
				isLeft = False
				isLeftRest = False
				isRight = True
				isRightRest = False
		elif event.type == pygame.KEYUP:
			if isDown:
				isDown = False
				isDownRest = True
			if isLeft:
				isLeft = False
				isLeftRest = True
			if isRight:
				isRight = False
				isRightRest = True
			if isUp:
				isUp = False
				isUpRest = True
	redraw()
