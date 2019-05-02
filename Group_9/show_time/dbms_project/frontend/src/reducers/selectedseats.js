import { GET_SELECTED_SEATS } from "../actions/types";

const initialState = {
  selectedseats: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_SELECTED_SEATS:
      return {
        ...state,
        selectedseats: action.payload
      };
    default:
      return state;
  }
}
