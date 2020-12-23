---------------------------
## ASSESSMENT 
---------------------------
### Problem
Create a Hangman game. 

First, choose a random word, replace the letters with underscores then display it for the player to guess. The player has the chance to guess either a letter or a word. 

If the guess is a letter and  is present in the word, all instances of that letter is displayed on the screen. If not, the game records the letter and asks the player for another input. The player has a total of 7 tries to guess the word. 

However, on the occassion that the player decides to enter a word and the word matches, the player wins; if not, the game ends.

### Objective
Replicate the game.

### Logic
1. Randomly choose a word
2. Display chosen word with underscores
3. Ask the player to enter a letter/word
4. Check if the letter is in the word
    T:
        - Replace the underscore w/ letter
        - Check if the guess is correct:
            T:
                - print winner
                - ask if user wants to play again
    F:
        - Record the guess and store it 
        - Update the amount of lives the player has left
        - Display the player's previous guesses
        - Display the player's remaining lives
        - Ask the player to enter another letter **Start at step 2**
5. If guess is correct
    T: 
        - Display winner
        - Ask if the user wants to play again
    F:
        - ** Start from step 2
    
### Identify
Inputs
    - Player guess (letter/word)
    - Play again(y/n)
Outputs
    - Letter in underscores
    - Letters if guessed correctly
    - Word if guessed correctly


---------------------------
## DESIGN
---------------------------
![Hangman Flowchart] (https://drive.google.com/drive/folders/14d5OjS9v6kIpgyaD22N7HH5ofHD7KlZw "Hangman Flowchart")


----------------------------
## ANALYSIS
----------------------------
### Formulate
1. Create a list of words
    - Use a random package to pick a word
2. Change string to a list of characters
    - Create another list that replaces the characters with underscores
    - add spaces inbetween each underscore
    - print list with underscores
**LOOP**:
~~2. Change string to a list of characters~~
    ~~- Create another list that replaces the characters with underscores~~
    ~~- add spaces inbetween each underscore~~
    ~~- print list with underscores~~
3. Ask player to enter a letter or word
4. **IF** the player guess is > 1 && player guess == chosen word:
        - print winner
        - ask player to play again
  **ELIF** player guess == letter in word:
        - find all instances of the letter and update the underscore list that is being displayed
        **IF** list of underscore == list of characters:
            - print winner
            **IF** player wants to play again:
                    - pick a new word
            **ELSE**:
                    - Exit game
  **ELSE**:
        - print ERROR
        - add player guess to the list of previous guesses
        - update amount of tries left
        - display previous guesses
        - display amount of tries left
~~5. **IF** player guess is correct:~~
        ~~- print winner~~
        ~~**IF** player wants to play again:~~
                ~~~- pick a new word~~
        ~~**ELSE**:~~
                ~~- Exit game~~
    ~~**ELSE**:~~
        ~~- **CONTINUE~~

### Risk Assessment
1. Imports
2. Namespace
3. Variable names
4. Functions

### Risk Analysis
**Imports**
Random
String
A bunch of words?

**Variable names**
word_rotation - list of words
active_word - random word chosen from word_rotation
active_letters - list of letters form active_word
active_underscore - list of underscores from active_letters
player_guess - player's input
previous_guesses - stores player's previous guesses
lives - amount of tries left

**Functions**
active_word_breakdown(active_word)
    - turn active_word into a list of characters and store it in a variable
    - take the list of characters and create another list that replaces the characters with 
        underscores and store it
    - return both variables

    _Variables_
    active_to_letters
    active_to_underscore

    _RETURN_
    active_letters
    active_underscore

ask_player(active_word)
    - ask for player input
    - IF answer is NOT in the alphabet:
            - keep asking the user for an input
      ELSE:
            - return player_answer
    
    _Variables_
    player_guess

    _RETURN_
    player_guess

update_active(active_letters, active_underscore, player_guess)
    - iterate through active_letters and find the index of the letters the player guessed
    - iterate through active_underscore and replace the underscore with the letters using the index

    _Variables_
    guess_index

    _RETURN_
    active_underscore


play_again(word_rotation)
    - ask player if he/she wants to play again
    - IF player wants to continue:
            - choose a random word 
            - active_word_breakdown(active_word)
     ELSE:
            - exit game

    _Variables_
    play_again_ans
    active_word
