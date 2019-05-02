import axios from 'axios';
import {GET_FOLLOWERS, ADD_FOLLOWERS, GET_ERRORS,} from './types';
import {createMessage, returnErrors} from "./messages";
import {tokenConfig} from "./auth";

//get followers
export const getFollowers = (id) => (dispatch, getState) => {
    axios.get(`/followers/${id}/`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_FOLLOWERS,
                payload: res.data
            });

        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};





