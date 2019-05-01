import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';


import { AuthenticationService } from '@/_services';
import * as customValidators from '@/custom-validators';

declare var ol: any;

@Component({
  selector: 'app-restaurant-register',
  templateUrl: './restaurant-register.component.html',
  styleUrls: ['./restaurant-register.component.css']
})
export class RestaurantRegisterComponent implements OnInit {
  restaurantRegisterForm: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: string;
  error = '';
  map: any;

  constructor(

      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private router: Router,
      private authenticationService: AuthenticationService,
      private http: HttpClient
  ) { 
  }

  ngOnInit() {
    
    this.restaurantRegisterForm = this.formBuilder.group({
      restaurantName: ['', [Validators.required,customValidators.resnameValidator()]],
      email: ['',[Validators.required,customValidators.emailValidator()]],
      lat: ['',Validators.required],
      lon: ['',Validators.required],
      zipcode: ['',[Validators.required,customValidators.zipcodeValidator()]],
      phone: ['',[Validators.required,customValidators.phoneValidator()]],
      address: ['',[Validators.required,customValidators.addressValidator()]],
      logo: ['',Validators.required],
      openingHrs: ['',[Validators.required,customValidators.timeValidator()]],
      closingHrs: ['',[Validators.required,customValidators.timeValidator()]],
  });

    this.map = new ol.Map({
      target: 'map',
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM()
        }),
      ],
      view: new ol.View({
        center: ol.proj.fromLonLat([80.2707, 13.0827]),
        zoom: 8
      })
    });
    var vectorSource = null;
    this.map.on('click', (args) => {
      var lonlat = ol.proj.transform(args.coordinate, 'EPSG:3857', 'EPSG:4326');
      if (vectorSource){
        vectorSource.clear()
      }
      var marker = new ol.Feature({
        geometry: new ol.geom.Point(
          ol.proj.fromLonLat(lonlat)
        ),  // Cordinates of New York's Town Hall
      });
      vectorSource = new ol.source.Vector({
        features: [marker]
      });
      var markerVectorLayer = new ol.layer.Vector({
        source: vectorSource,
      });
      this.map.addLayer(markerVectorLayer);
      this.restaurantRegisterForm.controls['lon'].setValue(lonlat[1].toString());
      this.restaurantRegisterForm.controls['lat'].setValue(lonlat[0].toString());
      this.getZipcode(lonlat[1],lonlat[0])
    });
    
    
    
    // get return url from route parameters or default to '/'
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/home';
  }
  // convenience getter for easy access to form fields
  get f() { return this.restaurantRegisterForm.controls; }


  onFileChange(event) {
    let reader = new FileReader();
   
    if(event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);
    
      reader.onload = () => {
        this.restaurantRegisterForm.patchValue({
          logo: reader.result.toString()
        })
      };
    }
  }

  getZipcode(lat,lon){
    this.http.get(`http://api.geonames.org/findNearbyPostalCodesJSON?lat=${lat}&lng=${lon}&username=thehanimo`)
    .subscribe(
        data => {
          this.restaurantRegisterForm.controls['zipcode'].setValue(data['postalCodes'][0]['postalCode']);
        })
  }
  onSubmit() {
    this.submitted = true;
    var email = this.f.email.value;
    if (this.restaurantRegisterForm.invalid) {
        return;
    }
    this.http.post(`http://localhost:3000/api/email`, {email})
    .pipe(first())
    .subscribe(
        data2 => {
            if (data2){
                this.loading = true;
                this.authenticationService.restaurantRegister(this.f.restaurantName.value, this.f.email.value, this.f.lat.value,this.f.lon.value, this.f.address.value, this.f.zipcode.value, this.f.phone.value, this.f.openingHrs.value, this.f.closingHrs.value, this.f.logo.value)
                .pipe(first())
                .subscribe(
                    data => {
                        this.router.navigate([this.returnUrl]);
                    },
                    error => {
                        this.error = error;
                        this.loading = false;
                    });
            } else {
                this.f.email.setErrors({'emailtakenValidator': true})
                return;
            }
        }
    ) 
  }
}
