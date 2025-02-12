# Pygame Sheetcut

Pygame Sheetcut is a Python package that simplifies the process of cutting sprite sheets for use in Pygame projects.

## Features

- Easy to use API for cutting sprite sheets
- All you need is Surfaces
- Allows for cutting by tile size or by rows and columns

## Installation

You can install Pygame Sheetcut using pip:

```bash
pip install pygame_sheetcut
```

## Usage

Here is a basic example of how to use Pygame Sheetcut:

```python
import pygame
from pygame_sheetcut import cut_grid, cut_size

# Initialize Pygame
pygame.init()

# Load your sprite sheet
sprite_sheet = pygame.image.load('path/to/your/sprite_sheet.png').convert_alpha()

# get frames
frames = cut_size(sprite_sheet, tile_width=32, tile_height=32)

# get a frame
sprite = frames[0]

# Display a sprite in a Pygame window
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

## Contributing

<!-- Contributions are welcome! Please fork the repository and submit a pull request. -->
Most likely won't edit this project much, so contributions probably wont be needed... you could ask, though!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue on GitHub.
