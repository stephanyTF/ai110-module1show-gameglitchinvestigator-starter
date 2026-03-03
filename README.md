# 🎮 Game Glitch Investigator: The Impossible Guesser

## TF Wk2 Task: Short Guiding Hint:

### Phase 1: Glitch Hunt (Spot Check)

#### Identified 6 bugs 
- 🐞1. [Hard Coded Range] <app.py line 110>:
   - No matter the difficulty mode, the range shown is always from 1-100 which can be misleading to the user. Instead it should be reflecting the range specified for each difficulty mode: 
   - Ex: Easy - 1-20, Hard 1-50
- 🐞2. [Attempt Off by 1] <app.py line 96>: 
  - In the dev log, the user’s first attempt is already counted as used even though the user hasn’t made a guess yet, so they’re always short 1 attempt.
- 🐞3. [Secret Answer Not in Current Mode Range ]  <app.py line 136>:
  - Range of number shown to user that they can guess, doens’t change in the blue toast
  - The secret answer doesn’t change even if its out of range from the Difficulty mode
  - Ex: Hard Mode (1-50) but the secret answer is 84 
- 🐞4. [Inverted Logic and hints]  <app.py line 32-47>
  - The hints tell the opposite of how they should change their number. 
  - For ex: when the guess is lower than the answer, the hint tells them to go lower not higher. 
- 🐞5. [Inconsistent Scoring Logic] <app.py line lines 50-65>
  - Final Score is Diff than whats shown in the developer log
  - Unclear about how scoring should work
- 🐞6. [New Game Reset] <line 134-138>
   - New game doesn’t reset win/loss status
   - The range is hard coded set to 1-100 and doesn't reflect the mode


### Phase 2: Investigate and Repair (Assigned)
  - Fixed all 6 Bugs
  - Reviewed and Modified AI-Generated Edit on Scoring Logic:
     - My final fixes:
        - Changed score calculation to be based on efficiency (attempts used relative to attempt limit) rather than a flat deduction per attempt, to better reflect performance across different difficulties
    - Generated pytest cases and ran pytest successfully for Scoring and Hints


   #### Short Guiding Hint: Scoring Logic:
   
   - To Identify: In streamlit, expand the dev log to see how the score changes and find the function responsible for it in the app.py
   - To Refactor the Scoring Logic:
     - If the current game logic is confusing don’t be afraid to completely change it into something that makes more sense for the game environment.
     - Think about what would make sense for scoring in any game. A higher score reflects better performance. Think how the number of attempts used until the answer is guessed correctly reflects the user’s  performance. 
   - Some Considerations:
     - Should a player on Easy (6 attempts) and Hard (5 attempts) get the same score for winning on attempt 2? How could scoring be fair across difficulties?"
     - Think about how the number of attempts used (out of the total allowed) reflects the user's performance across different difficulties
     - Formula Clue: The scoring formula should use a ratio, comparing attempts used to attempts allowed


### Phase 3: Reflection and README (Review)

   - Students should document their debugging experience and reflect on their usage of AI gen answers including its limiitations or shortfalls.
   - As TFs we should be prepared to help them through the reflection and updating their repo if needed.




## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
