import { TestBed, inject } from '@angular/core/testing';

import { KubeaService } from './kubea.service';

describe('KubeaService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [KubeaService]
    });
  });

  it('should be created', inject([KubeaService], (service: KubeaService) => {
    expect(service).toBeTruthy();
  }));
});
