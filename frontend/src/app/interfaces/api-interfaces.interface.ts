import { DEFAULT_SCRIPT_NAME } from "../constants/const";

export interface LoginModel {
    device_number: string;
    password: string;
}

export interface LoginResponse {
    message: string;
    access_token: string;
}

export interface CreateResponse {
    message: string;
    script_id: number;
}

export class CreateRequest {
    script_name: string = DEFAULT_SCRIPT_NAME;
    content: string = "";
}

export interface UpdateResponse {
    message: string;
}

export interface ExecuteResponse {
    message: string;
}

export class UpdateRequest {
    script_name: string = DEFAULT_SCRIPT_NAME;
    content: string = "";
}