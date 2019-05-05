import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/shared/services/provider.service';
import { AuthService } from 'src/app/shared/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.sass']
})
export class LoginComponent implements OnInit {

  public username: any = "";

  public password: any = "";

  constructor(
    private provider: ProviderService,
    private auth: AuthService
  ) { }

  ngOnInit() {
  }

  login() {
    if (this.username !== '' && this.password !== '') {
      this.auth.login(this.username, this.password);
    }
  }

}
