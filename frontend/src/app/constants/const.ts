export const API_HOST = 'localhost:4200';
export const API_URL = 'http://' + API_HOST + '/api';

export const API_ENDPOINTS = {
    login: API_URL + '/login',
    fetchScripts: API_URL + '/scripts/fetch',
    createScript: API_URL + '/scripts/create',
    fetchScript: (id: number) => `${API_URL}/scripts/${id}`,
    updateScript: (id: number) => `${API_URL}/scripts/${id}/update`,
    executeScript: (id: number) => `${API_URL}/scripts/${id}/execute`,
}

export const DEFAULT_SCRIPT_NAME = "Default name";