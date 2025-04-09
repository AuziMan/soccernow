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

#### This was design pattern I developed in order to stay within constraints of the public API I am using for all information. 

#### The public API only allows 100 queries per day (free teir) so I was forced to created a light dependency with the public API to avoid over calling the service.

#### Each day, a CRON job makes a call for ALL games two weeks ahead of the current date for several leages. 

#### This allows me to not only ingest new games into my 'games' collection, but I can also recive any updates such as 
- squad changes
- venue changes
- referee changes
- time changes


#### After making a successful call to the public API and having all games for the current leages, I perform schema validation to ensure all fields I intend to use on the frontend are present and in the corrent format. 

#### A similar process is used for 'teams' ingestion. Each week, I make a call to the public API and retrieve each team from each league, and perform updates to the 'teams' collection (if any)






![past-games](/readme-imgs/past-games.png)