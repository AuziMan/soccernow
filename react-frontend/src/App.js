import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import HeaderNavBar from './views/navBar';
import GamesToday from './games/gamesToday'; // Import the UpcomingGames component
import UpcomingGames from './games/upcomingGames'; // Import the UpcomingGames component
import Teams from './teams/teamId'
import TeamSquads from './teams/teamSquad';


function App() {
  return (
    <Router>
      <HeaderNavBar />
      <Routes>
        <Route path="/" element={<>
          <GamesToday />
          <UpcomingGames />
        </>} />

        {/* Add the dynamic route for teams */}
        <Route path="/leagues/:leagueId" element={<Teams />} />
        <Route path="/teams/:teamId" element={<TeamSquads/>} />

        </Routes>
    </Router>
  );
}

export default App;
