import { Injectable } from '@angular/core';
import { Observable, Subject, of } from 'rxjs';
import { cloneDeep } from 'lodash';

import { APIService } from './api.service';
import { ScriptButton } from '../interfaces/script-button.interface';
import { DEFAULT_SCRIPT_NAME } from '../constants/const';

@Injectable({
  providedIn: 'root'
})
export class WorkspaceService {

  private buttonsInner: ScriptButton[] = [];
  private buttons$: Subject<ScriptButton[]> = new Subject<ScriptButton[]>();

  constructor(private apiService: APIService) { }

  addButton(): void {
    this.apiService.createScript().subscribe(
      response => {
        const {message, script_id} = response;
        if (script_id != -1) {
          this.buttonsInner.push({ id: script_id.toString(), name: DEFAULT_SCRIPT_NAME });
          this.buttons$.next(cloneDeep(this.buttonsInner));
        }
      }
    )
  }

  fetchButtons() {
    this.apiService.fetchAllScripts().subscribe(
      buttonList => {
        this.buttonsInner = buttonList;
        this.buttons$.next(cloneDeep(this.buttonsInner));
      }
    );
  }

  getButtonsAsObservable(): Observable<ScriptButton[]> {
    return this.buttons$.asObservable();
  }
}
