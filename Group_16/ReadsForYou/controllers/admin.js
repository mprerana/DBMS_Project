const Admin = require('../models/admin');
const Entity = require('../models/book');

exports.verifyAdmin = (req, res, next) => {
    Admin.verifyByToken()
        .then()
        .catch()
};


exports.getAddBook = (req, res, next) => {
    res.render('admin/edit-product', {
        pageTitle: 'Add Product',
        path: '/admin/add-product',
        editing: false,
        editing: false,
        hasError: false,
        errorMessage: null
      });
};


exports.postAddBook = (req, res, next) => {
    const ASIN = req.body.ASIN;
    const FileName = req.body.FileName;
    const ImageURL = req.body.ImageURL;
    const Title = req.body.Title;
    const Author = req.body.Author;
    const CategoryId = req.body.CategoryId;
    const Temporary = req.body.Temporary; 

    const Book_obj = new Entity.Books(ASIN, FileName, ImageURL, Title, Author, CategoryId, Temporary);


      // Validation added here
    const errors = validationResult(req);
    if(!errors.isEmpty()) {
        console.log(errors.array());
        res.status(422).render('admin/edit-product', {
        pageTitle: 'Add Product',
        path: '/admin/edit-product',
        //editing: editMode,  Starting with  Not editing yet
        editing: false,
        hasError: false,       
        product: {
            ASIN: ASIN,
            FileName: FileName,
            ImageUrl: ImageURL,
            Title: Title,
            Author: Author,
            Description: Description
        },
        errorMessage: errors.array()[0].msg,
        });


    Book_obj.adminAddBook()
        .then(() =>
            res.redirect("/")
        )
        .catch(err => console.log(err)
        );
}}

exports.getEditBook = (req, res, next) => {
    // const param = req.body.param;
    // Entity.Books.fetchByParam(param)
    //     .then(result => 
    //         res.render('admin/edit-product', {
    //             pageTitle: "Edit Product",
    //             path: "/",
    //             editing: true
    //         }))
    //     .catch(err => console.log(err)
    //     )

    const editMode = req.query.edit;
    if(!editMode){
        return res.redirect('/');
    }
    const prodASIN = req.body.param;
    Product.findByASIN(prodASIN)
    .then(product => {
        if(!product) {
        return res.redirect('/');
        }
        res.render('admin/edit-product', {
        pageTitle: 'Edit Product',
        path: '/admin/edit-product',
        editing: editMode,    
        product: product,
        editing: false, 
        hasError: false,
        errorMessage: null     
        });
    }) 
    .catch(err => console.log(err))
}

exports.postEditBook = (req, res, next) => {
    const ASIN = req.body.ASIN;
    const FileName = req.body.FileName;
    const ImageURL = req.body.ImageURL;
    const Title = req.body.Title;
    const Author = req.body.Author;
    const CategoryId = req.body.CategoryId;
    //const Temporary = req.body.Temporary; 
    
    // Validation added here
    const errors = validationResult(req);
    if(!errors.isEmpty()) {
        res.status(422).render('admin/edit-book', {
            prods: products,
            pageTitle: 'Edit Book',
            path: '/admin/edit-book'
        });
    }
    const editedProduct = new Entity.Books(ASIN, FileName,
        ImageURL, Title, Author, CategoryId, Temporary);
    
    editedProduct.adminEditBook();
    res.redirect('/admin/edit-book');
};

exports.getProducts = (req, res, next) => {
    Product.fetchAll(products => {
      res.render('admin/products', {
        prods: products,
        pageTitle: 'Admin Products',
        path: '/admin/products'
      });
    });
  };
  
  exports.postDeleteProduct = (req, res, next) => {
    const prodASIN = req.body.productASIN;
    Product.deleteByASIN(prodASIN);
    res.redirect('/admin/products');
  };

