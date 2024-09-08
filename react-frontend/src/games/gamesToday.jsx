import React, { useEffect, useState } from 'react';
import '../css/upcomingGames.css';

function GamesToday() {
    const [games, setGames] = useState([]);
    const [isLoading, setIsLoading] = useState(true); // New isLoading state


    useEffect(() => {
        fetch(`${process.env.REACT_APP_SOCCER_API_ROOT}/games/games-today`)
            .then(response => response.json())
            .then(data => {
                console.log('Fetched Data:', data); // Log the fetched data to verify
                setGames(data);
                setIsLoading(false)
            })
            .catch(error => console.error('Error fetching data:', error));
            setIsLoading(false)

    }, []);

    const renderGames = () => {
        if(isLoading) {
            return <div>Loading...</div>
        }

        if (!Array.isArray(games) || games.length === 0) {
            return <div>No upcoming games available.</div>;
        }

        return games.map((game, index) => (
            <div class="center-wrapper">

                    <div key={index} className="team-game-team">
                        {game.fixture_teams && game.fixture_teams.home && game.fixture_teams.away ? (
                            <>
                                <h3>{game.fixture_teams.home.name} vs {game.fixture_teams.away.name}</h3>
                                <img src={game.fixture_teams.home.logo} alt={`${game.fixture_teams.home.name} Logo`} className="team-logo" />
                                <img src={game.fixture_teams.away.logo} alt={`${game.fixture_teams.away.name} Logo`} className="team-logo" />
                                <p>Date: {new Date(game.fixture_date).toLocaleString()}</p>
                                {/* <p>Location: {game.fixture_venue_name}, {game.fixture_venue_city}</p> */}
                            </>
                        ) : (
                            <p>Some game data is missing.</p>
                        )}
                    </div>
            </div>
        ));
    };

    return (
        <div>
            <div className="games-title">
                <h1>Games Today!</h1>
            </div>
            <div className="center-wrapper">
                <div className="team-games-container">
                    {renderGames()}
                </div>
            </div>
        </div>
    );
}

export default GamesToday;
