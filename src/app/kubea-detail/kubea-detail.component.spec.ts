import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KubeaDetailComponent } from './kubea-detail.component';

describe('KubeaDetailComponent', () => {
  let component: KubeaDetailComponent;
  let fixture: ComponentFixture<KubeaDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KubeaDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KubeaDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
