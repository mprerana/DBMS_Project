import axios from 'axios';
import {ADD_FOLLOWING, DELETE_FOLLOWING, GET_ERRORS, GET_FOLLOWING} from './types';
import {createMessage, returnErrors} from "./messages";
import {tokenConfig} from "./auth";


//get following
export const getFollowing = (id) => (dispatch, getState) => {
    axios.get(`/following/${id}/`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_FOLLOWING,
                payload: res.data
            });

        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};
//Unfollow

export const deleteFollowing = (id1,id2) => (dispatch, getState) => {
    console.log(id1);
    console.log(id2);
    axios.delete(`/unfollow/${id1}n${id2}/`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: DELETE_FOLLOWING,
                payload: id1,id2
            });

        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//Follow

export const addFollowing = (id1, id2, data) => (dispatch, getState) => {

    axios.post(`/follow/${id1}n${id2}/`, data,  tokenConfig(getState))
        .then(res => {
            dispatch({
                type: ADD_FOLLOWING,
                payload: data
            });

        })
};


