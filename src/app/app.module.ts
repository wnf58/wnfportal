import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { KubeaComponent } from './kubea/kubea.component';
import { KubeaService } from './kubea.service';
import { MessageService } from './message.service';
import { KubeaDetailComponent } from './kubea-detail/kubea-detail.component';


@NgModule({
  declarations: [
    AppComponent,
    KubeaComponent,
    KubeaDetailComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [KubeaService, MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
