import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { first } from 'rxjs/operators';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { User } from '@/_models';
import { UserService, AuthenticationService } from '@/_services';
import * as customValidators from '@/custom-validators';

@Component({ templateUrl: 'profile.component.html' })
export class ProfileComponent {
    profileForm: FormGroup;
    loading = false;
    submitted = false;
    returnUrl: string;
    error = '';
    picture = '';
    currentUser: User;

    constructor(
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private router: Router,
        private userService: UserService,
        private authenticationService: AuthenticationService,
    ) {
        this.currentUser = this.authenticationService.currentUserValue;
    }

    ngOnInit() {
        this.profileForm = this.formBuilder.group({
            firstname: ['', [Validators.required,customValidators.nameValidator()]],
            lastname: ['', [Validators.required,customValidators.nameValidator()]],
            phone: ['',[Validators.required,customValidators.phoneValidator()]],
            address: ['',Validators.required],
            picture: [this.picture]
        });
        this.userService.getUserProfile().pipe(first()).subscribe(user => {
            this.profileForm.controls['firstname'].setValue(user.firstname);
            this.profileForm.controls['lastname'].setValue(user.lastname);
            this.profileForm.controls['phone'].setValue(user.phone);
            this.profileForm.controls['address'].setValue(user.address);
            this.picture = user.picture;
            
        });
        

        // get return url from route parameters or default to '/'
        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
    }
    // convenience getter for easy access to form fields
    get f() { return this.profileForm.controls; }
    
    onFileChange(event) {
        let reader = new FileReader();
       
        if(event.target.files && event.target.files.length) {
          const [file] = event.target.files;
          reader.readAsDataURL(file);
        
          reader.onload = () => {
            this.profileForm.patchValue({
              picture: reader.result.toString()
            })
            this.picture = reader.result.toString();
          };
        }
    }

    onSubmit() {
        this.submitted = true;

        // stop here if form is invalid
        if (this.profileForm.invalid) {
            return;
        }

        this.loading = true;
        this.userService.updateUserProfile(this.currentUser.username, {
                                                                        firstname: this.f.firstname.value,
                                                                        lastname: this.f.lastname.value,
                                                                        phone: this.f.phone.value,
                                                                        address: this.f.address.value,
                                                                        picture: this.picture
                                                                    })
            .pipe(first())
            .subscribe(
                data => {
                    this.router.navigate([this.returnUrl]);
                },
                error => {
                    this.error = error;
                    this.loading = false;
                });
    }
}