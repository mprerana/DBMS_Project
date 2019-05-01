export const getTimeSlot = (time) => {
    if (time >= 3 && time < 9) {
        return 'morning';
    }
    if (time >= 9 && time < 15) {
        return 'afternoon';
    }
    if (time >= 15 && time < 21) {
        return 'evening';
    }
    if (time >= 21 || time < 3) {
        return 'night';
    }
}