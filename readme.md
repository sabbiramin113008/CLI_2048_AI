## CLI_2048_AI 
    CLI_2048_AI is a famous 2048 gaming interface from 
    Command Line for Teaching your Moves to an AI.
    
### Motivation
    2048 is not a newer game. It's a solid mathematical game for playing.
    Though the motivation was to teach your move to an AI, and then play along.
### Basics in a Nutshell.
    Firstly you need to play with the moves. The Moves are automatically recoreded and saved.
    Secondly when you load your AI, a Model based on Multi layer Perceptron Classifier is built being Trained on your move.
    
    Currently 30 Moves are alloted for AI's move. You can fork the Repo and Trained it on your own.
    
## How To Play
### Teaching AI the Moves
    1. Run 'python PlayBoard.py'.
    2. Select '1' to teach your moves to AI. Now Enter Your Name ( Put a Single Word).
    3. Press 'l' = To Left Turn.
    4. Press 'r' = To Right Turn.
    5. Press 'd' = To Down Turn.
    6. Press 'u' = To Up Turn.
    7. Press ' ctrl + C ' to Quit Teaching.
    
### Testing Your AI
    1. Run 'python PlayBoard.py'.
    2. Select '2' to Test The AI.
    3. Now Enter the Name you put earlier while teaching.
    4. Now A Multi Layer Perceptron Based Classifier is Trained on the moves Your played earlier.
    5. If model is trained successfully, you will get perfomance metrics.
    6. Now an AI trained on your moves will start playing the moves.
    
### PS.
    1. There is already recoreded data in the profile name of 'tasbir'.
    2. Your can directly type the name while Testing the AI, and it will load data from the profile named 'tasbir'.