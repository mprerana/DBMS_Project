import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RestaurantApplicationsComponent } from './restaurant-applications.component';

describe('RestaurantApplicationsComponent', () => {
  let component: RestaurantApplicationsComponent;
  let fixture: ComponentFixture<RestaurantApplicationsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RestaurantApplicationsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RestaurantApplicationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
