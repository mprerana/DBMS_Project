import { GET_SPECIFICMOVIE, ADD_COMMENT } from "../actions/types";

const initialState = {
  specificmovie: {}
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_SPECIFICMOVIE:
      return {
        ...state,
        specificmovie: action.payload
      };
    case ADD_COMMENT:
      return {
        ...state
      };
    default:
      return state;
  }
}
