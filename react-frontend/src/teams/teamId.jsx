import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom'; // To get the leagueId from the URL
import '../css/teamPages.css';

function TeamId() {
    const {leagueId} = useParams();
    const [teams, setTeams] = useState([]);
    const [isLoading, setIsLoading] = useState(true); // New isLoading state
    const [error, setError] = useState(null);


    useEffect(() => {
        const fetchTeams = async () => {
            try{
                const response = await fetch(`${process.env.REACT_APP_SOCCER_API_ROOT}/leagues/${leagueId}`);
                if(!response.ok){
                    throw new Error(`Error fetching teams: ${response.statusText}`);
                }
                const data = await response.json();
                setTeams(data)
                setIsLoading(false);
            } catch (error){
                setError(error.message);
                setIsLoading(false)
            }
        };

        fetchTeams();
    }, [leagueId]);


    if(isLoading){
        return (
            <div className="center-wrapper">
                <div>Loading....</div>
            </div>
        )
    }


    if(error){
        return <div>Error: {error}</div>
    }

    return (
        <div className="center-wrapper">
            <div className="team-container">
            <h2>Teams in League</h2>
            <div className="teams-container">
                {teams.map((team) => (
                    <Link
                        key={teams.team_id}
                        to={`/teams/${team.team_id}`}
                        className="team-card"
                    >
                        <h3>{team.team_name}</h3>
                        <img
                        src={team.team_logo}
                        alt={`${team.team_name} logo`}
                        className="team-logo"
                        />
                </Link>
                ))}
            </div>
            </div>
        </div>
      );
}

export default TeamId;
