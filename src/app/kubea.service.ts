import { Injectable } from '@angular/core';

import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';

import { KubeaRecord, KUBEADEMO } from './kubea_const';
import { MessageService } from './message.service';

@Injectable()
export class KubeaService {

  constructor(private messageService: MessageService) { }

  getKubEA(): Observable<KubeaRecord[]> {
    // Todo: send the message _after_ fetching the heroes
    this.messageService.add('KubeaService: fetched kubea');
    return of(KUBEADEMO);
  }
}
