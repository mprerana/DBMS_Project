import { GET_USERS } from '../actions/types.js';

const initialState = {
    Users: []
};

export default function(state=initialState, action) {
    switch(action.type) {
        case GET_USERS:
            return{
                ...state,
                Users: action.payload
            };
            default:
                return state;
    }
}