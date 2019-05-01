const wrapField = (fieldName) => `"${fieldName}"`;

const wrapValue = (value) =>{
    if (!value) return null;
    if (typeof(value)!='string'){
        throw new TypeError("Attempted to wrap non string value into db string.")
    }

    if (value[0]==='['){
        // array. dont wrap
        return `ARRAY ${value}`
    }
    return `'${value}'`
};

const wrapAllValues = (valueObject) => {

    Object.keys(valueObject).map((key)=>{
        valueObject[key] = wrapValue(valueObject[key]);
    });

    return valueObject;
};


module.exports = {
    wrapField:wrapField,
    wrapValue:wrapValue,
    wrapAllValues:wrapAllValues
};