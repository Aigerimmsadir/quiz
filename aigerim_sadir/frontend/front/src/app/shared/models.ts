export interface IUser {
    id: number,
    username: string,
    email: string
}

export interface ITaskList {
    id: number,
    name: string,
    owner: IUser
}

export interface ITaskShort {
    id: number,
    name: string,
    status: string
}

export interface ITaskLong {
    id: number,
    name: string,
    created_at: string,
    due_on: string,
    status: string
}

export interface IAuthResponse {
    token: string;
}

export interface ITaskNew {
    id: number,
    name: string,
    created_at: string,
    due_on: string,
    status: string,
    task_list: ITaskList,
    owner: IUser
}