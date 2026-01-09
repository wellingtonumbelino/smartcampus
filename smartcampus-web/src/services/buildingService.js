import { apiRoom } from '@/api/apiConfig';

export async function getAllBuildings() {
  try {
    const { data } = await apiRoom.get(
      '/entities/?type=Room&options=keyValues&attrs=name,description',
    );
    console.log('Request', data);
    return { data, error: null };
  } catch (error) {
    console.error('Error fetching buildings:', error);
    return { data: null, error };
  }
}
