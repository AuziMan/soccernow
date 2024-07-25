const express = require('express');
const router = express.Router();

const { dbGetMLSGames, getUpcomingMLSGames, getPrevMLSGames, getAllLiveGames, getLiveMLSGames } = require('../config/games'); // Adjust the path

router.get('/', async (req, res) => {
    try {
      const upcoming = await getUpcomingMLSGames();
      const prev = await getPrevMLSGames();
      const live = await getAllLiveGames();
      const liveMLS = await getLiveMLSGames();
      const dbMLSGames = await dbGetMLSGames();

      const api_response = {upcoming,prev,live,liveMLS,dbMLSGames }

      function validte_data_response(input_data) {
        for(const key in api_response){
          if (!input_data[key] || (input_data[key].response && input_data[key].response.length === 0)){
            return false;
          }
        }
        return api_response;
      }

      let full_api_response = validte_data_response(api_response)

      if(api_response == 'test'){
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
