
# ai-profit-suite

This repository contains simple tools to help grow income through daily skill improvement.

## Self-Learning Module

Run the module to get a new business skill and an income-generating task each day:

```bash
python self_learning_module.py
```

The first run creates `skills.json` and `progress.json` files to track your progress.

=======

# ai-profit-suite

This repository contains the AI Profit Suite application. Run `python main.py` to display the daily self-improvement task.
=======

# ai-profit-suite
=======
# AI Profit Suite

This simple tool helps you track daily learning prompts and rank them based on their usefulness. The program records ratings for each prompt, sorts them by average score, and removes items you mark with a score of `0`.

## Usage

Run the script with Python:

```bash
python3 main.py
```

You will be prompted to rate each learning strategy from 1 (least helpful) to 5 (most helpful). Enter `0` if the prompt was not helpful and should be discarded. After rating, the updated prompt list is saved to `prompts.json` and displayed in ranked order. main

