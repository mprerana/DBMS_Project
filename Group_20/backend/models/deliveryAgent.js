var self = this;

self.updateLocation = function(agent_username, lat, lon){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `UPDATE deliveryAgent
                    SET lat = $2,
                        lon = $3
                    WHERE  username = $1
                    returning *`,
            values: [agent_username, lat, lon],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

module.exports = self;
