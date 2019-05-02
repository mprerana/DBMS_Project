import axios from "axios";
import {ADD_LIST, ADD_WORK, GET_ALLWORKS, GET_ERRORS} from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig } from "./auth";


// GET ALL WORKS
export const  getallworks = () => (dispatch, getState) => {
    axios
        .get('literature/works/', tokenConfig(getState))
        .then(res => {
           dispatch({
               type: GET_ALLWORKS,
               payload: res.data
           });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const addworktolist = (id, work) => (dispatch, getState) => {

    axios
        .post(`literature/postworkinreadinglist/${id}/`, work, tokenConfig(getState))
        .then( res => {
            dispatch({
                type: ADD_WORK,
                payload: work
            });

        })
};