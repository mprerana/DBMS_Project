import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';


import { AppComponent } from './app.component';
import { routing } from './app.routing';

import { JwtInterceptor, ErrorInterceptor } from './_helpers';

import { AppRoutingModule } from './app-routing.module';
import { LoginComponent } from './landing/login/login.component';
import { CustomerComponent } from './customer';
import { LandingComponent } from './landing/landing.component';
import { RegisterComponent } from './landing/register/register.component';
import { VerificationComponent } from './landing/verification/verification.component';
import { ChangePasswordComponent } from './customer/change-password/change-password.component';
import { ProfileComponent } from './customer/profile/profile.component';
import { ForgotPasswordComponent } from './landing/forgot-password/forgot-password.component';
import { RestaurantRegisterComponent } from './landing/restaurant-register/restaurant-register.component';
import { AdminComponent } from './admin/admin.component';
import { RestaurantApplicationsComponent } from './admin/restaurant-applications/restaurant-applications.component';
import { SingleRestoApplicationComponent } from './admin/single-resto-application/single-resto-application.component';
import { RestaurantComponent } from './restaurant/restaurant.component';
import { ChangePasswordComponent as RChangePasswordComponent} from './restaurant/change-password/change-password.component'
import { UserLandingComponent } from './customer/user-landing';
import { RestaurantDetailComponent } from './restaurant/restaurant-detail/restaurant-detail.component';
import { MenuComponent } from './restaurant/menu/menu.component';
import { CategoryComponent } from './restaurant/menu/category/category.component';
import { ItemComponent } from './restaurant/menu/item/item.component'

@NgModule({
  imports: [
  BrowserModule,
  ReactiveFormsModule,
  HttpClientModule,
  routing,
  NgbModule,
  ],
  declarations: [
    AppComponent,
    LoginComponent,
    CustomerComponent,
    LandingComponent,
    RegisterComponent,
    VerificationComponent,
    ChangePasswordComponent,
    ProfileComponent,
    ForgotPasswordComponent,
    RestaurantRegisterComponent,
    AdminComponent,
    RestaurantApplicationsComponent,
    SingleRestoApplicationComponent,
    RestaurantComponent,
    RChangePasswordComponent,
    UserLandingComponent,
    RestaurantDetailComponent,
    MenuComponent,
    CategoryComponent,
    ItemComponent,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
