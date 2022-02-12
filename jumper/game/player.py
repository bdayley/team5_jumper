from game.terminal_service import TerminalService

class Player:
    """
    The person guessing the word/puzzle.
    
    The responsibility of Player is to:
        guess a letter
        draw itself 
        keep track of if it's alive

    Attributes:
        _parachute (List): for drawing, and keeping track if alive

    Methods:
        _guess_letter():
            return to director
        _draw(puzzle_TF):
        _is_alive():
            return to director
    """

    def __init__(self):
        """
        Constructs a new Player

        Args:
            self (Player): An instance of Player
        """
        self._terminal_service = TerminalService()
        self._parachute = [
            "  ___",
            " /___\\",
            " \   /",
            "  \ /",
            "   0",
            "  /|\\",
            "  / \\",
            "",
            "^^^^^^^"
            ]
    
    def draw(self, puzzle_TF): 
        """
        Calls terminal service to draw, passes self._parachute

        Args:
            self (Player): An instance of Player
            puzzle_TF: True or False from puzzle
        """
        # if the letter guess is false, and the player is alive, 
        # remove the first item of the parachute list
        if puzzle_TF == False and len(self._parachute) > 5:
            self._parachute.pop(0)
        
        # if the letter guess is false, and it's the last guess,
        # replace the '0' with 'x'
        if puzzle_TF == False and len(self._parachute) == 5:
            self._parachute[0] = '   x'

        # after checks, send to terminal services to print
        for line in self._parachute:
            self._terminal_service.write_text(line)

    def guess_letter(self):
        letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        return letter

    def is_alive(self):
        return len(self._parachute) > 5
