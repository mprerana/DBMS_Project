import { GET_FORMATS } from "../actions/types";

const initialState = {
  formats: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_FORMATS:
      return {
        ...state,
        formats: action.payload
      };
    default:
      return state;
  }
}
