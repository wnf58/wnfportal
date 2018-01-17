import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { KubeaComponent } from './kubea/kubea.component';
import { KubeaService } from './kubea.service';
import { MessageService } from './message.service';
import { KubeaDetailComponent } from './kubea-detail/kubea-detail.component';
import { AppRoutingModule } from './/app-routing.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MessagesComponent }    from './messages/messages.component';
import { KubeaSearchComponent } from './kubea-search/kubea-search.component';
import { KontostandComponent } from './kontostand/kontostand.component';


@NgModule({
  declarations: [
    AppComponent,
    KubeaComponent,
    KubeaDetailComponent,
    DashboardComponent,
    MessagesComponent,
    KubeaSearchComponent,
    KontostandComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [KubeaService, MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
