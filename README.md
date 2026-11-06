# Flow Tetris

An endless, adaptive falling-blocks game built for staying in the flow state. It runs in a single HTML file with no install.

**Play:** open `index.html` in a browser.

## How it works
- **No game over.** If you top out, the board clears and you keep 60% of your momentum.
- **Adaptive speed.** After every piece the game computes a pressure from four signals:
  ```
  pressure = (height − 0.45)/0.35            stack height
           + trend · (6 if worsening, 14 if improving)   rate of change of board stress
           + 2 · (0.85 − quality)            placement quality vs the best available spot
           + 2.5 · (timeUse − 0.7)           think time ÷ time for the piece to fall the board
  ```
  Pressure is bent exponentially (barely moves near balance, pushes hard at the extremes), then nudges your momentum: climbs gently (+0.6 max per piece), brakes firmly (−2.5). Like a psychophysics staircase, the step shrinks each time speed changes direction, so it settles at your edge. Speed never drops below 60% of your session best, except near the very top of the board, where a safety factor brings it back to the starting speed.
- **Placement quality.** Like a chess engine, the game scores every spot each piece could have gone (height, lines, holes, bumpiness) and rates your move from 0 (worst) to 1 (best). Multi-line clears are valued far above singles, and one open well column is not penalized, so building toward a 4-line clear counts as a good move.
- **Flow score** = speed × placement quality, averaged over about the last 20 pieces. It only climbs by making good moves continuously at high speed, and multi-line clears add +20% per extra line. Session peak and best ever are tracked.
- **Speed held.** The panel shows the speed you have sustained over the last 30 and 60 seconds (the slowest you dropped to in that window), with all-time records. Beating a record plays a bowl chord.
- **Tuned on real play.** The constants were tuned over about 5,800 logged pieces of play. To log your own, run `python3 log-server.py` while playing; each piece is appended to `play-log.jsonl`. Without the server, nothing is recorded.

## Modes (M or 1–5)
1. **Classic**: plain and minimal.
2. **Zen Mandala**: dreamy Buddhist palette, rotating mandala, and singing-bowl sound bath.
3. **Stained Glass**: blocks are windows onto a living Julia-set fractal that dives deeper as your flow rises.
4. **Bloom**: colored pieces bloom open into the same shared, breathing fractal when they land.
5. **Evolution**: each landing freezes the next stage of the fractal's journey, so your stack becomes a timeline.

## Controls
← → move · ↓ soft drop · Space hard drop · ↑/X rotate · Z rotate back · C hold · P pause · N mute · − / = volume
