import { GET_WORKS, DELETE_WORK, ADD_WORK } from "../actions/types";

const initialState = {
    works: {}
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_WORKS:
            return{
                ...state,
                works : action.payload
            };
        case DELETE_WORK:
            return{
                ...state,
                //works : state.works.filter( work => work.id !== action.payload)
            };
        case ADD_WORK:
            return{
                ...state,
                //works: [...state.works, action.payload]
            };
             default:
                return state;
    }
}