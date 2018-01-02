import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { KubeaComponent } from './kubea/kubea.component';
import { KubeaService } from './kubea.service';
import { MessageService } from './message.service';


@NgModule({
  declarations: [
    AppComponent,
    KubeaComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [KubeaService, MessageService],
  bootstrap: [AppComponent]
})
export class AppModule { }
