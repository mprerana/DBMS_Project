import axios from "axios";
import {GET_FEED} from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig } from "./auth";


// GET ALL WORKS
export const  getfeed = (id) => (dispatch, getState) => {
    axios
        .get(`literature/getfeed/${id}/`, tokenConfig(getState))
        .then(res => {
           dispatch({
               type: GET_FEED,
               payload: res.data
           });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};
