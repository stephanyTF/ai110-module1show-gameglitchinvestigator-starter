# 🎮 Game Glitch Investigator: The Impossible Guesser

## TF Wk2 Task: Short Guiding Hint:
### Scoring Logic:

- To Identify: In streamlit, expand the dev log to see how the score changes and find the function responsible for it in the app.py
- To Refactor the Scoring Logic:
  - If the current game logic is confusing don’t be afraid to completely change it into something that makes more sense for the game environment.
  - Think about what would make sense for scoring in any game. A higher score reflects better performance. Think how the number of attempts used until the answer is guessed correctly reflects the user’s  performance. 
- Some Considerations:
  - Should a player on Easy (6 attempts) and Hard (5 attempts) get the same score for winning on attempt 2? How could scoring be fair across difficulties?"
  - Think about how the number of attempts used (out of the total allowed) reflects the user's performance across different difficulties
  - Formula Clue: The scoring formula should use a ratio, comparing attempts used to attempts allowed



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
