import { apiDevice } from '@/api/apiConfig';

export async function getAllDevices() {
  try {
    const response = await apiDevice.get('/devices');
    return { data: response.data, error: null };
  } catch (error) {
    return { data: null, error };
  }
}
