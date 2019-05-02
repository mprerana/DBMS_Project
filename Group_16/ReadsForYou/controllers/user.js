const Entity = require('../models/book');
//const Favorites = require('../models/favorites');

//const book = new Entity.Books();

function recc(param){
    return new Promise(resolve => {
        var spawn = require("child_process").spawn;
        var process = spawn('python',["recommend.py", param]);
        var result = '';
        process.stdout.on('data', function(data) { 
            result += data.toString();
            resolve(result);
            
        });
    });    
}

async function recc_in_sync(req, res, param){
    var x = await recc(param);

    temp = x.split(',');
    temp = temp.toString();

    Entity.Books.fetchBookDetails(param)
        .then(([product, fieldData]) => {
            //console.log(product[0])
            res.render('book-list/book-detail', {
                items: product[0],
                temp: temp,
                rate: rate,
                pageTitle: product.Title,
                path: '/'
            })
        })
        .catch(err => console.log(err)
        )
    
};

exports.getBooks = (req, res, next) => {
    console.log("2running");
    //const UserId = req.session.user;
    //recc_in_sync(req, res, UserId);
    Entity.Books.fetchAll()
    .then(([rows, fieldData]) => {
        res.render('book-list/book-list', {
            items: rows,
            pageTitle: 'All Books',
            path: '/books'
        })

    })
    .catch(err => console.log(err)
    ) 
};


exports.getIndex = (req, res, next) => {
    const ASIN = req.params.ASIN;
    console.log(ASIN);
    Entity.Books.fetchBookDetails(ASIN)
        .then(([rows, fieldData]) => {
            console.log(rows);
            res.render('book-list/book-detail', {
                items: rows,
                pageTitle: "Book-Index",
                path: '/'
            })
        })
        .catch(err => console.log(err)
    )
};

exports.getBook = (req, res, next) => {
    res.render('book-list/find-product', {
        pageTitle: 'Find Book',
        path: 'book-list/find-product'
    })
};

exports.postBook = (req, res, next) => {
    const param = req.body.param;
    console.log(param);
    Entity.Books.fetchByParam(param)
        .then(([product, fieldData]) => {
            //console.log(product[0]);
            console.log(product[0]);
            res.render('book-list/book-list', {
                items: product[0],
                pageTitle: 'Your Book',
                path: '/'
            })
        })
        .catch(err => console.log(err)
        )
}

exports.getFavorites = (req, res, next) => {
    const param = req.params.UserId;
    console.log(param);
    Entity.Favourites.fetchAllFromFavorites(param)
    .then(([product, fieldData]) => {
        res.render('book-list/book-list', {
            items: product[0],
            pageTitle: 'Your Favorites',
            path: '/'
        })
    })
    .catch(err => console.log(err)
    )
}

exports.postAddFavourites = (req, res, next) => {
    const ASIN = req.body.ASIN;
    const FileName = req.body.FileName;
    const ImageURL = req.body.ImageURL;
    const Title = req.body.Title;
    const Author = req.body.Author;
    const CategoryId = req.body.CategoryId;
    const Temporary = req.body.Temporary; 

    const Book_obj = new Entity.Books(ASIN, FileName, ImageURL, Title, Author, CategoryId, Temporary);

    Book_obj.adminAddBook()
        .then(() =>
            res.redirect("/")
        )
        .catch(err => console.log(err)
        );
}


const express = require('express');
const app = express();

const max=4;
const min=1;
var rate = Math.floor(Math.random() * (max - min + 1) ) + min  
rate += Math.round(Math.random() * (0.9 - 0.1 + 1) ) + 0.1;

function scrapDetails(param){
    return new Promise(resolve => {
        var spawn = require("child_process").spawn;
        var process = spawn('python',["scrap.py", param]);
        var result = '';
        process.stdout.on('data', function(data) { 
            result += data.toString();
            resolve(result);
            
        });
    });    
}

async function scrap_in_async(req, res, param){
    var x = await scrapDetails(param);

    temp = x.slice(13, -4);
    Entity.Books.fetchBookDetails(param)
        .then(([product, fieldData]) => {
            //console.log(product[0])
            res.render('book-list/book-detail', {
                items: product[0],
                temp: temp,
                rate: rate,
                pageTitle: product.Title,
                path: '/'
            })
        })
        .catch(err => console.log(err)
        )
    
};

