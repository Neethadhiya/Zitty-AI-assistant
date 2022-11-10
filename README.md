# Zitty-AI-assistant
Vasee AI Corporation has opened out a challenge to build its highly intelligent personal robotic assistant called Zitti. Zitti is capable of responding to a few instructions and questions. It can clean the room, fetch your newspaper and answer a few questions. The Robot works based on the instruction/question issued to it.
For example:
Instruction: Hey. How are you?
Response: Hello, I am doing great.
I: How's the weather outside?
R: It's pleasant outside. You should take a walk.
I: Clean my room
R: Room is cleaned. It looks tidy now. Job completed at <current time>
I: Add Soap to my shopping list
R: Soap added to your shopping list.
I: Fetch the newspaper
R: Here is your newspaper.
I: Add <any-item> to my shopping list
R: <any-item> added to your shopping list.
I: Read my shopping list
R: Here is your shopping list. Soap, Shampoo, Conditioner.

You decided to give it a try and take up the Zitti challenge:
But you have to make sure that the Robot has a bit of a logic as well. The responses can vary
based on a few conditions:
Example 1: You ask it to clean the room again within 10 minutes, it politely declines stating:
The room was just cleaned <minutes since the last time the room was cleaned> minute(s)
ago. I hope it's not dirty
Example 2 - You ask it to fetch the newspaper within the same day, it politely declines
stating:
I think you don't get another newspaper the same day
Example 3 - You ask it to add an existing item on shopping list, it politely declines stating:

You already have <item name> in your shopping list
Example 4 - When you shopping list is empty, it says:
You have no items in your shopping list
Example 5 - When the question does not match any of the above mentioned template, it
declines stating:
Hmm.. I don't know that
RUN 
Run the program using the command python zitty.py or   python .\zitty.py in the terminal.
