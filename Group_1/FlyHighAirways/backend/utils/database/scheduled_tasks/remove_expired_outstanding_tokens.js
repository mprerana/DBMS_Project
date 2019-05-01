outstandingToken = require('../../../models/auth/token');

exports.declarations = `
                        `;

exports.statements = `
                      DELETE FROM 
                      ${outstandingToken.getTableName()}
                      WHERE 
                        is_valid is FALSE OR
                        expires_on < NOW();
                     `;