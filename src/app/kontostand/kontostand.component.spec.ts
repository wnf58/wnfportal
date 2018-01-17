import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KontostandComponent } from './kontostand.component';

describe('KontostandComponent', () => {
  let component: KontostandComponent;
  let fixture: ComponentFixture<KontostandComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KontostandComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KontostandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
