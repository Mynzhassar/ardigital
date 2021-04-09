export interface Profit {
  id: number;
  image: string;
  description: string;
}

export interface Service {
  id: number;
  title: string;
  image: string;
  description: string;
}

export interface Consultation {
  id: number;
  service: number;
  full_name: string;
  telephone_number: string;
  email: string;
  status: string;
  receipted_time: Date;
  response_time: Date;
  was_notified: boolean;
}
