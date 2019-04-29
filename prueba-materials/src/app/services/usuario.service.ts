import { Injectable } from '@angular/core';
import { tap, catchError } from 'rxjs/operators';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Usuario } from '../models/usuario.model';
import { UserRequest } from '../models/userRequest.model';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {


  constructor(private http: HttpClient) { }

  private loginUrl = 'http://localhost:8001/file/login/';
  private userChangeUrl = 'http://localhost:8001/file/user/';
  private userRequestUrl = 'http://localhost:8001/file/request_for_user/';
  private logoutUrl = 'http://localhost:8001/file/logout/';
  private filesUrl = 'http://localhost:8001/file/list_files/';
  private registerUrl = 'http://localhost:8001/file/register/';

  getRequest(user: Usuario): Observable<UserRequest> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'application/json');

    return this.http.post(this.userRequestUrl, user, {headers: headers}  ).pipe(
      tap((res: UserRequest) => this.log(`usuario recivido= ${res}`)),
      catchError(this.handleError<UserRequest>('error de peticion UserRequest'))
    );
  }

  getFiles(user: Usuario): Observable<UserRequest> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'application/json');

    return this.http.post(this.filesUrl, user, {headers: headers}  ).pipe(
      tap((res: UserRequest) => this.log(`usuario recivido= ${res}`)),
      catchError(this.handleError<UserRequest>('error de peticion UserRequest'))
    );
  }

  logout(user: Usuario): Observable<Usuario> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': 'my-auth-token',
        'Access-Control-Allow-Origin': '*'
      })
    };

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');


    console.log(user);
    return this.http.post<Usuario>(this.logoutUrl, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`usuario recivido=${res}`)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }

  login(user: Usuario): Observable<Usuario> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');

    return this.http.post<Usuario>(this.loginUrl, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`usuario recivido=${res}`)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }

  register(user: Usuario): Observable<Usuario> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'POST');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'plain/text');
    headers.append('responseType', 'blob');

    return this.http.post<Usuario>(this.registerUrl, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`usuario recivido=${res}`)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }

  change(user: Usuario): Observable<Usuario> {

    const headers = new HttpHeaders();
    headers.append('Access-Control-Allow-Methods', 'PUT');
    headers.append('Access-Control-Allow-Origin', '*');
    headers.append('Access-Control-Allow-Headers', 'Content-Type');
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('responseType', 'blob');

    return this.http.put<Usuario>(this.userChangeUrl + user.id, user, {headers: headers}  ).pipe(
      tap((res: Usuario) => this.log(`usuario recivido= ${res['username']}`)),
      catchError(this.handleError<Usuario>('error de envio de usuario'))
    );
  }


  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      console.error(error);

      this.log(`${operation} failed: ${error.message}`);

      return of(result as T);
    };
  }

  private log(entrada: string) {
    console.log(entrada);
  }
}