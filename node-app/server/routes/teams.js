const express = require('express');
const router = express.Router();

const { getAllTeams, getTeamById } = require('../config/teams'); // Adjust the path

router.get('/teams', async (req, res) => {
    try {
      const team = await getAllTeams();
        console.log(team)
      res.render('./partials/teams', {
        team
      });
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        res.status(500).send('Error fetching data from Python API');
    }
  });


router.get('/teams/:teamId', async (req, res) => {
    const teamId = parseInt(req.params.teamId, 10); // Convert teamId to integer

    try {
        // Fetch the team data from MongoDB
        const team = await getTeamById(teamId);

        if (team) {
            // Render the team data to a view template
            res.render('./partials/teams', {
                teams: [team]
            });
        } else {
            // If team not found, send a 404 response
            res.render('./partials/no-team-found');
        }
    } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).send('Error fetching data from MongoDB');
    }
});

module.exports = router;