import React from "react";
import GameCards from "./GameCards";
import '../css/gameCards.css'; // You can create a separate CSS file for this component


function GameLists({ games }) {

    // Loop through the game array and use reduce to identify the different leagues
    const groupedGames = games.reduce((acc, game) => {
        // Set the leage Name
        const leagueName = game.fixture_league_info.name;

        // Check if this league already exists. 
        if(!acc[leagueName]) {
            acc[leagueName] = []; // if not, create a new array with the league name
        }
        acc[leagueName].push(game)
        return acc
    }, {})

    return (
        <div className="center-wrapper">
            {Object.keys(groupedGames).map(league => (
                <div className="league-container" key={league}>
                    <h2 className="league-name">{league}</h2>
                    <div className="team-games-container">
                        {groupedGames[league].map(game => (
                            <GameCards key={game.id} game={game} />
                        ))}
                    </div>
                </div>
            ))}
        </div>
    );
}

export default GameLists;