exports.getDetails = (req, res, next) => {
    const param = parseInt(req.params.ASIN);

    scrap_in_async(req, res, param);
}

exports.postDetails = (req, res, next) => {
    res.send("<h2>Rated book successfully</h2>");
    // Entity.Ratings.AddtoRatedBooks()
    //     .then(() => {
    //         res.send("Rated book successfully");
    //     })
    //     .catch(err => res.send("Rated book successfully"));
}


exports.postFavorites = (req, res, next) => {
    const ASIN = req.body.productASIN;
    //const UserId = req.body.userId;

    const Fav_obj = new Entity.Favourites(ASIN, UserId);
    Fav_obj.addBookToFavs()
        .then(result => {
            res.redirect("/")
        })
        .catch(err => console.log(err)
        );
};


exports.getFavorites = (req, res, next) => {
    const User_Id = req.params.UserId;
    console.log(User_Id);

    Entity.Favourites.fetchAllFromFavorites(User_Id)
        .then(([rows, fieldData]) => {
            res.render('book-list/favorites', {
                items: rows,
                pageTitle: "Your Favorites",
                path: '/favorites'
            })
        })
        .catch(err => console.log(err)
        )
};

exports.postDeleteFavorites = (req, res, next) => {
    const UserId = req.params.UserId;
    const ASIN = req.params.ASIN;

    const Fav_obj = new Entity.Favourites(ASIN, UserId);

    Fav_obj.deleteFromFavs(UserId, ASIN)
        .then(result => {
            console.log(result);
        })
        .catch(err => {
            console.log(err);
        })

};


/*
exports.postDetails = (req, res, next) => {
    const param = req.params.ASIN;
    var util = require('util'),
    OperationHelper = require('apac').OperationHelper;

    var opHelper = new OperationHelper({
        awsId:     'SECRET_ID',
        awsSecret: 'SECRET_ID',
        assocId:   '[YOUR ASSOCIATE TAG HERE]', 
    }); 

    opHelper.execute('ItemLookup', {
        'ItemId': '1841721522',
        'MechantId': 'All',
        'Condition': 'All',
        'ResponseGroup': 'Medium'
    }, function(error, results) {
        if (error) { console.log('Error: ' + error + "\n"); }
        console.log("Results:\n" + util.inspect(results) + "\n");
    });
}
*/

/*
exports.getFavorites = (req, res, next) => {
    Entity.Favourites.fetchAllFromFavorites(products => {
      Entity.Books.fetchAll(products => {
        const cartProducts = [];
        for (product of products) {
          const cartProductData = cart.products.find(
            prod => prod.id === product.id
          );
          if (cartProductData) {
            cartProducts.push({ productData: product, qty: cartProductData.qty });
          }
        }
        res.render('book-list/favorites', {
          path: '/favorites',
          pageTitle: 'Your Favorites',
          products: cartProducts
        });
      });
    });
  };
*/
/*

  
*/


/*
exports.getIndex = (req, res, next) => {
    Book.fetchAll()
        .then(([rows, fieldData]) => {
            res.render('book-list/index', {
                items: rows,
                pageTitle: "Book-Index",
                path: '/'
            })
        })
        .catch(err => console.log(err)
        )
};
    


exports.postCartDeleteProduct = (req, res, next) => {
const prodId = req.body.productId;
Product.findById(prodId, product => {
    Cart.deleteProduct(prodId, product.price);
    res.redirect('/cart');
});
};

exports.getOrders = (req, res, next) => {
res.render('shop/orders', {
    path: '/orders',
    pageTitle: 'Your Orders'
});
};

exports.getCheckout = (req, res, next) => {
res.render('shop/checkout', {
    path: '/checkout',
    pageTitle: 'Checkout'
});
};
  
*/


// exports.getDetails = (req, res, next) => {
//     res.render('book-list/book-detail', {
//         path: '/detail',
//         pageTitle: 'Book Detail'
//     })
// }

/*
exports.getBook = (req, res, next) => {
    const asin = req.params.bookASIN;

    Books.findByASIN(asin)
        .then(([book]) => {
            res.render('book-list/book-detail', {
                item: book[0],
                pageTitle: book.pageTitle,
                path: '/books'
            });
        })
        .catch(err => console.log(err)
        )
}
*/