const express = require('express');
const router = express.Router();


const PYTHON_API_INGEST = 'http://127.0.0.1:5000/ingest';
const PYTHON_API_GAMES = 'http://127.0.0.1:5000/games';



const getEuroGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API_INGEST}/euro-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        
        
        return data;
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

const getUpcomingMLSGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API_GAMES}/upcoming-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        // console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

const dbGetMLSGames = async (teamId) => {
    try {
         const checkTeamsPassed = async () => {   
            const endpoint = teamId ?  `${PYTHON_API_GAMES}/${teamId}` : PYTHON_API_GAMES;
            const response = await fetch(endpoint);

            if (!response.ok){
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            return response.json();
        }
        const data = checkTeamsPassed();
        //console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

const getPrevMLSGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API_INGEST}/prev-mls-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        //console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

const getAllLiveGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API_INGEST}/all-live-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        //console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

const getLiveMLSGames = async (req, res) => {
    try {
        const response = await fetch(`${PYTHON_API_INGEST}/live-mls-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        return data;

        //console.log(data);
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

module.exports = {
    getUpcomingMLSGames,
    getAllLiveGames,
    getLiveMLSGames,
    getEuroGames,
    dbGetMLSGames
};
