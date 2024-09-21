import React from 'react';
import '../css/gameCards.css'; // You can create a separate CSS file for this component

function GameCards({ game }) {
    return (
        <div className="center-wrapper">
            <div className="team-game-team">
                {game.fixture_teams && game.fixture_teams.home && game.fixture_teams.away ? (
                    <>
                        <h3>{game.fixture_teams.home.name}</h3>
                        <h4>VS</h4>
                        <h3>{game.fixture_teams.away.name}</h3>
                        <div className="img-score">
                            <img src={game.fixture_teams.home.logo} alt={`${game.fixture_teams.home.name} Logo`} className="team-logo" />
                            <h2>{game.fixture_score.fulltime.home}</h2>
                        </div>
                        <div className="img-score">
                            <img src={game.fixture_teams.away.logo} alt={`${game.fixture_teams.away.name} Logo`} className="team-logo" />
                            <h2>{game.fixture_score.fulltime.away}</h2>
                        </div>

                        <p>Date: {new Date(game.fixture_date).toLocaleString()}</p>
                        {/* <p>Location: {game.fixture_venue_name}, {game.fixture_venue_city}</p> */}
                    </>
                ) : (
                    <p>Some game data is missing.</p>
                )}
            </div>
        </div>
    );
}

export default GameCards;
