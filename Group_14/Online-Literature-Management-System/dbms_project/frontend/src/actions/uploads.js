import axios from 'axios';
import { GET_UPLOADS, DELETE_UPLOADS, ADD_UPLOADS, GET_ERRORS } from "./types";
import { createMessage, returnErrors } from "./messages";
import  { tokenConfig} from "./auth";



//GET UPLOADS
export const getuploads = (id) => (dispatch, getState) => {

    axios
        .get(`literature/works/${id}`, tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_UPLOADS,
                payload: res.data

                
            });

            console.log(res.data);
            console.log("check_data")
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//DELETE UPLOADS
export const deleteuploads = (id) => dispatch => {
    console.log(id)
    axios.delete(`literature/workdelete/${id}/`,)
        .then( res => {
            dispatch({
                type: DELETE_UPLOADS,
                payload: id
            });
        }).catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

//ADD UPLOADS

export const adduploads = (upload, id) => dispatch => {

    // const formData = new FormData();
    // formData.append('upload',upload);
    console.log("upload")
    console.log(upload)

    // const config={
    //     headers:{
    //         //"Content-Dispositon": "attachment; filename=abc.jpg",
    //         "Content-Type":"application/x-www-form-urlencoded"
    //     }
    // };

    // const book={
    //     work:upload
    // }

    axios.post(`literature/postwork/${id}/`, upload)
        .then( res => {
            dispatch({
                type: ADD_UPLOADS,
                payload: upload
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

