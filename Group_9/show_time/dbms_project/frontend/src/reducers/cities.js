import { GET_CITIES, SELECT_CITY } from "../actions/types.js";

const initialState = {
  cities: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_CITIES:
      return {
        ...state,
        cities: action.payload
      };

    default:
      return state;
  }
}

// case REGISTER_FAIL:
// localStorage.removeItem("token");
// return {
//   ...state,
//   token: localStorage.getItem("token"),
//   isAuthenticated: null,
//   isLoading: false,
//   user: null
// };
