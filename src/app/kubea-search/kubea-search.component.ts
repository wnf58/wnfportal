import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs/Observable';
import { Subject }    from 'rxjs/Subject';
import { of }         from 'rxjs/observable/of';

import {
   debounceTime, distinctUntilChanged, switchMap
 } from 'rxjs/operators';

import { KubeaRecord } from '../kubea_const';
import { KubeaService } from '../kubea.service';

@Component({
  selector: 'app-kubea-search',
  templateUrl: './kubea-search.component.html',
  styleUrls: ['./kubea-search.component.css']
})
export class KubeaSearchComponent implements OnInit {
  kubeas$: Observable<KubeaRecord[]>;
  private searchTerms = new Subject<string>();

  constructor(private kubeaService: KubeaService) {}

  // Push a search term into the observable stream.
  search(term: string): void {
    this.searchTerms.next(term);
  }

  ngOnInit(): void {
    this.kubeas$ = this.searchTerms.pipe(
      // wait 300ms after each keystroke before considering the term
      debounceTime(300),

      // ignore new term if same as previous term
      distinctUntilChanged(),

      // switch to new search observable each time the term changes
      switchMap((term: string) => this.kubeaService.searchKubEA(term)),
    );
  }
}
