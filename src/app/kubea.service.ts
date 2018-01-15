import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { catchError, map, tap } from 'rxjs/operators';

import { KubeaRecord, KUBEADEMO } from './kubea_const';
import { MessageService } from './message.service';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json'})
};

@Injectable()
export class KubeaService {

  // private kubeaUrl = 'api/kubea';  // URL to web api
  //No 'Access-Control-Allow-Origin' header is present
  //private kubeaUrl = 'http://c2016.fritz.box:8081/kontostandLetzterMonat'
  private kubeaUrl = 'http://c2016.fritz.box:8081'

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

  getKubEARecords(): Observable<KubeaRecord[]> {
    return this.http.get<KubeaRecord[]>(this.kubeaUrl+'/jsonListEA')
      .pipe(
        tap(kubea => this.log('fetched kubea')),
        catchError(this.handleError('getKubEA', []))
      );
  }

  /** GET kubea by id. Return `undefined` when id not found */
  getKubEANo404<Data>(id: number): Observable<KubeaRecord> {
    const url = `${this.kubeaUrl}/?id=${id}`;
    return this.http.get<KubeaRecord[]>(url)
      .pipe(
        map(kubea => kubea[0]), // returns a {0|1} element array
        tap(h => {
          const outcome = h ? `fetched` : `did not find`;
          this.log(`${outcome} kubea id=${id}`);
        }),
        catchError(this.handleError<KubeaRecord>(`getKubEA id=${id}`))
      );
  }

  /** GET kubea by id. Will 404 if id not found */
  getKubEA(id: number): Observable<KubeaRecord> {
    const url = `${this.kubeaUrl}/jsonDetailEA/${id}`;
    return this.http.get<KubeaRecord>(url).pipe(
      tap(_ => this.log(`fetched kubea id=${id}`)),
      catchError(this.handleError<KubeaRecord>(`getKubEA id=${id}`))
    );
  }

  /* GET KubEA whose name contains search term */
  searchKubEA(term: string): Observable<KubeaRecord[]> {
    if (!term.trim()) {
      // if not search term, return empty kubea array.
      return of([]);
    }
    return this.http.get<KubeaRecord[]>(`api/kubea/?name=${term}`).pipe(
      tap(_ => this.log(`found KubeaRecord matching "${term}"`)),
      catchError(this.handleError<KubeaRecord[]>('searchKubEA', []))
    );
  }

  //////// Save methods //////////

  /** POST: add a new kubea to the server */
  addKubEA (kubea: KubeaRecord): Observable<KubeaRecord> {
    return this.http.post<KubeaRecord>(this.kubeaUrl, kubea, httpOptions).pipe(
      tap((kubea: KubeaRecord) => this.log(`added kubea w/ id=${kubea.id}`)),
      catchError(this.handleError<KubeaRecord>('addKubEA'))
    );
  }

  /** DELETE: delete the kubea from the server */
  deleteKubEA (kubea: KubeaRecord | number): Observable<KubeaRecord> {
    const id = typeof kubea === 'number' ? kubea : kubea.id;
    const url = `${this.kubeaUrl}/${id}`;

    return this.http.delete<KubeaRecord>(url, httpOptions).pipe(
      tap(_ => this.log(`deleted kubea id=${id}`)),
      catchError(this.handleError<KubeaRecord>('deleteKubEA'))
    );
  }

  /** PUT: update the kubea on the server */
  updateKubEA (kubea: KubeaRecord): Observable<any> {
    return this.http.put(this.kubeaUrl, kubea, httpOptions).pipe(
      tap(_ => this.log(`updated kubea id=${kubea.id}`)),
      catchError(this.handleError<any>('updateKubEA'))
    );
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  /** Log a kubeaService message with the MessageService */
  private log(message: string) {
    this.messageService.add('kubeaService: ' + message);
  }
}
