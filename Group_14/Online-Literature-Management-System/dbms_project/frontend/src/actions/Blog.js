import axios from 'axios';
import {GET_BLOG, DELETE_BLOG, ADD_BLOG} from './types';
import {returnErrors} from "./messages";
import  { tokenConfig} from "./auth";


// GET BLOG LIST

export const getBlog = (id) => (dispatch, getState) => {
    axios.get(`literature/bloglist/${id}/`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_BLOG,
                payload: res.data
            });

        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

// DELETE BLOG 

export const deleteBlog = (id) => (dispatch, getState) => {
    axios.delete(`literature/blogdelete/${id}/`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: DELETE_BLOG,
                payload: id
            });

        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

// DELETE BLOG 

export const addBlog = (title, content, id) => (dispatch, getState) => {

    const config ={
        headers:{
            "Content-Type":"application/json"
        }
    };

    

    const Blog = JSON.stringify({
        addblog:{
            blog_title: title,
            blog_content : content
        }

    });

    console.log(Blog);




    axios.post(`literature/blogpost/${id}/`, Blog , config, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: ADD_BLOG,
                payload: res.data
            });

        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};
