# ICS4U-Tile-Based-Game

My (work in progress) final project for ICS4U, a tile based game.

## What is it?
A tile-based game, made to demonstrate the various skills learned in ICS4U:

 * classes
 * modular programming
 * file access and modification
 * algorithm design
 * modification and use of images
 * reading and loading data from text files

## Documentation
### The Level Format
#### Background Map
The background map is an array of integers representing the background. The position of each number corresponds to its
position in the game, and its value corresponds to the position of the sprite in the sprite sheet. The sprites are
encoded sequentially, left-to-right and top-to-bottom, 00 to 99.

The horizontal and vertical index of a sprite in an array can be found using floor division of its value to find the
y-index, with the remainder being equal to the x-index of the number

#### Boundary Map
The boundary map is list of rectangles defining the areas that can be walked on. Each line in the file contains an ID
for the bound, and 4 integers -- the top left and bottom right corner of the bound.

The ID is a two character string. The first character represents the height of the given bound (1 - 9). The second
character defines the type of boundary: 0 is ground, D is a door, A is ascending staircase, and B is a descending
staircase.

Note: in order for staircases to work, an ascending and descending staircase must have the same bounds, at their
respective heights.

#### Entity list
The entity list is a list of entity IDs their positions, and an optional argument. These IDs are used to determine which
entities to create. For doors, the optional argument denotes which level they warp the player to.

### The `tools` module
#### The `BoundMap` Class
The BoundMap class creates a list of all the boundaries in a level (ie. the surfaces you can walk on) and allows you to check if
a given rectangle is contained by any of these boundaries. Because a rectangle can lie partially on two different
rectangles and still be completely within the BoundMap, this is done by checking if each corner of the rectangle lies
within the boundaries.

#### The `Entities` Class
The Entities Class acts as a container for all of the entities in a level. This allows for checking if any of the
entities in a level collides with the player.

#### The `Entity` Class
The Entity class defines a list of entities, and the individual entities that interact with the boundmap. The method
`Entity.update` allows the entity to be updated to the next sprite (if animated) and update the direction of the entity
(North, East, South, West).

##### The `Player` Sub-class
The Player sub-class pre-loads the player sprite, and adds the variables `Player.money` (range: 0 - 9999) and `Player.health`
(range: 0 - 16).

##### The `Door` Sub-class
The Door sub-class is initialized with a smaller hit box (to allow the player to walk "into" the door before warping).

#### The `HUDOverlay` Class
The HUDOverlay pre-creates the base of the heads up display. The functions `HUDOverlay.update_money` and
`HUDOverlay.update_health` create a surface containing the appropriate representation of each.

#### The `Level` Class
The Level class initializes the boundmap, entities, and background of a level, inputted the name of the level.

#### The `Screen` Class
This class creates a pygame.Surface object of a given size. The method `Screen.background` draws a background to the
surface given a sprite sheet and map of the background.

#### The `SpriteSheet` Class
This class allows the import and subdivision of sprite sheets into individual sprites.

### Miscellaneous functions
#### `fade`
The fade function creates a transparent surface to overlay on the screen for fading effects. The opacity of this surface
is determined by an inputted integer from 0 to 64, with 0 being clear, and 64 being no opacity.

## Art sources
background1.png and ui_hud.png by [Buch on OpenGameArt](http://opengameart.org/users/buch), public domain  
player.png by [Skylar1146 on OpenGameArt](http://opengameart.org/users/Skylar1146), public domain  
icon.png by [k-u-h-l](https://github.com/k-u-h-l), public domain  
