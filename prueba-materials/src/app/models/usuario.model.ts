export class Usuario {
    id: any;
    username: string;
    password: string;
    first_name: string;
    last_name: string;
    email: string;

    constructor(username?: string, password?: string) {
        this.username = username;
        this.password = password;
    }

}
