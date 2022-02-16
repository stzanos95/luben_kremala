import ranwords
import random

ranword = ranwords.random_words[random.randint(0, len(ranwords.random_words)-1)]
game_word = list("_" for i in range(0, len(ranword)))
tries = 8
letters_tried = []
	
def checkGuess(guess):
	prev_guess = "".join(game_word)
	letters_tried.append(guess)
	global tries
	
	for i, letter in enumerate(ranword):
		if letter == guess:
			game_word[i] = guess
	if prev_guess == "".join(game_word):
		tries -= 1
		print("{} To {} den uparxei.".format(ranwords.fail_words[random.randint(0, len(ranwords.fail_words)-1)], guess))
	else:
		print("{} Swsto to {}!".format(ranwords.win_words[random.randint(0, len(ranwords.win_words)-1)], guess))
	print(" ".join(game_word))
	print("Mexri twra exeis dokimasei: {}".format(", ".join(letters_tried)))
	if tries == 0:
		print("Exases, alla de me poluendiaferei kai vasika kiolas.")
		return False
	else:
		if "".join(game_word).find("_") == -1:
			print("CONGRATULATIONS! Eisai h megaluteri poutana twn Athinwn!")
			return False
		else:
			print("Exeis {} prospatheies akoma, ksekina na agxwnesai.".format(tries))
			return True
			

def play():	
	
	print("--> KREMALA <--")
	print("Rules: ")
	print("- Egglezika grammata")
	print("- Aples kathimerines ksenes lekseis")
	print("- Exeis {} prospatheies.".format(tries))
	print("\'Desmeuomai na sevastw, to opoio apotelesma autis tis dimokratikis diadikasias.\' - A. Tsipras")
	print("\'Ellada eisai etoimi?\' - S. Kontizas")
	still_playing = True
	while still_playing:
		guess_let = str(input("Gia madepse kana gramma: \n"))
		if guess_let.isalpha():
			still_playing = checkGuess(guess_let)
			print("===================================")
		else:
			print("Re gramma de sou eipa? Twra ftaiw egw na pw, pou ta vrikate auta ta fidania?")
			print("===================================")
			continue
	
if __name__ == "__main__":
	play()
