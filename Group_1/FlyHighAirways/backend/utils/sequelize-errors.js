const uniqueConstraintError = (err) =>{

    const errorMessages = {};
    for (field in err.fields){
        errorMessages[field] = `${field} ${err.fields[field]} already exists`;
    }

    return errorMessages
};


const handleSequelizeErrors = (err)=>{
  switch (err.name) {
      case "SequelizeUniqueConstraintError": return uniqueConstraintError(err);
      default: throw err;
  }
};
module.exports = handleSequelizeErrors;

