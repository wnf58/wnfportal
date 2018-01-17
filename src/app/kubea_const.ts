export class KubeaRecord {
  id: number;
  kurz: string;
  bez: string;
  datum: number;
  betrag: number;
}

export const KUBEADEMO: KubeaRecord[] = [
  { id: 11, kurz: 'kurz_11', bez: 'bez_11', datum: Date.now(), betrag: 11.11 },
  { id: 12, kurz: 'kurz_12', bez: 'bez_12', datum: Date.now(), betrag: 12.12 }
];

export class KontoRecord {
  id: number;
  kurz: string;
  bez: string;
  datum: number;
  betrag: number;
}

export class KontostandSummeRecord {
  summe: number;
}

export const KONTOSTANDDEMO: KontoRecord[] = [
  { id: 11, kurz: 'konto_kurz_11', bez: 'konto_bez_11', datum: Date.now(), betrag: 11.11 },
  { id: 12, kurz: 'konto_kurz_12', bez: 'konto_bez_12', datum: Date.now(), betrag: 12.12 }
];
