import React from 'react';
import './App.css';
import UpcomingGames from './server/upcomingGames'; // Import the UpcomingGames component
import HeaderNavBar from './views/navBar';

function App() {
  return (
    <div className="App">
      <HeaderNavBar />

      <h1>Soccer Information</h1>
      <UpcomingGames />  {/* Include the UpcomingGames component */}

    </div>
  );
}

export default App;
