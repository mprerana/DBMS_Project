import { GET_MOVIES } from "../actions/types.js";

const initialState = {
  movies: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_MOVIES:
      return {
        ...state,
        movies: action.payload
      };
    default:
      return state;
  }
}
