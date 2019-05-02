import axios from "axios";
import {GET_ERRORS, GET_WORKS, DELETE_WORK} from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig } from "./auth";


// GET WORKS
export const  getworks = (id) => (dispatch, getState) => {
    axios
        .get(`literature/worksinreadinglist/${id}/`, tokenConfig(getState))
        .then(res => {
           dispatch({
               type: GET_WORKS,
               payload: res.data
           });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//DELETE WORK

export const deletework = (id1, id2) => (dispatch, getState) => {
    console.log("id1: %s",id1);
    console.log("id2: %s", id2);
    axios
        .delete(`literature/deleteworkinreadinglist/${id2}n${id1}/`, tokenConfig(getState))
        .then(res => {
            dispatch(createMessage({ deletework: "work deleted" }));
            dispatch({
                type: DELETE_WORK,
                payload: id1,id2
            });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//ADD LIST

// export const addlist = list => (dispatch, getState) => {
//     axios
//         .post('literature/readinglist/', list, tokenConfig(getState))
//         .then( res => {
//             dispatch({
//                 type: ADD_LIST,
//                 payload: res.data
//             });

//         }).catch(err => {
//             const errors = {
//                 msg: err.response.data,
//                 status: err.response.status
//             };

//             dispatch({
//                 type: GET_ERRORS,
//                 payload: errors
//             });
// });
// };

