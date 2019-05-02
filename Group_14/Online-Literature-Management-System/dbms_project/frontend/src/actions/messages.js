import {CREATE_MESSAGE, GET_ERRORS} from './types';

//create msgs

export const createMessage = msg => {
    return {
        type: CREATE_MESSAGE,
        payload: msg
    };
};

//related to 5th tutorial
//return errors
export const returnErrors = ( msg, status ) => {
        return {
            type: GET_ERRORS,
            payload: {msg, status}
        };
};