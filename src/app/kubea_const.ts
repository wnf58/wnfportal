export class KubeaRecord {
  id: number;
  kurz: string;
  bez: string;
  datum: number;
  betrag: number;
}

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

export const DEFAULTKONTOSTANDSUMME: KontostandSummeRecord = { summe: 11.11 };
