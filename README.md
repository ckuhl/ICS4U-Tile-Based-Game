# ICS4U-Tile-Based-Game

My (work in progress) final project for ICS4U, a tile based game.

## What is it?
A tile-based game, made to demonstrate the various skills learned in ICS4U:

 * classes
 * modular programming
 * file access and modification
 * algorithm design
 * modification and use images
 * reading from text files
 * loading data from text files
 * creating a primitive AI

## Documentation
### Background Map
The background map is an array of hex numbers corresponding to the position of a sprite in the sprite sheet. The sprites
are encoded sequentially, left-to-right and top-to-bottom.

### Boundary Map
The boundary map is an array of two digit decimal numbers. The first corresponds to the height of the piece, with the
second corresponding to the nature of the tile: 0 is a wall, 1 walkable tile, and 2 a door.
