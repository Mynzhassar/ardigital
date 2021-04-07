import {Component, OnInit} from '@angular/core';
import {Consultation} from "../../models/models";
import {ProviderService} from "../../services/provider.service";

@Component({
  selector: 'app-consultation',
  templateUrl: './consultation.component.html',
  styleUrls: ['./consultation.component.css']
})
export class ConsultationComponent implements OnInit {
  public consultations !: Consultation[]

  constructor(private provider: ProviderService) {
  }

  ngOnInit(): void {
  }

}
