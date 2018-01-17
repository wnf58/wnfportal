import { BrowserModule } from '@angular/platform-browser';
import { NgModule, LOCALE_ID } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { registerLocaleData } from '@angular/common';
import localeDE from '@angular/common/locales/de';

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

registerLocaleData(localeDE);

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
  providers: [
      {
      provide: LOCALE_ID,
      useValue: 'de' // 'de-DE' for Germany, 'fr-FR' for France ...
      },
      KubeaService, MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
