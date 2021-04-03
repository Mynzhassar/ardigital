import { TestBed } from '@angular/core/testing';

import { ProfitService } from './profit.service';

describe('ServicesService', () => {
  let service: ProfitService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProfitService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
