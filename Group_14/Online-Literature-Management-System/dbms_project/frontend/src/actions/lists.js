import axios from "axios";
import {GET_ERRORS, GET_LISTS, DELETE_LIST, ADD_LIST} from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig } from "./auth";


// GET LISTS
export const  getlists = (id) => (dispatch, getState) => {
    axios
        .get(`literature/readinglist/${id}/`, tokenConfig(getState))
        .then(res => {
           dispatch({
               type: GET_LISTS,
               payload: res.data
           });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//DELETE LIST

export const deletelist = id => (dispatch, getState) => {
    axios
        .delete(`literature/readinglistdelete/${id}/`, tokenConfig(getState))
        .then(res => {
            dispatch(createMessage({ deletelist: "List deleted" }));
            dispatch({
                type: DELETE_LIST,
                payload: id
            });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//ADD LIST

export const addlist = (list,id) => (dispatch, getState) => {
    const config ={
        headers:{
            "Content-Type":"application/json"
        }
    };

    

    const info = JSON.stringify({
        addlist:{
            r_list_name:list
        }

    });

    console.log(info);


    axios
        .post(`literature/readinglistpost/${id}/`, info, tokenConfig(getState))
        .then( res => {
            dispatch({
                type: ADD_LIST,
                payload: res.data
            });

        }).catch(err => {
            const errors = {
                msg: err.response.data,
                status: err.response.status
            };

            dispatch({
                type: GET_ERRORS,
                payload: errors
            });
});
};

