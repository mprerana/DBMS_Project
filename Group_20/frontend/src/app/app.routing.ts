import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './landing/login';
import { RegisterComponent } from './landing/register';
import { CustomerComponent } from './customer';
import { LandingComponent } from './landing';
import { AuthGuard } from './_guards';
import { VerificationComponent } from './landing/verification';
import { ChangePasswordComponent } from './customer/change-password';
import { ProfileComponent } from './customer/profile';
import { ForgotPasswordComponent } from './landing/forgot-password';
import { UserLandingComponent } from './customer/user-landing';
import { RestaurantDetailComponent } from './customer/restaurant-detail';

import { AdminComponent } from './admin'
import { RestaurantApplicationsComponent } from './admin/restaurant-applications'
import { Role } from './_models';
import { from } from 'rxjs';
import { RestaurantRegisterComponent } from './landing/restaurant-register';
import { SingleRestoApplicationComponent } from './admin/single-resto-application/single-resto-application.component';
import { RestaurantComponent } from './restaurant/restaurant.component';
import { ChangePasswordComponent as RChangePasswordComponent} from './restaurant/change-password/change-password.component'
import { MenuComponent } from './restaurant/menu/menu.component';
import { CategoryComponent } from './restaurant/menu/category/category.component';
import { ItemComponent } from './restaurant/menu/item/item.component';
import { RestaurantsComponent } from './customer/restaurants/restaurants.component';


const appRoutes: Routes = [
    {
        path: 'home',
        component: CustomerComponent,
        children: [
            {path:'',redirectTo: 'landing',pathMatch: 'full'},
            {path: 'changePassword', component: ChangePasswordComponent},
            {path: 'profile', component: ProfileComponent},
            {path: 'landing', component: UserLandingComponent},
            {path: 'restaurants', component: RestaurantsComponent},
            {path: 'restaurant/:resname', component: RestaurantDetailComponent},
        ],
        canActivate: [AuthGuard],
        data: { roles: ['1'] },

    },
    {
        path: '',
        component: LandingComponent,
        children: [
            {path:'login',component:LoginComponent},
            {path:'register',component: RegisterComponent},
            {path:'confirmation/:token',component:VerificationComponent},
            {path:'iforgot',component:ForgotPasswordComponent},
            {path:'restaurant-register',component:RestaurantRegisterComponent}
        ]
    },
    {
        path: 'admin',
        component: AdminComponent,
        canActivate: [AuthGuard],
        children: [
            {path: 'restaurantApplications', component: RestaurantApplicationsComponent},
            {path: 'restaurantApplication/:id', component: SingleRestoApplicationComponent},
        ],
        data: { roles: ['2'] },
    },
    {
        path: 'restaurant',
        component: RestaurantComponent,
        canActivate: [AuthGuard],
        children: [
            {path: 'changePassword', component: RChangePasswordComponent},
            {path: 'menu',
            component: MenuComponent,
            children: [
                {path: 'category', component: CategoryComponent},
                {path: 'item', component: ItemComponent},
            ]
            },
        ],
        data: { roles: ['3'] },
    },
    // otherwise redirect to landing page
    { path: '**', redirectTo: '' }
];

export const routing = RouterModule.forRoot(appRoutes);