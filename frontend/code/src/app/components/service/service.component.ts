import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs';

import {ProviderService} from '../../services/provider.service';
import {Service} from '../../models/models';

@Component({
  selector: 'app-service',
  templateUrl: './service.component.html',
  styleUrls: ['./service.component.css']
})

export class ServiceComponent implements OnInit {
  services$ !: Observable<Service[]>;

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.getServices();
  }

  public getServices() {
    this.services$ = this.provider.getServices();
  }

}
