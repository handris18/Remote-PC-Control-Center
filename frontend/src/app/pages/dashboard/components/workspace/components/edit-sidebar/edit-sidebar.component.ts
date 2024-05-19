import { ChangeDetectionStrategy, Component, inject, ChangeDetectorRef } from '@angular/core';
import { Subject, takeUntil } from 'rxjs';
import { NgbActiveOffcanvas } from '@ng-bootstrap/ng-bootstrap';

import { ScriptButton, ScriptObject } from '../../../../../../interfaces/script-button.interface';
import { SidebarService } from '../../../../../../services/sidebar.service';

@Component({
  selector: 'app-edit-sidebar',
  templateUrl: './edit-sidebar.component.html',
  styleUrls: ['./edit-sidebar.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class EditSidebarComponent {

  private closeNotifier$ = new Subject<number>();

  scriptButton: ScriptButton = { id: '', name: '' }; 
  scriptText: string = '';
  activeOffcanvas = inject(NgbActiveOffcanvas);

  constructor (
    private sidebarService: SidebarService,
    private changeDetectorRef: ChangeDetectorRef
  ) { }

  ngOnInit(): void {
    this.sidebarService.getScriptButtonAsObservable()
      .pipe(takeUntil(this.closeNotifier$))
      .subscribe(scrBtn => {
        this.scriptButton = scrBtn;
        this.changeDetectorRef.detectChanges();
      });
    this.sidebarService.getScriptTextAsObservable()
      .pipe(takeUntil(this.closeNotifier$))
      .subscribe(scrTxt => {
        this.scriptText = scrTxt;
        this.changeDetectorRef.detectChanges();
      });
  }

  ngOnDestroy(): void {
    this.closeNotifier$.next(0);
  }

  saveScript(): void {
    let scriptObj: ScriptObject = { ...this.scriptButton, content: this.scriptText };
    this.sidebarService.saveScript(scriptObj).subscribe(
      _ => this.activeOffcanvas.close()
    );
  }
}
