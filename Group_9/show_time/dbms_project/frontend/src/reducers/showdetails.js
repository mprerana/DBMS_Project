import { GET_SHOW_DETAILS } from "../actions/types";

const initialState = {
  showdetails: {}
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_SHOW_DETAILS:
      return {
        ...state,
        showdetails: action.payload
      };
    default:
      return state;
  }
}
