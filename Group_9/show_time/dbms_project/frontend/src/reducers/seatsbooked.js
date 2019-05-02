import { GET_SEATS_BOOKED, IN_BOOKING } from "../actions/types";

const initialState = {
  seatsbooked: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_SEATS_BOOKED:
      return {
        ...state,
        seatsbooked: action.payload
      };
    case IN_BOOKING:
      return state;
    default:
      return state;
  }
}
