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
The various components of this game are all documented within their code, in the *tools* module.

The resources file contains all the resources that the game requires. At this time they are:

 * the spritesheet
 * the background map
    * which contains hex numbers corresponding to a sprite in the sprite sheet, numbered left-to-right and top-to-bottom
 * and the boundary map
    * which contains decimal numbers, the first of which defines the level of a tile, and the second its characteristics
