const express = require('express');
const router = express.Router();

const { dbGetMLSGames, getUpcomingGames, getGamesToday, getAllLiveGames, getLiveMLSGames } = require('../config/games'); // Adjust the path

function getTimeZone() {
  const options = { timeZoneName: 'short' };
  const date = new Date();
  const timezone = date.toLocaleString('en-US', options).split(' ')[3];
  return timezone;
}

const userTimezone = getTimeZone();
console.log(userTimezone); // Output: PST, EST, CST, etc.


router.get('/', async (req, res) => {
    try {

      const leagueId = req.query.leagueId

      const upcoming = await getUpcomingGames(leagueId);
      const live = await getAllLiveGames();
      const liveMLS = await getLiveMLSGames();
      const gamesToday = await getGamesToday(userTimezone);
      // const dbMLSGames = await dbGetMLSGames();
      //const api_response = {upcoming,live,liveMLS,dbMLSGames }
      


      const api_response = {upcoming, gamesToday, live,liveMLS }

      function validate_data_response(input_data) {
        for(const key in api_response){
          if (!input_data[key] || (input_data[key].response && input_data[key].response.length === 0)){
            return false;
          }
        }
        return api_response;
      } 

      let full_api_response = validate_data_response(api_response)

      if(api_response == false){
        res.render('partials/no-games', {
          message: 'No Games found'
        });
      } else {
          res.render('main', full_api_response);
      }
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        res.status(500).send('Error fetching data from Python API');
    }
  });


  module.exports = router;