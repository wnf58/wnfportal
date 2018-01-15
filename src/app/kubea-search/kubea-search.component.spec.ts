import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KubeaSearchComponent } from './kubea-search.component';

describe('KubeaSearchComponent', () => {
  let component: KubeaSearchComponent;
  let fixture: ComponentFixture<KubeaSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KubeaSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KubeaSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
