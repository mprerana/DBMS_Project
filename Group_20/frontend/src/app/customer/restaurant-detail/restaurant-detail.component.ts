
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { Cart } from './cart';
import { MenuItems, User, Order } from '@/_models';

import { UserService, AuthenticationService } from '@/_services';

import { first } from 'rxjs/operators';

@Component({
  selector: 'app-restaurant-detail',
  templateUrl: './restaurant-detail.component.html',
  styleUrls: ['./restaurant-detail.component.css',
              '../assets/css/open-iconic-bootstrap.min.css',
              "../assets/css/animate.css",
              // "./assets/css/owl.carousel.min.css",
              "../assets/css/owl.theme.default.min.css",
              "../assets/css/magnific-popup.css",
              "../assets/css/aos.css",
              "../assets/css/ionicons.min.css",
              "../assets/css/bootstrap-datepicker.css",
              "../assets/css/jquery.timepicker.css",
              "../assets/css/flaticon.css",
              "../assets/css/icomoon.css",
              "../assets/css/style.css"
]
})
export class RestaurantDetailComponent implements OnInit {
  items: MenuItems;
  cart: Cart [] = [];
  currentUser: User;
  loading = false;
  error = '';
  order: Order;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private userService: UserService,
    private authenticationService: AuthenticationService,
  ) { 
    this.currentUser = this.authenticationService.currentUserValue;
  }

  ngOnInit() {
    this.getRestaurantItems();
    this.getLastOrder();
  }

  getRestaurantItems(): void {
    const id = this.route.snapshot.paramMap.get('resname');
    this.userService.getRestaurantItems(id)
      .subscribe(items => this.items = items);
  }

  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
  }
  initialiseCart(id, op): void {
    var i = 0;
    for (var item in this.items) {
      if(!this.cart[i])
      {
        this.cart[i] = {itemid: this.items[item].id, quantity: 0}; 
      }
      if(this.items[i].id === id)
      {
        if(op)
          this.cart[i].quantity += 1;
        else
          if(this.cart[i].quantity != 0)
            this.cart[i].quantity -= 1;
      }
      i++;
    }
  }

  addToCart(id, op): void {
    this.initialiseCart(id, op);
    console.log(this.cart);
  }

  getLastOrder(): void {
    this.userService.getLastOrder()
      .subscribe(order => this.order = order);
  }

  createOrder(): void {
    console.log("Hi");
    
    if(this.order[0] !== undefined){
      var orderid = this.order[0].id + 1 ;
    } else {
      var orderid = 1 ;
    }
    console.log(orderid);
    this.userService.createOrder(orderid, this.currentUser.username, 'restaurant19', '13.591471582246442', '80.03223359606993', 'Mira')
    .pipe(first())
    .subscribe(
      data => {
        this.router.navigate(['../user/landing']);
    },
    error => {
        this.error = error;
        this.loading = false;
    });
    var i = 0;
    for (var item in this.cart){
      if(this.cart[i].quantity != 0)
      {
        this.userService.addOrderItems(orderid, this.cart[i].itemid, this.cart[i].quantity)
        .pipe(first())
        .subscribe(
          data => {},
          error => {
            this.error = error;
            this.loading = false;
          });
          this.cart[i].quantity = 0;
          i++;
      }
    }
  }
}
