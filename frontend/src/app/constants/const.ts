export const API_HOST = 'localhost:5000';
export const API_URL = 'http://' + API_HOST;

export const API_ENDPOINTS = {
    login: API_URL + '/login',
    fetchScripts: API_URL + '/scripts/fetch',
    createScript: API_URL + '/scripts/create',
    fetchScript: (id: number) => `${API_URL}/scripts/${id}`,
    updateScript: (id: number) => `${API_URL}/scripts/${id}/update`, 
}

export const DEFAULT_SCRIPT_NAME = "Default name";