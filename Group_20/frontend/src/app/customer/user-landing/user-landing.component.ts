import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { UserService } from '@/_services';

import { RestaurantProfile } from '@/_models';

@Component({
  selector: 'app-landing',
  templateUrl: './user-landing.component.html',
  styleUrls: ['./user-landing.component.css']
})
export class UserLandingComponent implements OnInit {

  returnUrl: string;
  error = '';
  restaurants: RestaurantProfile;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private userService: UserService,
  ) { }

  ngOnInit() {
    this.getRestaurants();
  }

  getRestaurants(): void {
    this.userService.getRestaurantProfiles()
      .subscribe(restaurants => {
        this.restaurants = restaurants
        console.log(this.restaurants)
      });
  }
}
