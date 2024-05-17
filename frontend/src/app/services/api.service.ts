import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, catchError, map, of, tap } from 'rxjs';

import { CreateRequest, CreateResponse, ExecuteResponse, LoginModel, LoginResponse, UpdateRequest, UpdateResponse } from '../interfaces/api-interfaces.interface';
import { API_ENDPOINTS } from '../constants/const';
import { ScriptButton, ScriptObject } from '../interfaces/script-button.interface';


@Injectable({
  providedIn: 'root'
})
export class APIService {

  private httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  
  constructor (private httpClient: HttpClient) {}

  login({device_number, password}: LoginModel): Observable<LoginResponse> {
    return this.httpClient.post<LoginResponse>(
      API_ENDPOINTS.login, {device_number, password}, this.httpOptions).pipe(
        tap(_ => localStorage.setItem('loggedUser', device_number)),
        catchError(this.handleError<LoginResponse>('login', { message: 'Login failed', access_token: '' }))
      );
  }

  fetchAllScripts(): Observable<Array<ScriptButton>> {
    return this.httpClient.get<any[]>(API_ENDPOINTS.fetchScripts, this.httpOptions).pipe(
        map(scriptList => scriptList.reduce<Array<ScriptButton>>(
          (buttonList, scriptElem) => {
            const [id, name] = scriptElem;
            buttonList.push({id, name});
            return buttonList;
          },
          new Array<ScriptButton>())),
        catchError(this.handleError<Array<ScriptButton>>('fetchAll', []))
      )
  }

  createScript(): Observable<CreateResponse> {
    let requestBody = new CreateRequest();
    return this.httpClient.post<CreateResponse>(
      API_ENDPOINTS.createScript, requestBody, this.httpOptions).pipe(
        catchError(this.handleError<CreateResponse>('create', { message: 'Create failed', script_id: -1 }))
      );
  }

  fetchScript(id: number): Observable<ScriptObject | null> {
    return this.httpClient.get<any>(
      API_ENDPOINTS.fetchScript(id), this.httpOptions).pipe(
        map<any, ScriptObject>(tuple => {
          const [id, name, content] = tuple;
          return {id, name, content};
        }),
        catchError(this.handleError<ScriptObject | null>('fetch', null))
      )
  }

  updateScript(scriptObj: ScriptObject): Observable<UpdateResponse> {
    const {id, name, content} = scriptObj;
    let requestBody: UpdateRequest = { script_name: name, content };

    return this.httpClient.put<UpdateResponse>(
      API_ENDPOINTS.updateScript(parseInt(id)), requestBody, this.httpOptions).pipe(
        catchError(this.handleError<UpdateResponse>('update'))
      )
  }

  executeScript(id: number): Observable<ExecuteResponse> {
    return this.httpClient.post<any>(
      API_ENDPOINTS.executeScript(id), this.httpOptions).pipe(
        catchError(this.handleError<ExecuteResponse>('execute'))
      )
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      console.log(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }
}
