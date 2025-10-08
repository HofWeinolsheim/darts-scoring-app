// Updated database functions to use the backend API
const API_BASE = '/api';

// Player management
export const savePlayerProfile = async (player) => {
  try {
    const response = await fetch(`${API_BASE}/players`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(player)
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error saving player:', error);
    return { success: false, error: error.message };
  }
};

export const getPlayers = async () => {
  try {
    const response = await fetch(`${API_BASE}/players`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error fetching players:', error);
    return [];
  }
};

// Game management
export const saveGameRecord = async (gameData) => {
  try {
    const response = await fetch(`${API_BASE}/games`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(gameData)
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error saving game:', error);
    return { success: false, error: error.message };
  }
};

// Statistics
export const getPlayerStats = async (playerId) => {
  try {
    const response = await fetch(`${API_BASE}/stats/${playerId}`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error fetching player stats:', error);
    return {};
  }
};

export const getLeaderboard = async () => {
  try {
    const response = await fetch(`${API_BASE}/leaderboard`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error fetching leaderboard:', error);
    return [];
  }
};

// Health check
export const checkHealth = async () => {
  try {
    const response = await fetch(`${API_BASE}/health`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error checking health:', error);
    return { status: 'error', error: error.message };
  }
};
