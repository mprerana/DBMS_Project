var self = this;

self.trackOrder = function(order_id){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select lat, lon from tracking where orderId = $1`,
            values: [order_id],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

module.exports = self;
