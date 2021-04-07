import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProfitComponent } from './components/profit/profit.component';
import { ServiceComponent } from './components/service/service.component';
import { ConsultationComponent } from './components/consultation/consultation.component';

@NgModule({
  declarations: [
    AppComponent,
    ProfitComponent,
    ServiceComponent,
    ConsultationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
