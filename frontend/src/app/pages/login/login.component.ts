import { ChangeDetectionStrategy, Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class LoginComponent {

  loginObj: LoginModel  = new LoginModel();

  constructor(private router: Router) {};

  onLogin() {
    console.log('im here');
  //   const localUsers =  localStorage.getItem('angular17users');
  //   if(localUsers != null) {
  //     const users =  JSON.parse(localUsers);

  //     const isUserPresent =  users.find( (user:SignUpModel)=> user.email == this.loginObj.email && user.password == this.loginObj.password);
  //     if(isUserPresent != undefined) {
  //       alert("User Found...");
  //       localStorage.setItem('loggedUser', JSON.stringify(isUserPresent));
        this.router.navigateByUrl('/dashboard');
  //     } else {
  //       alert("No User Found")
  //     }
  //   }
  }
}

export class LoginModel  { 
  deviceId: string;
  password: string;

  constructor() {
    this.deviceId = ""; 
    this.password = "";
  }
}
