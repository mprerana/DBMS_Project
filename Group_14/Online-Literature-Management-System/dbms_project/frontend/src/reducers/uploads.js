import {GET_UPLOADS, DELETE_UPLOADS, ADD_UPLOADS} from "../actions/types";

const initialState = {
    uploads: []
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_UPLOADS:
            return{
                ...state,
                uploads : action.payload
            };
        case DELETE_UPLOADS:
            return{
                ...state,
                uploads : state.uploads.filter( upload => upload.id !== action.payload)
            };
        case ADD_UPLOADS:
            return{
                ...state,
                uploads: [...state.uploads, action.payload]
            };
             default:
                return state;
    }
}