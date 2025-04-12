# SoccerNow - Your place for accurtate soccer information

## The 'goal' (haha get it?) of SoccerNow is to provide simple, accurare soccer information from a variaty of leagues. 

### Whether its:
- game times
- game scores
- team squads
- game officials
- league standings

### Soccer now has you covered.
### SoccerNow displays soccer info in a easy to follow format using React for a seamless UI.

---

## Here is a diagram outlining the backend functionality of SoccerNow, starting from left to right.

---
![past-games](/readme-imgs/design-diagram.png)

---

#### This is design pattern I developed in order to stay within constraints of the public API I am using for all game and team information. 

#### The public API only allows 100 queries per day (free teir) so I was forced to created a light dependency with the public API to avoid over calling the service.

#### Each day, a CRON job makes a call for ALL games *two weeks ahead* of the current date for several leages. 

#### This allows me to not only ingest new games into my 'games' collection, but I can also recive any updates such as 
- squad changes
- venue changes
- referee changes
- time changes

#### By making one call each day, I am able to display the upcoming games *in the useres current timezone* (timezone conversion logic I developed) and also update the results of the games that have already occured.
---
#### A marjor update I would like to implement is 'live updates'

#### I can do this by making 4 calls per game to check for any updates such as goals, substitutions, etc

#### Unfortunatly this would not be as live as I would like, but a user would be able to track the progress of a game in a delayed fashion. 
---

#### After making a successful call to the public API and retrieveing all upcoming games for the current leages, I perform schema validation to ensure all fields I intend to use on the frontend are present and in the corrent format. 

#### A similar process is used for 'teams' ingestion. Each week, I make a call to the public API and retrieve each team from each league, and perform updates to the 'teams' collection (if any)

---

## Below are some screenshots from the frontend:


### Past Games:

![past-games](/readme-imgs/past-games.png)

### Team Squads page:
![team-squads](/readme-imgs/team-squads.png)

