import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';
import { Router,ActivatedRoute } from '@angular/router';


import { AdminService,AuthenticationService } from '@/_services';
import { defineBase } from '@angular/core/src/render3';

declare var ol: any;


@Component({
  selector: 'app-single-resto-application',
  templateUrl: './single-resto-application.component.html',
  styleUrls: ['../assets/css/bootstrap.min.css',
              '../assets/css/now-ui-dashboard.css?v=1.3.0',
              '../assets/demo/demo.css',
              './single-resto-application.component.css'
            ]
})
export class SingleRestoApplicationComponent implements OnInit {
  restaurant: any = '';
  map: any;

  constructor(
    private adminService: AdminService,
    private route: ActivatedRoute,
    private router: Router,
    private authenticationService: AuthenticationService
  ) {

    
   }

  ngOnInit() {
    this.adminService.getRestaurantApplicationByID(this.route.snapshot.params['id']).pipe(first()).subscribe(restaurant => {
      this.restaurant = restaurant;
      this.map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([parseFloat(this.restaurant.lon), parseFloat(this.restaurant.lat)]),
          zoom: 14
        })
      });
      var marker = new ol.Feature({
        geometry: new ol.geom.Point(
          ol.proj.fromLonLat([parseFloat(this.restaurant.lon), parseFloat(this.restaurant.lat)])
        ),  // Cordinates of New York's Town Hall
      });
      var vectorSource = new ol.source.Vector({
        features: [marker]
      });
      var markerVectorLayer = new ol.layer.Vector({
        source: vectorSource,
      });
      this.map.addLayer(markerVectorLayer);
    })
    
  }
  verifyAppl(email){
    this.adminService.updateRestaurantApplication(email, 'A').pipe(first()).subscribe(done => {
    });
    this.router.navigate(['../restaurantApplications'])
  }
  rejectAppl(email){
    this.adminService.updateRestaurantApplication(email, 'R').pipe(first()).subscribe(done => {
    });
    this.router.navigate(['../restaurantApplications'])
  }
  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
    
  }

}
