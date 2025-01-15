import {Routes} from '@angular/router';
import {LoginPageComponent} from "./pages/login-page/login-page.component";
import {SearchPageComponent} from "./pages/search-page/search-page.component";
import {ProfilePageComponent} from "./pages/profile-page/profile-page.component";
import {HomePageComponent} from "./pages/home-page/home-page.component";
import {SidebarComponent} from "./common-ui/sidebar/sidebar.component";
import {HeaderComponent} from "./common-ui/header/header.component";
import {LayoutComponent} from "./common-ui/layout/layout.component";


export const routes: Routes = [
  {
    path: '', component: LayoutComponent, children: [
      {
        path: '', component: HeaderComponent, children: [
          {path: '', component: HomePageComponent},
          {path: 'search', component: SearchPageComponent},
          {path: 'home', component: HomePageComponent},
          {path: 'profile', component: ProfilePageComponent},
        ]
      },
    ]
  },
  {path: 'login', component: LoginPageComponent}
];
