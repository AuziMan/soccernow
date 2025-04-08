import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import HeaderNavBar from './views/navBar';
import GamesToday from './games/gamesToday'; // Import the UpcomingGames component
import UpcomingGames from './games/upcomingGames'; // Import the UpcomingGames component
import PastGames from './games/pastGames';
import Teams from './teams/teamId'
import TeamSquads from './teams/teamSquad';
import TeamGames from './games/teamGames';


function App() {
  return (
    <Router>
      <HeaderNavBar />
      <Routes>
        <Route path="/" element={<>
          <GamesToday />
          <UpcomingGames />
          <PastGames />

        </>} />

        {/* Add the dynamic route for teams */}
        <Route path="/leagues/:leagueId" element={<Teams />} />
        <Route path="/teams/:teamId" element={<TeamSquads/>} />
        <Route path="/games/:teamId" element={<TeamGames/>} />


        </Routes>
    </Router>
  );
}

export default App;
