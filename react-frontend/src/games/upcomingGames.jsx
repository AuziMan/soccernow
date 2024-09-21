import React, { useEffect, useState } from 'react';
import GameCards from '../components/GameCards';

function UpcomingGames() {
    const [games, setGames] = useState([]);
    const [isLoading, setIsLoading] = useState(true); // New isLoading state


    useEffect(() => {
        fetch(`${process.env.REACT_APP_SOCCER_API_ROOT}/games/upcoming-games`)
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
           <GameCards key={index} game={game} />
        ));
    };

    return (
        <div>
            <div className="games-title">
                <h1>Upcoming Games!</h1>
            </div>
            <div className="center-wrapper">
                <div className="team-games-container">
                    {renderGames()}
                </div>
            </div>
        </div>
    );
}

export default UpcomingGames;
