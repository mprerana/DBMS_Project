import axios from "axios";

import { GET_SELECTED_SEATS } from "./types";

import { createMessage, returnErrors } from "./messages";

//GET SELECTED SEATS

export const getSelectedSeats = seatlist => dispatch => {
  dispatch({
    type: GET_SELECTED_SEATS,
    payload: seatlist
  });
};
