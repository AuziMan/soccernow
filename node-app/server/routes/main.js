const express = require('express');
const router = express.Router();

const { getUpcomingMLSGames, getPrevMLSGames, getAllLiveGames, getLiveMLSGames } = require('../config/sports'); // Adjust the path

router.get('/', async (req, res) => {
    try {
      const upcoming = await getUpcomingMLSGames();
      const prev = await getPrevMLSGames();
      const live = await getAllLiveGames();
      const liveMLS = await getLiveMLSGames();

      res.render('main', {
        upcoming,
        prev,
        live,
        liveMLS
      });
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        res.status(500).send('Error fetching data from Python API');
    }
  });


  module.exports = router;
