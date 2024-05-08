import { Injectable } from '@angular/core';
import { Observable, Subject, of } from 'rxjs';
import { cloneDeep } from 'lodash';

import { APIService } from './api.service';
import { ScriptButton } from '../interfaces/script-button.interface';

@Injectable({
  providedIn: 'root'
})
export class WorkspaceService {

  private buttonsInner: ScriptButton[] = [];
  private buttons$: Subject<ScriptButton[]> = new Subject<ScriptButton[]>();

  constructor(private apiService: APIService) { }

  addButton(): void {
    let id: number = this.buttonsInner.length == 0 ? 
      0 : Number.parseInt(this.buttonsInner[this.buttonsInner.length - 1].id) + 1;
    
    this.buttonsInner.push({ id: id.toString(), name: `Funny Name #${id}` });
    this.buttons$.next(cloneDeep(this.buttonsInner));
  }

  getButtonsAsObservable(): Observable<ScriptButton[]> {
    return this.buttons$.asObservable();
  }
}
