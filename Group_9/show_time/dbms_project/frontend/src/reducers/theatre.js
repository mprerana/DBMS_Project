import { GET_THEATRE_LIST } from "../actions/types";

const initialState = {
  theatres: {}
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_THEATRE_LIST:
      return {
        ...state,
        theatres: action.payload
      };
    default:
      return state;
  }
}
