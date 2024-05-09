import { ChangeDetectionStrategy, ChangeDetectorRef, Component } from '@angular/core';
import { Router } from '@angular/router';

import { APIService } from '../../services/api.service';
import { LoginModel } from '../../interfaces/api-interfaces.interface';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class LoginComponent {

  loginObj: LoginFormModel  = new LoginFormModel();
  loggingIn: boolean = false;

  constructor(
    private router: Router,
    private apiService: APIService,
    private changeDetectorRef: ChangeDetectorRef
  ) {};

  onLogin() {
    const loginModelObj: LoginModel = {
      device_number: this.loginObj.deviceId,
      password: this.loginObj.password
    };

    if (loginModelObj.device_number != "" && loginModelObj.password != "") {
      this.loggingIn = true;
      this.apiService.login(loginModelObj)
        .subscribe(({message, access_token}) => {
          if (message != 'Login failed') {
            localStorage.setItem('access_token', access_token);
            this.router.navigateByUrl('/dashboard');
          }

          this.loggingIn = false;
          this.changeDetectorRef.detectChanges();
        });
    };
  }
}

class LoginFormModel  { 
  deviceId: string;
  password: string;

  constructor() {
    this.deviceId = ""; 
    this.password = "";
  }
}
