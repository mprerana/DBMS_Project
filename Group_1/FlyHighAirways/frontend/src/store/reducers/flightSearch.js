const initialState = {
    source: '',
    destination: '',
    time: ''
};

const reducer = ( state = initialState, action ) => {
    switch(action.type) {
        case 'ADD_FLIGHT_FORM':

            const temp = {
                source: action.flightData.source,
                destination: action.flightData.destination,
                time: action.flightData.time
            }
            return temp;
        default:
            return state;
    }
};


export default reducer;