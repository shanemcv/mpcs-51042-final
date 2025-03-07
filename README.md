# mpcs-51042-final
Final Project for MPCS 51042 (Fishing Game)

GENERAL INFORMATION - read this first!

(1) Game source files are uploaded to this GitHub repo. You can play the game by downloading the repo and running the main.py file. 

(2) I created an executable for the game as well. You can access this executable file at ([THIS LINK](https://drive.google.com/file/d/1OQYeOY-Tu3jekvFWLvXft0ENI4mDfo91/view?usp=sharing)). I did not include it in the github repo because it is too large. 

RECOMMENDATION - the easiest way to play using the executable file will be to download it from the above link and place it in your cloned repo in the main project directory (i.e. where all the .py files are). 

If you wish to create the executable yourself, you can follow the below instructions: 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

(1) Download the github repo

(2) Run this pyinstaller code at the terminal, updating with the path to your local repository
pyinstaller --onefile --name=fishtown --distpath ./ --windowed --icon=images/icon.ico --add-data "images;images" --add-data "help.txt;." --add-data "player_data;player_data" "<PATH_TO_YOUR_LOCAL_REPOSITORY>\mpcs-51042-final\main.py"
For example, my command prompt was:

pyinstaller --onefile --name=fishtown --distpath ./ --windowed --icon=images/icon.ico --add-data "images;images" --add-data "help.txt;." --add-data "player_data;player_data" "C:\Users\mcvei\Desktop\UChicago Winter 25\MPCS-51042-Python\mpcs-51042-final\main.py"

(3) This will create an executable file in your main directory of your cloned repo. You can run the game from that executable file. 

(4) Note - you may need to turn off Real-time protection under "Virus and threat protection settings" in Windows settings, 
so that pyinstaller can create the executable. 

(5) To trust the executable always >> go to Windows Security, Virus and Threat Protection Settings, Add Exclusion, and then add the local repository folder path, or directly the .exe file to the exclusions

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Overview (Fishing Game - from Proposal)

I have always liked basic desktop games and applications, like Minesweeper or Solitaire. My first idea for a project would be to create a fun game that can be packaged into an executable program using tkinter or another basic UI toolkit. I have an idea for a fishing game where the player can: 
 - Catch fish, with some species being more common and more rare
 - Have logic to determine the “grade” of the fish once caught
 - Sell fish and buy fishing equipment in a shop. 
 - Change locations in order to have a different fishing experience and catch different types of fish. 
 - Track their achievements in the game application. 
 - Player information is saved across different runs of the game. 

- Convert the game into an executable and downloadable program.

TO DO LIST: 

 - Week 4: Create the baseline structure for the game, including a tkinter executable window that allows the player to run the program and catch fish into their inventory. Save player information into pickle files.  
 - Week 5: Include fish grading logic; build basic shop workflow. Allow players to buy certain fishing equipment and certain fish. 
 - Week 6: Add experience and currency to track how well the player is doing. Track the player's current skill at fishing using the experience and check their currency. Make sure currency works with shop. Add currency values to fish based on species and grade. 
 - Week 7: Add locations and new fish species to allow for gameplay variety. Add logic to when fish are "available" (certain times of day, months). Allow players to unlock location through shop. 
 - Week 8: Add achievements to the game. Allow the player to check their achievements and requirements for achievements that have not been completed yet.  
 - Week 9: Convert the game into an executable and downloadable program. 
