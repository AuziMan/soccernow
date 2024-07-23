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

      const noData = !upcoming || !prev || !live || !liveMLS || !dbMLSGames ||
                        (Array.isArray(dbMLSGames) && dbMLSGames.length === 0) ||
                        (upcoming.response && upcoming.response.status == '308');

      if(noData){
        res.render('partials/no-games', {
          message: 'No Games found'
        });
      } else {
          res.render('main', {
            dbMLSGames,
            upcoming,
            prev,
            live,
            liveMLS
          });
      }
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        res.status(500).send('Error fetching data from Python API');
    }
  });


  module.exports = router;
