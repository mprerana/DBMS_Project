import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SingleRestoApplicationComponent } from './single-resto-application.component';

describe('SingleRestoApplicationComponent', () => {
  let component: SingleRestoApplicationComponent;
  let fixture: ComponentFixture<SingleRestoApplicationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SingleRestoApplicationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SingleRestoApplicationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
