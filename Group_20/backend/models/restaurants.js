var self = this;

self.restaurantApply = function(name, email, lon, lat, address, zipcode, phone, openingHrs, closingHrs, logourl){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `insert into restaurantApplications(name,email,lon,lat,address,zipcode,phone,openingHrs,closingHrs,logourl)
                    values ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10) returning *`,
            values: [name,email,lon,lat,address,zipcode,phone,openingHrs,closingHrs,logourl],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.getRestaurantApplicationByEmail = function(email){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from restaurantApplications
                    where email = $1`,
            values: [email],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0]);
        })
        .catch(e => reject(e))
    });
}

self.getRestaurantApplications = function(){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select name,email,phone,zipcode,id from restaurantApplications`
        }
        client.query(query)
        .then(res => {
            resolve(res.rows)
        })
        .catch(e => reject(e))
    });
}

self.getRestaurantApplicationByID = function(id){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from restaurantApplications
                    where id = $1`,
            values: [id],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.updateRestaurantApplication = function(email, status){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `update restaurantApplications
                    set status = $1 where email = $2 returning *`,
            values: [status,email],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.getRestaurantProfiles = function() {
    client = this;
    return new Promise(function(resolve, reject){
        const query = {
            text:   `select * from restaurantProfile limit 15`
        }
        client.query(query)
        .then(res => {
            resolve(res.rows)
        })
        .catch(e => reject(e))
    });
}
          
self.getRestaurantCategory = function(username, catName){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from category
                    where rest_username = $1 and categoryName = $2`,
            values: [username,catName],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.getRestaurantItems = function(id) {
    client = this;
    return new Promise( function(resolve, reject){
        const query = {
            text:   `select * from item where restid='${id}'`
          
        }
        client.query(query)
        .then(res => {
            resolve(res.rows)
        })
        .catch(e => reject(e))
    });
}

self.addRestaurantCategory = function(username, catName){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `insert into category(rest_username,categoryName)
                    values($1,$2) returning *`,
            values: [username,catName],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.getRestaurantCategories = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select id,categoryName from category
                    where rest_username = $1`,
            values: [username],
          
        }
        client.query(query)
        .then(res => {
            resolve(res.rows)
        })
        .catch(e => reject(e))
    });
}

self.getRestaurantItem = function(username, itemName){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from item
                    where restId = $1 and itemName = $2`,
            values: [username,itemName],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.addRestaurantItem = function(username, itemName,price,desc,catID,pictureurl){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `insert into item(restId,itemName,price,description,photoUrl,categoryId)
                    values($1,$2,$3,$4,$5,$6) returning *`,
            values: [username,itemName,price,desc,pictureurl,catID],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.addOrderItem = function(orderID, itemID, quantity){
    client = this;
    return new Promise(function(resolve, reject){
        const query = {
            text:   `insert into orderitem(orderid, itemid, quantity)
                    values($1,$2,$3) returning *`,
            values: [orderID, itemID, quantity],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.createOrder = function(orderID, username, restname, lat, lon, deliveryname){
    client = this;
    return new Promise(function(resolve, reject){
        const query = {
            text:   `insert into orders(id, username, rest_name, lat, lon, del_username)
                    values($1,$2,$3,$4,$5,$6) returning *`,
            values: [orderID, username, restname, lat, lon, deliveryname],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.getLastOrder = function(){
    client = this;
    return new Promise(function(resolve, reject){
        const query = {
            text:   `select * from orders ORDER BY id DESC LIMIT 1`,
        }
        client.query(query)
        .then(res => {
            resolve(res.rows)
        })
        .catch(e => reject(e))
    });
}

module.exports = self;