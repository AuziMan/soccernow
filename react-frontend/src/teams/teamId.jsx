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
                
                // console.log(data)
                // const teamIds = data.map(team => team.team_id).join(', ');
                // console.log('Team IDs (Comma-Separated):', teamIds);

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
                    <div className="league-team-container">
                        <h3>{team.team_name}</h3>
                        <img
                                src={team.team_logo}
                                alt={`${team.team_name} logo`}
                                className="team-logo"
                            />
                            <div className="team-button-container">
                                <Link
                                    key={teams.team_id}
                                    to={`/games/${team.team_id}`}
                                    className="team-card">
                                <button className='team-buttons'>Past Games</button>
                                </Link>
                                <Link
                                    key={teams.team_id}
                                    to={`/teams/${team.team_id}`}
                                    className="team-card">
                                    <button className='team-buttons'>Squad</button>
                                </Link>
                            </div>
                    </div>))}
                </div>
            </div>
        </div>
      );
}

export default TeamId;
