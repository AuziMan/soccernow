import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import '../css/teamSquads.css'; // Assuming you have a CSS file for styling

function TeamSquads() {
    const { teamId } = useParams();
    const [team, setTeam] = useState(null); // Store the entire team data
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchTeamSquad = async () => {
            try {
                const response = await fetch(`${process.env.REACT_APP_SOCCER_API_ROOT}/teams/${teamId}`);
                if (!response.ok) {
                    throw new Error(`Error fetching squad: ${response.statusText}`);
                }
                const data = await response.json();

                if (!data || data.length === 0) {
                    setError('No squad data available.');
                } else {
                    setTeam(data);
                }
                setIsLoading(false);
            } catch (error) {
                setError(error.message);
                setIsLoading(false);
            }
        };

        fetchTeamSquad();
    }, [teamId]);

    if (isLoading) {
        return <div>Loading squad data...</div>;
    }

    if (error) {
        return (
            <div className="center-wrapper">
                <div>{error}</div>
            </div>
        );
    }

    return (
        <div className="squad-container">
            {team && (
                <>
                    <div className="team-header">
                        <img src={team.team_logo} alt={`${team.team_name} logo`} className="team-logo" />
                        <h2>{team.team_name}</h2>
                    </div>
                    <h3>Squad List</h3>
                    <div className="squad-list">
                        {team.team_squad.map((player) => (
                            <div key={player.id} className="player-card">
                                <img
                                    src={player.phote}
                                    alt={`${player.name} logo`}
                                    className="player-img"
                                />
                                <h4>{player.name}</h4>
                                <p>Position: {player.position}</p>
                                <p>Number: {player.number ? player.number : 'N/A'}</p>
                            </div>
                        ))}
                    </div>
                </>
            )}
        </div>
    );
}

export default TeamSquads;