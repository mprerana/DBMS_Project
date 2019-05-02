import { GET_LANGUAGES } from "../actions/types";

const initialState = {
  languages: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_LANGUAGES:
      return {
        ...state,
        languages: action.payload
      };
    default:
      return state;
  }
}
