
                                    EPL Fantasy League Optimal Team Pick Generator

We will let our analysis be guided by a few key questions below:

- Is there a correlation between individual player Fantasy League stats and their team table position and total points in the English premier league?
- Can we look at individual players as stocks and try to find the underpriced and overpriced players, so we can spend our limited budget in a way that generates the most return on investment(ROI), which in this example would represent total Fantasy points per 1MM dollars spent?
- If so can we build an algorithm that tries to pick as many of the high ROI players as possible and beat the AVG Fantasy player in  terms of total fantasy points returned for the 100MM budget that each player starts the game with.

Procedure:

1. Start with the EPL standings table and arrange teams by table position and look at the aggregate squad points for all their players and see if that correlates directly to the team Table position.

- Are there any surprises and outliers? How can that guide our further investigations?

2. Look at each Teams cumulative player ROI and plot that against the number of players that the coach uses on a regular basis to try to find the teams that have too many expensive and underperforming players and the teams that have a solid core of consistent players that generate a high aggregate ROI.

- Are there any surprises and outliers? How can that guide our further investigations?  Where are those diamonds in the rutt hiding? Which teams should we try to avoid buying players from?

3. Now we will dive deeper and look at individual player stats, so we can write our algorithm logic for picking the most optimal combination of individual players. Let's look at a scatter plot of Player Cost vs. Player total fantasy points. We would want our AI to pick players who are as west-north as possible in our scatter plot, but also a few that are far east-north, if these are some of the star league players with the most points in the whole league, who are naturally some of the most expensive.

- Does the team data agree with our player data? Do we find a lot of undervalued, high ROI players in those teams had a good total_points / total_cost ration?  

-What teams do some of the more overpriced players fall on?

4. Now let's look at the top 20 and bottom 20 players in terms of ROI and compare that to the AVG ROI for all players in the league.

- We should guide our Algorithm to pick as many of the top 20 as possible and stay away from the bottom 20.

5. Now it's time for the most fun part - writing the actual algorithm and comparing the results of the AI picks vs what an AVG person might pick as their team.  We also asked a classmate to pick a random team of his own to verify that our random team picker function is somewhat accurate.

Here are the basic constraints of the EPL Fantasy League:

1. Each fantasy player starts with a budget of 100M
2. You need to have at least 1 goalkeeper, 3 defenders, 3 midfielders and 2 strikers and at most 2 GK, 5 DF, 5 MF, and 3 STR.
3. You cannot have more than 3 players from the same team

So, we start our algorithm with these conditions and then we add our own conditions and logic on top of that, so that each time that the algorithm loops through our list of players, it can make a valid pick:

4. Check if a player is injured first and if so, skip that player.
5. Pick the top three start players with the most cumulative league points first. We will test the outcome of this condition with different constraints and pick the number of start players that generates the biggest return on investment.
6. Every time we pick a player and add it to our team, we subtract their cost from our 100MM budget and we add their position and team-name to a list, to make sure that we stop buying players for the positions and the teams that hit their constraint limit.
7. Once the optimal number of star players are picked, the Algorithm starts going through the list of players withe highest ROI and tries to get us as many of the top names as we can, until we get close to depleting our budget and filling all of the team positions.
8. Algorithm prints a list of the players it picked at the end and gives us the remaining budget and the total fantasy points of the team.
9. We repeat the same procedure for the AVG Joe team algorithm, which focuses more on star players and players from big teams, who are often overpriced and might not return the highest cumulative ROI for our limited budget of 100M.
10. In the end we compare the results of our AI Team vs. the AVG Joe team vs. Random Classmate team to see which one performed best and by what margin.

- Did our AI return the highest ROI team?  Did it beat the others by a significant margin?
- Did our AI pick players from some middle of the table teams, which we initially identified as undervalued?
- Did the AVG Joe pick more expensive players from the top teams and what was their team variety?

Conclusion:

Removing team/player biases and favoritism and focusing on the actual stats, allows our AI to get the most bang for our buck and beat the AVG EPL player by a total of 132 pts or a whole %16.25.

11. Next steps: Keep monitoring the data and see if there are any drastic changes further in the season, when players start getting injured and the battle for points tropheys gets more heated.
