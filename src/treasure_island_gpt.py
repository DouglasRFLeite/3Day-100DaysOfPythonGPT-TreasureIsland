import sys
from os.path import abspath, dirname

# Add the parent directory of the current file to sys.path
sys.path.append(abspath(dirname(dirname(__file__))))

from include import gpt
import xml.etree.ElementTree as ET

first_scenario = """
You have always heard the tale of the Treasure Island, some place in the middle of the sea
where people believed to be a hidden lost treasure that can change your life completly. 

So, trying to find this treasure, you got into a ship and, when it was passing close to 
where this island should be, you stealed the ships boat and sailed towards this place.

In the middle of the way a storm showed up and your boat was wrecked. Even though, you
had the luck to end up in the shore of a close island you believe was the one you looked for.

Know you have two options:
"""

first_choice = """
1 ) Go inside the jungle that is ahead of you and try to find something there.
"""

first_consequence="""
You enter the jungle and walk in it for a while not seeing anything of interest, but soon
enough you find yourself been chased by some very angry monkeys throwing rocks at you and
you run trying to loose them.
"""

def create_choice_story(step):
    prompt= f"""
I am building a game of Choose Your Own Adventure called "Treasure Island". My player is 
set in an Island where they believes there is a hidden treasure. I will provide them with a
scenario and give them a two choices each round, depending on what they chooses, the outcome
will differ. 

Your task is to create the scenario and the two choices for them. Your response shall
be a XML like this example:

'''
<root>
    <scenario>
    You are at a crossroad. On the left you can scent a really strong and disgusting smell of 
    blood. On the right you hear the flow of water at a distance. Choose one of the following:
    </scenario>
    <choice1>
    1 ) Take the path to your right.
    </choice1>
    <choice2>
    2 ) Take the path to your left.
    </choice2>
    <consequence1>
    You have taken the path to your right. You walk for a bit and the sound of water flowing
    gets bigger every second.
        <is_game_over>False</is_game_over>
    </consequence1>
    <consequence2>
    You followed the scent of blood and soond found out where it came from. A pile of corpses
    lies ahead of you and, out of nowhere, something bites your head off and you die.
    GAME OVER
        <is_game_over>True</is_game_over>
    </consequence2>
</root>'''

Remember to give the answer after removing every possible blank space. Also, know that you
should make the "is_game_over" tag True only if the character dies in that consequence.

You shall also use their last scenario, choice and consequence as a starting point to 
your creation. They were:
<last scenario>
{step["scenario"]}
</last scenario>
<last choice>
{step["choice"]}
</last choice>
<last consequence>
{step["consequence"]}
</last consequence>

Make creative scenarios, choices and consequences.
    """

    return gpt.get_completion(prompt=prompt)

def consume_gpt_creation(gpt_creation):
    try:
        root = ET.fromstring(gpt_creation)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        print(gpt_creation)
        exit()

    data = {}
    data["scenario"] = root.find('scenario').text
    data["choice1"] = root.find('choice1').text
    data["choice2"] = root.find('choice2').text
    data["consequence1"] = root.find('consequence1').text
    data["is_game_over_1"] = root.find('consequence1').find("is_game_over").text
    data["consequence2"] = root.find('consequence2').text
    data["is_game_over_2"] = root.find('consequence2').find("is_game_over").text

    return data

def user_interaction(step):
    print(step["scenario"])
    print(step["choice1"])
    print(step["choice2"])

    user_choice = input("Type 1 to choose option 1 or 2 to choose option 2: ")
    print(step["consequence"+user_choice])

    if step["is_game_over_"+user_choice] == "True":
        print("GAME OVER!")
        exit(0)

    next_step = {
        "scenario" : step["scenario"],
        "choice" : step["choice"+user_choice],
        "consequence" : step["consequence"+user_choice]  
    }

    return next_step




if __name__ == "__main__":
    first_step = {
        "scenario" : first_scenario,
        "choice" : first_choice,
        "consequence" : first_consequence 
    }

    next_step = first_step

    while(True):
        step = consume_gpt_creation(create_choice_story(next_step))
        next_step = user_interaction(step)

