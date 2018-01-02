import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KubeaComponent } from './kubea.component';

describe('KubeaComponent', () => {
  let component: KubeaComponent;
  let fixture: ComponentFixture<KubeaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KubeaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KubeaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
