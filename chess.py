class ChessBoard:
    def __init__(self):
        self.board = [
            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
            ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
            [".", " .", " .", " .", " .", " .", ".", " ."],
            [".", " .", " .", " .", " .", " .", ".", " ."],
            [".", " .", " .", " .", " .", " .", ".", " ."],
            [".", " .", " .", " .", " .", " .", ".", " ."],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
        ]
        self.turn = "white"

    def print_board(self):

        print("  a  b  c  d  e  f g  h")
        for i, row in enumerate(self.board):

            rank = 8 - i
            print(rank, " ".join(row), rank)
        print("  a  b  c  d  e f  g  h\n")

    def move_piece(self, start, end):

        try:
            start_row = 8 - int(start[1])
            start_col = ord(start[0].lower()) - ord('a')
            end_row = 8 - int(end[1])
            end_col = ord(end[0].lower()) - ord('a')
        except (IndexError, ValueError):
            print("Invalid input format.")
            return False

        piece = self.board[start_row][start_col]
        if piece == ".":
            print("No piece at the starting square!")
            return False


        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = "."
        self.turn = "black" if self.turn == "white" else "white"
        return True


def main():
    game = ChessBoard()
    game.print_board()

    while True:
        prompt = f"{game.turn.capitalize()}'s move (e.g., e2 e4) or type 'quit': "
        user_input = input(prompt).strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Game terminated.")
            break

        try:
            start, end = user_input.split()
        except ValueError:
            print("Please enter two positions separated by a space (e.g., 'e2 e4').")
            continue

        if game.move_piece(start, end):
            game.print_board()
        else:
            print("Move not executed. Try again.")


if __name__ == "__main__":
    main()