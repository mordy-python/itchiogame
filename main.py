import os
import random
import sys
from tkinter import messagebox
import tkinter

import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 500
FPS = 60
CARDPOS_X, CARDPOS_Y = 50, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")
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
player_cards = []
dealer_cards = []

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
	return hidden, faceup

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
def rank_from_card(card):
	rank = get_rank(card)
	if rank in ('J', "Q", "K"):
		return 10
	elif rank == 'A':
		if sum(player_cards) < 10:
			return 11
		else:
			return 1
	else:
		return card['rank']
def player_setup(player_card_list:list, cposx):
	card1 = random.choice(deck)
	card2 = random.choice(deck)
	while card1 in drawn_cards:
		card1 = random.choice(deck)
	while card2 in drawn_cards:
		card2 = random.choice(deck)
	drawn_cards.append(card1)
	drawn_cards.append(card2)
	rank1 = get_rank(card1)
	rank2 = get_rank(card2)
	cposx += 100
	screen.blit(
		pygame.image.load(os.path.join(cards_path, f'card{card1["suit"]}{rank1}.png')),
		(cposx, CARDPOS_Y),
	)
	screen.blit(
		pygame.image.load(os.path.join(cards_path, f'card{card1["suit"]}{rank2}.png')),
		(CARDPOS_X, CARDPOS_Y),
	)
	player_card_list.append(rank1)
	player_card_list.append(rank2)
	return card1,card2
hidden, faceup = dealer_setup()
c1, c2 = player_setup(player_cards, CARDPOS_X)
h_key = K_h
score = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q or event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_l:
				import help
			if event.key == h_key:
				card = random.choice(deck)
				while card in drawn_cards:
					card = random.choice(deck)
				try:
					rank = int(get_rank(card))
				except ValueError:
					rank = rank_from_card(card)
				player_cards.append(rank)
				score = sum(player_cards)
				score_text = pygame.font.SysFont("Helvetica", 100)
				screen_score = score_text.render(str(score), True, (0, 255, 255), (100, 175, 75))
				screen.blit(screen_score, (10,200))
				drawn_cards.append(card)
				rank = get_rank(card)
				screen_card = pygame.image.load(
					os.path.join(cards_path, f"card{card['suit']}{rank}.png")
				)
				CARDPOS_X += 150
				screen.blit(screen_card, (CARDPOS_X, CARDPOS_Y))
			if event.key == K_s:
				dealer_val = 0
				h_key = None
				hrank = get_rank(hidden)
				frank = get_rank(faceup)
				print(hrank, frank)
				screen.blit(
					pygame.image.load(
						os.path.join(cards_path, f'card{hidden["suit"]}{rank}.png')
					),
					(400, 10),
				)
	pygame.display.flip()
	clock.tick(FPS)
