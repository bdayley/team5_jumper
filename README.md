# Jumper

Jumper is variation on the classic Hangman game. A player guesses letters to
find a word. Each wrong guess removes a line from the jumper figure. Each right
guess displays the letter in the correct position in the word. The game is over
when the puzzle is solved or the jumper no longer has a parachute.

## Rules

The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over.
If the player has no more parachute the game is over.

## Project Structure

Director\
 Methods:\
 start_game()\
 get_input()\
 do_updates()\
 do_outputs()\
Player\
 Methods:\
 guess_letter()
draw()
is_alive()
Puzzle\
 Methods:\
 check_guess()
show_word()
is_solved()
TerminalService\
 read_text()
write_text()

## Authors

Carina Aguero (agu21022@byui.edu)\
Rob Cox (cox21008@byui.edu)\
Brianna Dayley (col04002@byui.edu)\
Anamilena Casariego (cas21052@byui.edu)\
Eduardo Pulido (pul21010@byui.edu)
