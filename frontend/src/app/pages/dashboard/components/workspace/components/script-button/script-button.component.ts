import { ChangeDetectionStrategy, Component, EventEmitter, Input, Output } from '@angular/core';

import { ScriptButton } from '../../../../../../interfaces/script-button.interface';

@Component({
  selector: 'app-script-button',
  templateUrl: './script-button.component.html',
  styleUrl: './script-button.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ScriptButtonComponent {

  @Input() scriptButtonData: ScriptButton = { id: '', name: '' }
  @Output() editScriptEvent = new EventEmitter<ScriptButton>();
  @Output() launchScriptEvent = new EventEmitter<ScriptButton>();

  editScript() {
    this.editScriptEvent.emit(this.scriptButtonData);
  }

  launchScript() {
    this.launchScriptEvent.emit(this.scriptButtonData);
  }
}
