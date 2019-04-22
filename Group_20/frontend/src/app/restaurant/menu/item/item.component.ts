import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';


import { AuthenticationService } from '@/_services';
import * as customValidators from '@/custom-validators';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css',
  '../../../admin/assets/css/bootstrap.min.css',
  '../../../admin/assets/css/now-ui-dashboard.css?v=1.3.0',
  '../../../admin/assets/demo/demo.css',                
]
})
export class ItemComponent implements OnInit {
  addItemForm: FormGroup;
  categories: Object;
  loading = false;
  submitted = false;
  returnUrl: string;
  error = '';
  

  constructor(
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private router: Router,
      private authenticationService: AuthenticationService,
      private http: HttpClient
  ) { 
  }

  ngOnInit() {
      this.addItemForm = this.formBuilder.group({
          name: ['', [Validators.required,customValidators.nameValidator()]],
          price: ['', [Validators.required,customValidators.priceValidator()]],
          description: ['', [Validators.required,customValidators.descriptionValidator()]],
          category: ['', [Validators.required]],
          photo: ['', [Validators.required]],
      });
      
      // get return url from route parameters or default to '/'
      this.returnUrl = '/restaurant/menu';

      this.http.get(`http://localhost:3000/restaurant/categories`)
      .pipe(first())
          .subscribe(
              data => {
                  if (data){
                    this.categories = data;
                    return;
                  }
              },
              error => {
                  this.error = error;
                  this.loading = false;
                  return;
              }
          );
  }

  // convenience getter for easy access to form fields
  get f() { return this.addItemForm.controls; }

  onFileChange(event) {
    let reader = new FileReader();
   
    if(event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);
    
      reader.onload = () => {
        this.addItemForm.patchValue({
          photo: reader.result.toString()
        })
      };
    }
  }

  onSubmit() {
      this.submitted = true;
      if (this.addItemForm.invalid) {
          return;
      }
      var itemName = this.f.name.value;
      var price = this.f.price.value;
      var desc = this.f.description.value;
      var categoryID = this.f.category.value;
      var photo = this.f.photo.value;
      this.http.post(`http://localhost:3000/restaurant/addItem`, {itemName,price,desc,categoryID,photo})
      .pipe(first())
        .subscribe(
          data => {
              if (data){
                this.router.navigate([this.returnUrl]);
                return;
              } else { 
                this.f.name.setErrors({'nametakenValidator': true})
                return;
              }
          },
          error => {
              this.error = error;
              this.loading = false;
              return;
          }
      );
    }

}
