import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import GameCards from '../components/GameCards';


function TeamGames() {
    const { teamId } = useParams();
    const [games, setGames] = useState([]);
    const [teamName, setTeamName] = useState(''); // State for team name
    const [isLoading, setIsLoading] = useState(true); // New isLoading state
    const [error, setError] = useState(null);


    useEffect(() => {
        const fetchTeamGames = async () => {
            try{
                const response = await fetch(`${process.env.REACT_APP_SOCCER_API_ROOT}/games/${teamId}`)
                if (!response.ok) {
                    throw new Error(`Error fetching squad: ${response.statusText}`);
                }
                const data = await response.json();
                setGames(data);

                // Get Team Name from team Id

                if(data.length > 0) {
                    const firstGame = data[0];
                    const {home, away} = firstGame.fixture_teams
                    if(home.id === parseInt(teamId)){
                        setTeamName(home.name)
                    } else if (away.id === parseInt(teamId)){
                        setTeamName(away.name)
                    }
                }

                setIsLoading(false);
            } catch (error) {
                setError(error.message);
                setIsLoading(false);
            }
        };
        fetchTeamGames();
    }, [teamId]);

    const renderGames = () => {
        if(isLoading) {
            return <div>Loading...</div>
        }

        if (error) {
            return <div>Error: {error}</div>;
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
                <h1>Past Games for {teamName || 'Team'} </h1>
            </div>
            <div className="center-wrapper">
                <div className="team-games-container">
                    {renderGames()}
                </div>
            </div>
        </div>
    );
}

export default TeamGames;
