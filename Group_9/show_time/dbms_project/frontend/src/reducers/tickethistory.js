import { GET_TICKET_BOOKING_HISTORY, BOOK_HISTORY } from "../actions/types";

const initialState = {
  ticketbookinghistory: {}
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_TICKET_BOOKING_HISTORY:
      return {
        ...state,
        ticketbookinghistory: action.payload
      };
    case BOOK_HISTORY:
      return state;
    default:
      return state;
  }
}
