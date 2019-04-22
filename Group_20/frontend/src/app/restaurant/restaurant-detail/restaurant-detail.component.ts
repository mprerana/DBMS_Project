import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { MenuItems } from '@/_models';

import { UserService } from '@/_services';

@Component({
  selector: 'app-restaurant-detail',
  templateUrl: './restaurant-detail.component.html',
  styleUrls: ['./restaurant-detail.component.css']
})
export class RestaurantDetailComponent implements OnInit {

  items: MenuItems;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private userService: UserService,
  ) { }

  ngOnInit() {
    this.getRestaurantItems();
  }

  getRestaurantItems(): void {
    const id = this.route.snapshot.paramMap.get('resname');
    this.userService.getRestaurantItems(id)
      .subscribe(items => this.items = items);
  }

}
