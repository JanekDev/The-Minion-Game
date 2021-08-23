# The-Minion-Game
### Just a fast and mathematically optimized solution of Minion Game problem with easily scalable amount of players.
## Description
Game starts with choosing the word to play with. The two player are Stuart & Kevin and they have to create as much substrings from given letters as possible.<br>
- Stuart's strings have to start with consonants
- Kevin's strings have to start with vowels

The player gets point for each occurence of substring in the primary string. The game ends when all players created all possible words.
## Solution
By solving this problem on a piece of paper for the case where some substring are overlapping (e.g. substring *ana* in *Banana* occurs twice, but each occurence overlaps the other), I managed to notice combination patter which allowed for fast and least space-complex soultion just by iterating through the whole string, without creating the list of possible letters combinations and then working with that list.<br>
**Note:** Input is *case insensitive.*

Example playthrough with word *Banana*:
[game](img/banana.jpg)
