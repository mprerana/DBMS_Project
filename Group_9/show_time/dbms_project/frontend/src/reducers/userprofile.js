import { GET_USERPROFILE, EDIT_USERPROFILE } from "../actions/types";

const initialState = {
  userprofile: {}
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_USERPROFILE:
      return {
        ...state,
        userprofile: action.payload
      };
    case EDIT_USERPROFILE:
      return {
        ...state,
        userprofile: action.payload
      };

    default:
      return state;
  }
}
