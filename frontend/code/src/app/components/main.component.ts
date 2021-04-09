import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Profit, Service} from '../models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {

  public profits: Profit[] = [];
  public services: Service[] = [];

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.getProfits();
    this.getServices();
  }

  public getProfits() {
    this.provider.getProfits().then(res => {
      this.profits = res
    })
  }

  public getServices() {
    this.provider.getServices().then(res => {
      this.services = res
    })
  }

}
