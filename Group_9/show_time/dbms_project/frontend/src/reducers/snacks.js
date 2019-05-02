import { GET_SNACKS } from "../actions/types";

const initialState = {
  snacks: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_SNACKS:
      return {
        ...state,
        snacks: action.payload
      };
    default:
      return state;
  }
}
