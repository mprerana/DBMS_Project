module.exports = (errorData) => {

    const errorArray = [];
    Object.keys(errorData).map(key=>{
        errorArray.push({
            "param":key,
            "msg": errorData[key]
        })
    });

    return errorArray;
};