# Mars Rover OOP Interview Exercise
#
# Problem Statement:
# You are tasked with designing a system to control a Mars Rover. The rover is located on a grid, and it can move around based on commands.
# The grid is represented as a 2D plane, and the rover has a position (x, y) and a direction it is facing (N, E, S, W).
#
# The rover can receive the following commands:
# - 'L': Turn left (90 degrees counterclockwise)
# - 'R': Turn right (90 degrees clockwise)
# - 'M': Move forward one grid square in the direction it is currently facing
#
# The interviewer may ask the following:
# 1. Implement the MarsRover class with methods to handle the commands.
# 2. Ensure the rover does not move outside the grid boundaries.
# 3. Add error handling for invalid commands.
# 4. Write a method to return the rover's current position and direction.
# 5. Extend the functionality to handle multiple rovers on the same grid.

class MarsRover:
    """
    A class to represent a Mars Rover on a 2D grid.
    """
    def __init__(self, x: int, y: int, direction: str, grid_size: tuple):
        """
        Initialize the rover with its starting position, direction, and grid size.
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_size = grid_size
        self.directions = ['N', 'E', 'S', 'W']

    def turn_left(self):
        """
        Turn the rover 90 degrees counterclockwise.
        """
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index - 1) % 4]

    def turn_right(self):
        """
        Turn the rover 90 degrees clockwise.
        """
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index + 1) % 4]

    def move(self):
        """
        Move the rover forward one grid square in the direction it is facing.
        """
        if self.direction == 'N' and self.y < self.grid_size[1] - 1:
            self.y += 1
        elif self.direction == 'E' and self.x < self.grid_size[0] - 1:
            self.x += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1
        else:
            raise ValueError("Rover cannot move outside the grid boundaries.")

    def execute_commands(self, commands: str):
        """
        Execute a series of commands to control the rover.
        """
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move()
            else:
                raise ValueError(f"Invalid command: {command}")

    def get_position(self):
        """
        Return the current position and direction of the rover.
        """
        return self.x, self.y, self.direction

# Example usage for pair programming:
if __name__ == "__main__":
    # Initialize the Mars Rover
    rover = MarsRover(0, 0, 'N', (5, 5))

    # Example commands
    commands = "MMRMMRMRRM"
    rover.execute_commands(commands)

    # Print the final position and direction
    print("Final Position and Direction:", rover.get_position())