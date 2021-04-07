import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs';

import {ProviderService} from '../../services/provider.service';
import {Profit} from '../../models/models';

@Component({
  selector: 'app-profit',
  templateUrl: './profit.component.html',
  styleUrls: ['./profit.component.css']
})

export class ProfitComponent implements OnInit {
  profits$ !: Observable<Profit[]>;

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.getProfits();
  }

  public getProfits() {
    this.profits$ = this.provider.getProfits();
  }

}
