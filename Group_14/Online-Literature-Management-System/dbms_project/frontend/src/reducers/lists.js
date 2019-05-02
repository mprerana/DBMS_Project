import { GET_LISTS, DELETE_LIST, ADD_LIST } from "../actions/types";

const initialState = {
    lists: []
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_LISTS:
            return{
                ...state,
                lists : action.payload
            };
        case DELETE_LIST:
            return{
                ...state,
                lists : state.lists.filter( list => list.id !== action.payload)
            };
        case ADD_LIST:
            return{
                ...state,
                lists: [...state.lists, action.payload]
            };
             default:
                return state;
    }
}