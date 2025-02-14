import React, { useEffect, useState } from 'react';
// import GameCards from '../components/GameCards';
import GameLists from '../components/GameLists';


function PastGames() {
    const [games, setGames] = useState([]);
    const [isLoading, setIsLoading] = useState(true); // New isLoading state


    useEffect(() => {
        fetch(`${process.env.REACT_APP_SOCCER_API_ROOT}/games/past-games`)
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
            return <div className="no-games">
            <h2>No past games avalible.</h2>
        </div>
        }

        return<GameLists games={games} />

    };

    return (
        <div className="center-wrapper">
            <div className="games-title">
                <h1>Past Games!</h1>
            </div>
            <div className="center-wrapper">
                    {renderGames()}
            </div>
        </div>
    );
}

export default PastGames;
