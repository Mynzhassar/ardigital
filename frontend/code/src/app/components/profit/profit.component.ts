import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs';

import {ProfitService} from '../../services/profit/profit.service';
import {Profit} from '../../models/models';

@Component({
  selector: 'app-profit',
  templateUrl: './profit.component.html',
  styleUrls: ['./profit.component.css']
})

export class ProfitComponent implements OnInit {
  profits$ !: Observable<Profit[]>;

  constructor(private profitService: ProfitService) {
  }

  ngOnInit() {
    this.getProfits();
  }

  public getProfits() {
    this.profits$ = this.profitService.getProfits();
  }

}
