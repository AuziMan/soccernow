const express = require('express');
const router = express.Router();


const PYTHON_API = 'http://127.0.0.1:5000/ingest';

const getEuroGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API}/euro-games`);
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

const getUpcomingMLSGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API}/up-mls-games`);
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

const getPrevMLSGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API}/prev-mls-games`);
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
        const response = await fetch(`${PYTHON_API}/all-live-games`);
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
        const response = await fetch(`${PYTHON_API}/live-mls-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        return data;


        //console.log(data);
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

module.exports = {
    getUpcomingMLSGames,
    getPrevMLSGames,
    getAllLiveGames,
    getLiveMLSGames,
    getEuroGames
};
