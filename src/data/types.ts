export type Letter = "A" | "B" | "C" | "D";

export type Question = {
  id: number;
  tema: string;
  stem: string;
  options: Record<Letter, string>;
  answer: Letter;
  explain: string;
};

export const LETTERS: Letter[] = ["A", "B", "C", "D"];
