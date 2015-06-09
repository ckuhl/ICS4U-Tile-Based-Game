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
The background map is an array of numbers corresponding to the position of a sprite in the sprite sheet. The sprites
are encoded sequentially, left-to-right and top-to-bottom, 00 to 99.

### Boundary Map
The boundary map is list of rectangles defining the areas which can be walked on (floors and doors). Each area has a two
character code defining it. The first is the level (1 - 9) and the second defines the type of bound: 0 is ground, D is
door and A is stairs (ascending), B is stairs (descending).

### Entity list
The entity list is a list of entity IDs and their positions. These IDs are used to determine which kind of entity to
create.

## The `tools` module
### The `SpriteSheet` Class
This class allows the import and subdivision of sprite sheets into individual sprites. `get_image` and `get_sheet` are
the two main methods to use.

### The `BoundMap` Class
This class creates a list of all the boundaries in a level (ie. the surfaces you can walk on) and allows you to check if
a given rectangle is contained by any of these boundaries. Because a rectangle can lie partially on two different
rectangles and still be completely within the BoundMap, this is done by checking if each corner of the rectangle lies
within the boundaries.

### The `Screen` Class
This class creates a pygame.Surface object of a given size. The method `Screen.background` draws a background to the
surface given a sprite sheet and map of the background.

### The `Entity` Class
This class defines a list of entities, and the individual entities that interact with the boundmap. The method
`Entity.update` allows the entity to be updated to the next sprite (if animated) and update the direction of the entity
(North, East, South, West).

## Art sources
background1.png by Buch on OpenGameArt, public domain

player.png by Skylar1146 on OpenGameArt, public domain

icon.png by k-u-h-l
