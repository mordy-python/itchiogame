import pygame
import sys, random, os
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 500
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill((100, 175, 75))
pygame.display.flip()

cards_path = os.path.join(os.path.dirname(__file__), "cards")

deck = list()
for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
	for rank in range(1, 14):
		deck.append({"rank": rank, "suit": suit})
card1 = random.choice(deck)
cardback = pygame.image.load(os.path.join(cards_path, f"cardback.png"))
screen.blit(cardback, (10, 10))
screen.blit(cardback, (30, 10))
pygame.display.flip()

drawn_cards = []


def dealer_setup():
	hidden = random.choice(deck)
	faceup = random.choice(deck)
	while hidden in drawn_cards:
		hidden = random.choice(deck)
	while faceup in drawn_cards:
		faceup = random.choice(deck)
	drawn_cards.append(hidden)
	drawn_cards.append(faceup)
	rank = get_rank(faceup)
	screen.blit(pygame.image.load(os.path.join(cards_path, "cardBack.png")), (400, 10))
	screen.blit(
		pygame.image.load(os.path.join(cards_path, f'card{faceup["suit"]}{rank}.png')),
		(550, 10),
	)
	return hidden


def get_rank(card):
	
	if card["rank"] == 11:
		rank = "J"
		return rank
	if card["rank"] == 12:
		rank = "Q"
		return rank
	if card["rank"] == 13:
		rank = "K"
		return rank
	if card["rank"] == 1:
		rank = "A"
		return rank
	rank = card['rank']
	return rank


hidden = dealer_setup()
h_key = K_h
score = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()
			if event.key == K_l:
				screen.fill((0, 0, 0))
				pygame.display.flip()
			if event.key == h_key:
				card = random.choice(deck)
				try:
					score += int(get_rank(card))
				except ValueError:
					rank = get_rank(card)
					if rank == 'J': score += 11
					if rank == 'Q': score += 12
					if rank == 'K': score += 13 
				score_text = pygame.font.SysFont("Helvetica", 100)
				screen_score = score_text.render(str(score), True, (0, 255, 255)), (10,200)
				screen.__delattr__(screen_score[0])
				screen.blit(screen_score)
				pygame
				while card in drawn_cards:
					card = random.choice(deck)
				drawn_cards.append(card)
				rank = get_rank(card)
				print(rank)
				print(os.path.join(cards_path, f"card{card['suit']}{rank}.png"))
				screen_card = pygame.image.load(
					os.path.join(cards_path, f"card{card['suit']}{rank}.png")
				)
				screen.blit(screen_card, (300, 300))
			if event.key == K_s:
				h_key = None
				rank = get_rank(hidden)
				screen.blit(
					pygame.image.load(
						os.path.join(cards_path, f'card{hidden["suit"]}{rank}.png')
					),
					(400, 10),
				)
	pygame.display.flip()
	clock.tick(FPS)
