const express = require('express');
const router = express.Router();

const { dbGetMLSGames, getUpcomingMLSGames, getGamesToday, getAllLiveGames, getLiveMLSGames } = require('../config/games'); // Adjust the path

router.get('/', async (req, res) => {
    try {
      const upcoming = await getUpcomingMLSGames();
      const live = await getAllLiveGames();
      const liveMLS = await getLiveMLSGames();
      const gamesToday = await getGamesToday();
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