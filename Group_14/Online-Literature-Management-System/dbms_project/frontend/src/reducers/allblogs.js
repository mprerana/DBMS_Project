import { GET_ALLBLOGS } from "../actions/types";

const initialState = {
  allblogs: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_ALLBLOGS:
      return {
        ...state,
        allblogs: action.payload
      };
    default:
      return state;
  }
}
