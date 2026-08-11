import { roomApi } from "../../../core/api/config";
import type { RoomResponseDTO } from "./room.dto";

export async function getAllRooms(): Promise<RoomResponseDTO[] | undefined> {
  try {
    const { data } = await roomApi.get(
      "/entities/?type=Room&options=keyValues&attrs=name,description",
    );
    return data;
  } catch (error) {
    console.error("Error loading rooms:", error);
    throw error;
  }
}

export async function createNewRoom(
  id: string,
  name: string,
  description: string,
) {
  try {
    const newRoom = {
      id: id,
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
