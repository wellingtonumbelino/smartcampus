import { roomApi } from "../api/config";

export async function getAllRooms() {
  try {
    const response = await roomApi.get(
      "/entities/?type=Room&options=keyValues&attrs=name,description",
    );
    return { data: response.data, error: null };
  } catch (error) {
    return { data: null, error };
  }
}

export async function createNewRoom(
  id: string,
  name: string,
  description: string,
) {
  try {
    const newRoom = {
      id: `urn:ngsi-ld:Room:${id}`,
      type: "Room",
      name: { type: "Text", value: name },
      description: { type: "Text", value: description },
      category: {
        type: "Array",
        value: [
          "telecommunicationsRoom",
          "classroom",
          "laboratory",
          "projectRoom",
          "meetingRoom",
        ],
      },
      floor: { type: "Integer", value: 1 },
      refBuilding: { type: "Relationship", value: "urn:ngsi-ld:Building:003" },
    };

    await roomApi.post("/entities/", newRoom);
  } catch (error) {
    return { data: null, error };
  }
}

export async function deleteRoomById(id: string) {
  try {
    await roomApi.delete(`/entities/${id}`);
  } catch (error) {
    return { data: null, error };
  }
}
