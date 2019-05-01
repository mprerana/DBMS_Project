tasks = [
    {
        name:'remove_expired_tokens',
        procedureName:'remove_expired_outstanding_tokens',
        procedure:require('./remove_expired_outstanding_tokens'),
        timeDelta:'1 day',
        description:'Removes old outstanding tokens that are either expired or invalid'
    }
];

module.exports = tasks;