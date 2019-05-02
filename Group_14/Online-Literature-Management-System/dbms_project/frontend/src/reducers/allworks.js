import {GET_ALLWORKS} from "../actions/types";

const initialState = {
    allworks: []
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_ALLWORKS:
            return{
                ...state,
                allworks : action.payload
            };
             default:
                return state;
    }
}