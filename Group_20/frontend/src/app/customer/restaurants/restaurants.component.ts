import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { UserService,AuthenticationService } from '@/_services';

import { RestaurantProfile } from '@/_models';

@Component({
  selector: 'app-restaurants',
  templateUrl: './restaurants.component.html',
  styleUrls: ['./restaurants.component.css',
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
export class RestaurantsComponent implements OnInit {
  restaurants: RestaurantProfile;

  constructor(
  private userService: UserService,
  private authenticationService: AuthenticationService,
  private router: Router,

  ) { 
    
  }

  ngOnInit() {
    this.getRestaurants();

  }
  getRestaurants(): void {
    this.userService.getRestaurantProfiles()
      .subscribe(restaurants => {
        this.restaurants = restaurants
      });
  }

  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
  }
}
