# 3Day-100DaysOfPythonGPT-TreasureIsland
Day 3 of the [100 Days of Code with Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) from Udemy.

## What is 100DaysOfPythonGPT?

100 Days of Python is a Python Bootcamp from Udemy that provides 100 days of Python pratical content with lessons and projects. The GPT part is something I'm adding to the course and infers that I shall use ChatGPT's engine and/or API in some way on each and every one of those 100 projects. Furthermore, I shall also practice using PyTest to test these projects and applications at least in some level.

## TreasureIsland

Treasure Island is the third project of the third day of the bootcamp. Its original purpose is to develop Flow Control with if-else statements.

It is a sort of "Choose Your Own Adventure" game where the player is in a treasure island and the game gives them a scenario and two possible choices that lead to the next scenario.

It really can't be tested - or can, but I don't really know how.

## Treasure Island GPT

So, in this specific case, the GPT version is too big to be in the prior section. 

The teacher of the bootcamp asked to be more creative when creating the scenarios, consequences, etc. So, first of all, I used Chat GPT to create these scenarios, consequences, choices and everything.

Second, I made it infinite: the API uses a first scenario as base for the following one as well as the choices and the consequence of each choice. Then, going on, the API is fed with the scenario, choices and consequences it made itself to create the following one. If the AI determines that the character has died it sets an "is_game_over" flag that notifies the script to end the game.

Future addings to this may be to let the AI create the first scenario, then openning this "open-world" game to an universe of possible games. Further on we can use DALL-E (or some other Image Generative Model) to create an image for every scenario. We'd basically have an AI generate Light Novel that is completely diferent every time you play it.


## Project Structure

 - [src/](src/) - The `treasure_island.py` file holds the basic game as suggested by the bootamp, whilst `treasure_island_gpt.py` has the code for the game with AI scenario-generation;
 - [include/](include/) - The `gpt.py` file holds the `get_completion` function that accesses the ChatGPT API. 
